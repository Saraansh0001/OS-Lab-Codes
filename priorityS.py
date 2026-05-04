# Priority Scheduling (Non-Preemptive)

p = ["P1","P2","P3","P4","P5"]
at = [0,1,2,3,4]
bt = [5,3,8,6,2]
pr = [2,1,4,3,5]   # smaller number = higher priority

n = len(p)

ct = [0]*n
tat = [0]*n
wt = [0]*n
done = [0]*n

time = 0
completed = 0

while completed < n:
    idx = -1
    best_pr = 9999

    for i in range(n):
        if at[i] <= time and done[i] == 0:
            if pr[i] < best_pr:
                best_pr = pr[i]
                idx = i

    if idx != -1:
        time += bt[idx]
        ct[idx] = time
        done[idx] = 1
        completed += 1
    else:
        time += 1   # CPU idle

for i in range(n):
    tat[i] = ct[i] - at[i]
    wt[i] = tat[i] - bt[i]

avg_tat = sum(tat)/n
avg_wt = sum(wt)/n

print("P AT BT PR CT TAT WT")
for i in range(n):
    print(p[i], at[i], bt[i], pr[i], ct[i], tat[i], wt[i])

print("Average TAT =", avg_tat)
print("Average WT =", avg_wt)
