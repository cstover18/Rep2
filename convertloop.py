# Fahrenheit Converter On a Loop

def main():
    celsius = eval(input("What is the Celsius temperature?"))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degress Fahrenheit.")


for i in range(5):
    main()
