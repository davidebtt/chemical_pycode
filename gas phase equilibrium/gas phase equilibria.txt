#copy paste your code in python and solve your exercise.
#Try Google colab It is free!
#Link: https://colab.research.google.com/
#please insert your data using dots to separate decimals
#please do not use commas to separate decimals
#GAS EQUILIBRIA
#Having the following chemical equation calculate [H2] [I2] [HI] at equilibrium
#[A] + [B] <-> 2[C]
#[I2] + [H2] <-> 2[HI]
#calculate [HI] at equilibrium.


import math

# Constants
Keq = 0.02 # Equilibrium constant
temp_K = 700 # Temperature in Kelvin

# Input
I2_initial = float(input("Insert initial I2 mol (positive value): "))
H2_initial = float(input("Insert initial H2 mol (positive value): "))

# Check that the values are positive
if I2_initial <= 0 or H2_initial <= 0:
    print("Error: Initial mol values must be positive.")
else:
    # Option 1: Initial I2 and H2 are the same
    if I2_initial == H2_initial:
        HI_eq = round(math.sqrt(Keq * I2_initial * H2_initial), 4)
        I2_eq = round(I2_initial - (HI_eq / 2), 4)
        H2_eq = round(H2_initial - (HI_eq / 2), 4)

    # Option 2: Initial H2 is greater than I2
    elif H2_initial > I2_initial:
        HI_eq = round(math.sqrt(Keq * I2_initial**2), 4)
        I2_eq = round(I2_initial - (HI_eq / 2), 4)
        H2_eq = round(H2_initial - (HI_eq / 2), 4)

    # Option 3: Initial I2 is greater than H2
    else:
        HI_eq = round(math.sqrt(Keq * H2_initial**2), 4)
        I2_eq = round(I2_initial - (HI_eq / 2), 4)
        H2_eq = round(H2_initial - (HI_eq / 2), 4)

    # Output
    print(f"""
At {temp_K} K the equilibrium constant is {Keq}:
- HI mol at equilibrium: {HI_eq} mol
- I2 mol at equilibrium: {I2_eq} mol
- H2 mol at equilibrium: {H2_eq} mol
""")