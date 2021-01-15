    def Bartels(datas):
        datas = pd.Series(datas)
        n = len(datas.values)
        R = pd.Series(range(0, len(datas)))
        m = np.sum(R.values)/len(R.values)
        t1 = R[1:(n - 1)]
        t2 = R[2:n]
        U = np.divide(sum(np.power(np.subtract(t1.values, t2.values), 2)), np.sum(np.power(np.subtract(R.values,m), 2)))
        pvalue = stats.norm.cdf(U, loc=2, scale=20/(5*n + 7))
        return U, pvalue
