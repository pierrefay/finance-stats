# finance-stats

*Bartels (1982)*

Statistical test in Python for n >= 100

The ranks r[1], ..., r[n] of the X[i], ..., X[n] are used for the statistic:

T = ∑_{i=1}^n (r[i] - r[i+1])^2 / ∑(r[i] - meanr)^2

For p-value calculation we require a sample sizes n >= 100 and we do a normal approximation with N(2, 20/(5n + 7)).
