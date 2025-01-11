# This program calculates the mass of a gas in a container based on the Ideal Gas Law.
# It allows the user to choose one of five gases (CH4, O2, H2, CO2, N2), and input the container's volume (in liters),
# the temperature (in Celsius), and the pressure (in atm). Using the Ideal Gas Law, the program computes the
# number of moles of the gas and its mass. Additionally, it generates a graph to show how the gas mass changes
# with pressure for the given conditions.

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Constants
R = 0.0821  # Ideal gas constant in L*atm/(mol*K)
MW_gases = {
    "CH4": 16.04,  # Molecular weight of methane in g/mol
    "O2": 32.00,   # Molecular weight of oxygen in g/mol
    "H2": 2.016,   # Molecular weight of hydrogen in g/mol
    "CO2": 44.01,  # Molecular weight of carbon dioxide in g/mol
    "N2": 28.02    # Molecular weight of nitrogen in g/mol
}

# Step 1: Choose the gas
gas_choice = input("Choose a gas (CH4, O2, H2, CO2, N2): ").strip().upper()
if gas_choice not in MW_gases:
    raise ValueError("Invalid gas choice. Please choose from CH4, O2, H2, CO2, or N2.")
MW = MW_gases[gas_choice]

# Step 2: Input the values for volume, temperature, and pressure
volume_L = float(input("Enter the volume of the container in L: "))  # in L
temperature_C = float(input("Enter the temperature of the gas in °C: "))  # in Celsius
pressure_atm = float(input("Enter the pressure of the gas in atm: "))  # in atm

# Step 3: Convert the units to standard SI units
temperature_K = temperature_C + 273.15  # Convert Celsius to Kelvin

# Step 4: Use the Ideal Gas Law to calculate the number of moles
# PV = nRT -> n = PV / RT
n_moles = (pressure_atm * volume_L) / (R * temperature_K)

# Step 5: Calculate the mass of the chosen gas
gas_mass = n_moles * MW

# Print the result
print(f"The mass of {gas_choice} in the container is {gas_mass:.2f} g.")

# Step 6: Create a graph showing the dependence of gas mass on pressure
pressures_atm = np.linspace(0.5, 300, 100)  # Generate a range of pressures in atm
masses = (pressures_atm * volume_L) / (R * temperature_K) * MW  # Calculate masses

# Plot the graph
plt.figure(figsize=(8, 5))
plt.plot(pressures_atm, masses, label=f"Mass of {gas_choice}")
plt.title(f"Dependence of {gas_choice} Mass on Pressure")
plt.xlabel("Pressure (atm)")
plt.ylabel(f"Mass of {gas_choice} (g)")
plt.grid()
plt.legend()
plt.show()
