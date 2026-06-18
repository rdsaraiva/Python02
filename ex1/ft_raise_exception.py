def input_temp(temp_str: str) -> int:
    temp = int(temp_str)
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants "
                         f"(max 40°C)")
    elif temp < 0:
        raise ValueError(f"{temp}°C is too cold for plant "
                         f"(min 0°C)")
    return temp


def test_temp() -> None:
    print("=== Garden Temperature Checker ===\n")

    test_inputs = ["25", "abc", "100", "-50"]

    for temp_str in test_inputs:
        print(f"Input data is '{temp_str}'")
        try:
            temp = input_temp(temp_str)
            print(f"Temperature is now {temp}°C\n")
        except ValueError as e:
            print(f"Caught input tempetarture error: {e}\n")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temp()