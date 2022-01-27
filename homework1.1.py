x = int(input("Define x: "))
y = int(input("Define y: "))

if y != 0:
    print(x, "/", y, "=", int(x / y))
    print("Remainder: ", int(x % y))
else:
    print("Undefined")
