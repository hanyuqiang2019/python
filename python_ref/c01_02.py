principal=1000  # 初始金额
rate = 0.05     # 利率
numyears = 5    # 年数
year = 1

while year <= numyears:
    principal = principal * (1 + rate)
    print ("%3d %0.2f" % (year, principal) )    
    year += 1

