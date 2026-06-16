def input_temp(temp_str: str) -> int:
    return int(temp_str)

def test_temp() -> None:
    print("=== Garden Temperature ===\n")

    test_inputs = ["25", "abc"]
    
    for temp_str in test_inputs:
        print(f"Input data is '{temp_str}'")
        try:
            temp = input_temp(temp_str)
            print(f"Temperature is now {temp}°C\n")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}\n")
        
    print("All tests completed - program didn't crash!")
        
    

if __name__ == "__main__":
    test_temp()