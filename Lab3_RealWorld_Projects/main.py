# main.py

from telemetry import process_telemetry
from diagnostic import (
    detect_abnormal,
    analyze_fault,
    final_diagnostic,
    execution_log
)


# Values from the first program
LAST_NAME = "DANTES"
SEED_NUM = 5
FAVORITE_ARTIST = "ONE DIRECTION"


# Process telemetry
valid_values, invalid_values = process_telemetry(
    LAST_NAME,
    SEED_NUM,
    FAVORITE_ARTIST
)


# Detect abnormal conditions
abnormal = detect_abnormal(valid_values)


# Recursive analysis
recursive_trace = analyze_fault(abnormal)


# Final equipment status
status = final_diagnostic(
    valid_values,
    abnormal
)


# OUTPUT

print("=== Student Specific Inputs ===")
print("Surname:", LAST_NAME)
print("SEED_NUM:", SEED_NUM)
print("Favorite Artist:", FAVORITE_ARTIST)


print("\n=== Generated Telemetry Data ===")
for value in valid_values:
    print(value)


print("\n=== Valid / Invalid Results ===")
print("Valid Readings:", len(valid_values))
print("Invalid Readings:", len(invalid_values))

for error in invalid_values:
    print("Invalid:", error)


print("\n=== Processed Results ===")
for value in valid_values:
    print("Processed:", value)


print("\n=== Detected Abnormal Conditions ===")
if len(abnormal) == 0:
    print("No abnormal conditions detected.")
else:
    for condition in abnormal:
        print(condition)


print("\n=== Recursive Analysis ===")
for step in recursive_trace:
    print(step)


print("\n=== Final Diagnostic Summary ===")
print("Processed Readings:", len(valid_values))
print("Valid Readings:", len(valid_values))
print("Invalid Readings:", len(invalid_values))
print("Abnormal Conditions:", len(abnormal))
print("Overall Equipment Status:", status)


print("\n=== Execution Log ===")
for log in execution_log:
    print(log)


print("\n=== Final Output ===")
print("Equipment Status:", status)