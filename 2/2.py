colMax = {"red" : 12,
"green" : 13,
"blue" : 14}

sum = 0
for i in range(100):
    valid = True
    line = input().split(":")[1]
    sets = line.split(";")
    for set in sets:
        # print(i+1, set)
        cubes = set.split(",")
        for colour in cubes:
            num, col = colour.split()
            if int(num) > colMax[col]:
                valid = False
                break
        if not valid:
            break
    if not valid:
        continue
    sum += i + 1
print(sum)