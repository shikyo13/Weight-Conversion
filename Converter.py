weight  = input("Weight: ")
unit = input("(K)g or (L)bs: ")

if unit.upper() == "K":
    result = float(weight) * 2.2
    print("Weight in Lbs:",result)
else:
    result = float(weight) / 2.2
    print ("Weight in Kg:",result)
