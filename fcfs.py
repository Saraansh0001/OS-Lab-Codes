p = ["P1","P2","P3","P4"]
at = [0,10,2,3]
bt = [5,3,8,6]

data = list(zip(at,bt,p))
data.sort()

at , bt , p =zip(*data)

n = len(p)

ct = [0]*n
tat = [0]*n
wt = [0]*n

ct[0] = at[0] + bt[0]
for i in range(1,n):
    if ct[i-1] < at[i]:
        ct[i] = at[i] + bt[i]
    else:
        ct[i] = ct[i-1] + bt[i]

for i in range(n):
    tat[i] = ct[i] - at[i]
    wt[i] = tat[i] - bt[i]

avg_tat = sum(tat)/n
avg_wt = sum(wt)/n

print("P  AT  BT  CT  TAT  WT")
for i in range(n):
    print(p[i], at[i], bt[i], ct[i], tat[i], wt[i])

print("Average TAT =", avg_tat)
print("Average WT =", avg_wt)


commit chekc
