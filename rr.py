p = ["P1","P2","P3","P4","P5"]
at = [0,2,4,6,8]
bt = [5,3,1,2,4]

n = 5
tq = 3

rem_bt = bt.copy()
ct = [0]*n
tat = [0]*n
wt = [0]*n

time = 0
queue = []
visited = [0]*n

# first process
queue.append(0)
visited[0] = 1

while queue:
    i = queue.pop(0)

    if rem_bt[i] > tq:
        time += tq
        rem_bt[i] -= tq
    else:
        time += rem_bt[i]
        rem_bt[i] = 0
        ct[i] = time

    # add newly arrived processes
    for j in range(n):
        if at[j] <= time and visited[j] == 0:
            queue.append(j)
            visited[j] = 1

    # if process not finished, push again
    if rem_bt[i] > 0:
        queue.append(i)

# calculate TAT & WT
for i in range(n):
    tat[i] = ct[i] - at[i]
    wt[i] = tat[i] - bt[i]

avg_tat = sum(tat)/n
avg_wt = sum(wt)/n

print("P AT BT CT TAT WT")
for i in range(n):
    print(p[i], at[i], bt[i], ct[i], tat[i], wt[i])

print("Average TAT =", avg_tat)
print("Average WT =", avg_wt)
