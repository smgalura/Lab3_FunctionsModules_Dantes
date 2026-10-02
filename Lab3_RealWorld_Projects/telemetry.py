# telemetry.py

def generate_telemetry(name, seed, artist):
    name_sum = sum(ord(c) for c in name)
    artist_sum = sum(ord(c) for c in artist)

    data = [
        40 + (name_sum % 50) + seed,
        20 + (artist_sum % 60) + seed,
        round(1 + ((name_sum + artist_sum) % 100) / 10, 1),
        200 + ((name_sum * seed) % 40),

        # Extra telemetry values
        50 + seed,
        10 + (artist_sum % 30),
        100 + (name_sum % 80)
    ]

    for value in data:
        yield value


# Lambda function
transform = lambda value: round(value * 1.05, 2)


def process_telemetry(name, seed, artist):
    valid = []
    invalid = []

    telemetry_stream = generate_telemetry(name, seed, artist)

    for value in telemetry_stream:
        try:
            if not isinstance(value, (int, float)):
                raise TypeError("Telemetry value is not numeric")

            if value < 0:
                raise ValueError("Telemetry value cannot be negative")

            processed_value = transform(value)
            valid.append(processed_value)

        except (TypeError, ValueError) as error:
            invalid.append(str(error))

    return valid, invalid