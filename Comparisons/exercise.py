weight = float(input("Weight: "))

unit = input("(K)g or (L)bs: ").upper();

if unit == "L" :
    converted = weight * 0.45
    print("Weight in Kg: " + str(converted))
else :
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))

