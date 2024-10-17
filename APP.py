Open In Colab

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Menu for the user to choose the conversion type
def temperature_converter():
    print("Select the conversion type:")
    print("1: Convert Celsius to Fahrenheit")
    print("2: Convert Fahrenheit to Celsius")

    choice = int(input("Enter 1 or 2: "))

    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius}°C is equal to {celsius_to_fahrenheit(celsius):.2f}°F")

    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"{fahrenheit}°F is equal to {fahrenheit_to_celsius(fahrenheit):.2f}°C")

    else:
        print("Invalid input! Please enter 1 or 2.")

# Run the temperature converter
temperature_converter()
