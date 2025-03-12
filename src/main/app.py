from lab import *

def main():
    # Convert integer to float
    int_val = int(input("Enter an integer value to convert to float: "))
    float_val = int_to_float(int_val)
    print("Converted to float:", float_val)

    # Convert float to integer
    float_val = float(input("Enter a float value to convert to integer: "))
    int_val = float_to_int(float_val)
    print("Converted to integer:", int_val)

    # Convert string to integer
    str_val = input("Enter a string value to convert to integer: ")
    int_val = str_to_int(str_val)
    print("Converted to integer:", int_val)

    # Convert string to float
    str_val = input("Enter a string value to convert to float: ")
    float_val = str_to_float(str_val)
    print("Converted to float:", float_val)

    # Convert integer to string
    int_val = int(input("Enter an integer value to convert to string: "))
    str_val = int_to_str(int_val)
    print("Converted to string:", str_val)

    # Convert float to string
    float_val = float(input("Enter a float value to convert to string: "))
    str_val = float_to_str(float_val)
    print("Converted to string:", str_val)



if __name__ == "__main__":
    main()
