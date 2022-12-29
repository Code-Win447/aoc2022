#day 2 of advent of code 2022
score = 0
pchoice = ['D', 'E', 'F']
res = ['X', 'Y', 'Z']
echoice = ['A', 'B', 'C']
with open('input.txt') as f:
    data = f.read().splitlines()
for line in data:
    score +=int(3*res.index(line[-1]))
    if line[-1] == 'X':
        if line[0] == 'A':
            score += 3
        elif line[0] == 'B':
            score += 1
        elif line[0] == 'C':
            score += 2
    elif line[-1] == 'Y':
        score += int(echoice.index(line[0])+1)
    else:
        if line[0] == 'A':
            score += 2
        elif line[0] == 'B':
            score += 3
        elif line[0] == 'C':
            score += 1
print(score)
