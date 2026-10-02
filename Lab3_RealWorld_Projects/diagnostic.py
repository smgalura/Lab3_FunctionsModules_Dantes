# diagnostics.py

execution_log = []


# Decorator
def monitor(func):
    def wrapper(*args, **kwargs):
        execution_log.append(func.__name__ + ": STARTED")

        try:
            result = func(*args, **kwargs)
            execution_log.append(func.__name__ + ": SUCCESS")
            return result

        except Exception as error:
            execution_log.append(func.__name__ + ": FAILED")
            print("Processing error:", error)
            return None

    return wrapper


@monitor
def detect_abnormal(values):
    abnormal = []

    for value in values:
        if value > 180:
            abnormal.append(
                "HIGH VALUE: " + str(value)
            )
        elif value < 15:
            abnormal.append(
                "LOW VALUE: " + str(value)
            )

    return abnormal


# Recursive analysis
def analyze_fault(abnormal, index=0, trace=None):
    if trace is None:
        trace = []

    # Base condition
    if index >= len(abnormal):
        trace.append("Analysis complete")
        return trace

    trace.append(
        "Analyzing: " + abnormal[index]
    )

    return analyze_fault(
        abnormal,
        index + 1,
        trace
    )


def final_diagnostic(values, abnormal):
    if len(values) == 0:
        return "NO DATA"

    if len(abnormal) == 0:
        return "NORMAL"

    elif len(abnormal) <= 2:
        return "WARNING"

    else:
        return "CRITICAL"