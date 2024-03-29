# %%
import matplotlib.pyplot as plt
import numpy as np
import seaborn as snb

from scipy.stats import binom as binom_dist
from scipy.stats import beta as beta_dist
from scipy.special import beta as beta_fun
import scipy
# %%
N = 17
y = 1

a0, b0 = 1, 1


# ==================== Task 1.2 ====================

prior = beta_dist(a0, b0)
likelihood = binom_dist(N, y)

a0_post = a0 + y
b0_post = b0 + N - y

posterior = beta_dist(a0_post, b0_post)

mean = posterior.mean()
cred_int_95 = beta_dist.interval(0.95, a0_post, b0_post)

print(f"Mean: {mean}")
print(f"95% credibility interval: {cred_int_95}")

# %% 

# ==================== Task 1.3 ====================
a1_post = 4 + 2
b1_post = 20-4+17

posterior1 = beta_dist(a1_post, b1_post)

mean1 = posterior1.mean()
cred_int_951 = beta_dist.interval(0.95, a1_post, b1_post)

print(f"Mean: {mean1}")
print(f"95% credibility interval: {cred_int_951}")