sum = 0
for i in range(100):
    red = 0
    green = 0
    blue = 0
    line = input().split(":")[1]
    sets = line.split(";")
    for set in sets:
        cubes = set.split(",")
        for colour in cubes:
            num, col = colour.split()
            if col == "red" and int(int(num)) > red:
                red = int(num)
            if col == "green" and int(num) > green:
                green = int(num)
            if col == "blue" and int(num) > blue:
                blue = int(num)
    sum += red * green * blue

print(sum)