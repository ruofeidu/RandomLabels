import random
import itertools

l_wth, l_common, l_g1, l_g2, l_env = [], [], [], [], []

l_envs = {"weather" : l_wth, "environment" : l_env}
l_objects = {"common" : l_common, "group1" : l_g1, "group2" : l_g2}

for obj, l in l_envs.items():
    for line in open("%s.txt" % obj):
        l.append(" ".join(line.strip().split('\t')).lower())
    print(l)

for obj, l in l_objects.items():
    for line in open("%s.txt" % obj):
        l += line.strip().lower().split('\t')
    print(l)

total = len(l_wth) * (len(l_common) * (len(l_g1) + len(l_g2))) * len(l_env)
print("Total combinations if choose one: ", total)
hashset = set()
num = 10000
res = ""

l_g1 += l_g2

l_common2, l_g2, l_g3 = [], [], []
for subset in itertools.combinations(l_common, 2):
    l_common2.append(" ".join(subset))
for subset in itertools.combinations(l_g1, 2):
    l_g2.append(" ".join(subset))
for subset in itertools.combinations(l_g1, 3):
    l_g3.append(" ".join(subset))

total = len(l_wth) * (len(l_common) + len(l_common2) * (len(l_g2) + len(l_g3))) * len(l_env)
print("Total combinations: ", total)

cnt = 0
while cnt < num:
    res = random.choice(l_wth) + " " + random.choice(l_env)
    x = random.randint(0, 2)
    if x == 1:
        res += " " + random.choice(l_common)
    elif x == 2:
        res += " " + random.choice(l_common2)
    x = random.randint(2, 3)
    if x == 2:
        res += " " + random.choice(l_g2)
    elif x == 3:
        res += " " + random.choice(l_g3)
    if res not in hashset:
        hashset.add(res)
    if cnt % 1000 == 0:
        print(res)
    cnt += 1

with open("results.csv", "w") as f:
    for key in hashset:
        f.write("%s\n" % key)