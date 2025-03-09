temperature = float(input('enter temperature' ))
unit_of_temp = input('celsius "c" or fahreheit "f"')

if unit_of_temp == "c":
    convert_temp = (temperature*9/5)+32
    print(convert_temp,'fahrenheit')

elif unit_of_temp== "f":
    convert_temp = (temperature - 32)*5/9
    print(convert_temp,'celsius')
else:
    print ('invalid number')