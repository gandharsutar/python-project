unit=input(("Is this temperatuer in Celsius or Fahrenheit (C/F):"))
temp=float(input("Enter the temperature"))
if unit=="C":
    temp=round((9*temp)/5+32, 2)
    print(f"The temperature in Fahrenhit is: {temp}°F")
elif unit=="F":
    temp=round((temp-32)*5/9, 2)
    print(f"The temperature in Celsius is: {temp}°C")
else:
    print(f"{unit} is an invalid unit of measurement")