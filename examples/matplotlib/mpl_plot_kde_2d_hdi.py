"""
2D KDE with HDI Contours
========================
_gallery_category: Distributions
"""
import matplotlib.pyplot as plt
import numpy as np

import arviz as az

az.style.use("arviz-doc")

rng = np.random.default_rng()
data = rng.multivariate_normal([2, 2], [[1, 0.4], [0.4, 0.8]], 1000000)

ax = az.plot_kde(
    data[:, 0],
    data[:, 1],
    hdi_probs=[0.393, 0.865, 0.989],  # 1, 2 and 3 sigma contours
    contourf_kwargs={"cmap": "Blues"},
)

ax.set_aspect("equal")
plt.show()
