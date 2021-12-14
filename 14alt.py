file = open("input/14.sam", "r")
lines = file.readlines()
polymer = lines[0].strip()
map = {}
for i,line in enumerate(lines):
    if i < 2: continue
    tr = line.strip().split(" -> ")
    map[tr[0]] = tr[0][0]+tr[1]+tr[0][1]

counter = {}
def add_to_counter(c):
    if c in counter:
        counter[c] += 1
    else:
        counter[c] = 1

def develop(p, remaining=40):
    if remaining > 0:
        r = map[p]
        add_to_counter(r[1])
        develop(r[:2], remaining-1)
        develop(r[1:], remaining-1)

for p in polymer:
    add_to_counter(p)

for i in range(len(polymer)-1):
    develop(polymer[i:i+2])

'''p = polymer[0]
    for i in range(len(polymer)-1):
        p += map[polymer[i:i+2]][1:]
        add_to_counter(p[-2])
    polymer = p
print(counter)'''
print("Part I", max(counter.values())-min(counter.values()))