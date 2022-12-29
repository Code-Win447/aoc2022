#day 2 of advent of code 2022
score = 0
pchoice = ['X', 'Y', 'Z']
echoice = ['A', 'B', 'C']
with open('input.txt') as f:
    data = f.read().splitlines()
for line in data:
    score += int(pchoice.index(line[-1])+1)
    if int(echoice.index(line[0]))==int(pchoice.index(line[-1])):
        score += 3
    elif int(echoice.index(echoice[int(echoice.index(line[0]))]))==int(pchoice.index(pchoice[int(pchoice.index(line[-1]))-1])):
        score += 6
    else:
        continue

print(score)
