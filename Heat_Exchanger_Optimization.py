import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# INPUT PARAMETERS
# -----------------------------
Th_in = 120   # Hot fluid inlet temp (°C)
Th_out = 80   # Hot fluid outlet temp (°C)
Tc_in = 30    # Cold fluid inlet temp (°C)

U = 500       # Heat transfer coefficient (W/m²K)
A = 10        # Heat transfer area (m²)

flow_rates = np.linspace(0.5, 5, 20)  # kg/s

heat_transfer = []

# -----------------------------
# CALCULATIONS
# -----------------------------
for m in flow_rates:
    
    # Estimate cold outlet temp
    Tc_out = Tc_in + (Th_in - Th_out) * (m / (m + 1))
    
    deltaT1 = Th_in - Tc_out
    deltaT2 = Th_out - Tc_in
    
    # LMTD
    if deltaT1 == deltaT2:
        LMTD = deltaT1
    else:
        LMTD = (deltaT1 - deltaT2) / np.log(deltaT1 / deltaT2)
    
    Q = U * A * LMTD
    heat_transfer.append(Q)

# -----------------------------
# OPTIMIZATION
# -----------------------------
optimal_index = np.argmax(heat_transfer)
optimal_flow = flow_rates[optimal_index]

print(f"Optimal Flow Rate: {optimal_flow:.2f} kg/s")
print(f"Maximum Heat Transfer: {heat_transfer[optimal_index]:.2f} W")

# -----------------------------
# PLOT 1: Heat Transfer vs Flow Rate
# -----------------------------
plt.figure()
plt.plot(flow_rates, heat_transfer, marker='o')
plt.xlabel("Flow Rate (kg/s)")
plt.ylabel("Heat Transfer (W)")
plt.title("Heat Transfer vs Flow Rate")
plt.grid()

plt.savefig("heat_transfer_plot.png")


# -----------------------------
# PLOT 2: Comparison (Co-current vs Counter-current)
# -----------------------------
heat_transfer_cc = [q * 1.15 for q in heat_transfer]

plt.figure()
plt.plot(flow_rates, heat_transfer, label="Co-current", marker='o')
plt.plot(flow_rates, heat_transfer_cc, label="Counter-current", marker='s')
plt.xlabel("Flow Rate (kg/s)")
plt.ylabel("Heat Transfer (W)")
plt.title("Flow Configuration Comparison")
plt.legend()
plt.grid()

plt.savefig("comparison_plot.png")
plt.show()