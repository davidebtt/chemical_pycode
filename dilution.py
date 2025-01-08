# This program help you to dilute concentrated solutions to the desired concentration and volume, Try it!

#M1V1 = M2V2

#V1 = M2V2/M1

M1 = float(input("enter the concentration of the starting solution %wt %v or M "))

M2 = float(input("enter the desired final concentration %wt %v or M "))

V2 = float(input("enter the desired final volume in ml: "))

V1 = round(float((M2*V2)/M1),2)

print("PROCEDURE: ")
print(f"measure {V1} ml of concentrated solution and then dilute with solvent until solution reach volume {V2}")