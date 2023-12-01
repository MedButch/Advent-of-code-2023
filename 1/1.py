sum = 0
numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
numbersR = {"eno": 1, "owt": 2, "eerht": 3, "ruof": 4, "evif": 5, "xis": 6, "neves": 7, "thgie": 8, "enin": 9}
try:
    while (line := input()):
        number = ""
        for i, char in enumerate(line):
            if char.isnumeric():
                number += char
                break
            elif (val := line[i-2:i+1]) in numbers or (val := line[i-3:i+1]) in numbers or (val := line[i-4:i+1]) in numbers:
                number += str(numbers[val])
                break
        reverse = ''.join(reversed(line))
        for i, char in enumerate(reverse):
            if char.isnumeric():
                number += char
                break
            elif (val := reverse[i-2:i+1]) in numbersR or (val := reverse[i-3:i+1]) in numbersR or (val := reverse[i-4:i+1]) in numbersR:
                number += str(numbersR[val])
                break
        sum += int(number)
except:
    print(sum)