import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jv

# plt.style.use("https://raw.githubusercontent.com/cnativid/MPL-Styles/main/default.mplstyle")
plt.style.use("default.mplstyle")

fig, ax = plt.subplots()
x = np.linspace(-10, 10, 100)

for i in range(0, 7):
  J = jv(i, x)
  ax.plot(x, J, label = f"Line{i:g}")

plt.legend()
plt.title("Title")
plt.xlabel("test")
plt.ylabel("test")
plt.show()