from msvcrt import getch
def compareVersions(version1, version2):
    # All elements or numbers in the version string are separated as list items setting the delimiter as '.'
    elementsInVersion1 = version1.split('.')
    elementsInVersion2 = version2.split('.')
    # Every element in the list are converted into integer
    numbersInVersion1 = list(map(int, elementsInVersion1))
    numbersInVersion2 = list(map(int, elementsInVersion2))
    # Length of each list is calculated
    lengthOfVersion1 = len(numbersInVersion1)
    lengthOfVersion2 = len(numbersInVersion2)
    # Smallest in length among both the lists
    smallestLength = min(lengthOfVersion1,lengthOfVersion2)
    # Only the first few numbers in the list are gonna be compared, but a zero is appended to the end of the smaller list for checking
    # Eg: to check version 1.3 and 1.3.4, a zero is added to the end of first one and the lists would be [1, 3, 0] and [1, 3, 4]
    if(lengthOfVersion1 > lengthOfVersion2):
        numbersInVersion2.append(0)
    elif(lengthOfVersion2 > lengthOfVersion1):
        numbersInVersion1.append(0)
    else:
        smallestLength = lengthOfVersion1 - 1 # when length of both string are the same, no extra element added to the list
    i = 0
    while(i <= smallestLength):
        # If the number in list of version 1 are ever greater than version 2
        if(numbersInVersion1[i] > numbersInVersion2[i]):
            return 1
        # If the number in list of version 2 are ever greater than version 1
        elif(numbersInVersion2[i] > numbersInVersion1[i]):
            return -1
        # If both are equal just check for the next element in the lists
        else:
            i = i + 1
    # This means the numbers were always equal
    return 0

version1 = input("Enter the First Version : ")
version2 = input("Enter the Second Version : ")
result = compareVersions(version1, version2)
print(result)
if(result == 1):
    print("Version1 (" + version1 + ") is larger than Version2 (" + version2 + ")")
elif(result == -1):
    print("Version2 (" + version2 + ") is larger than Version1 (" + version1 + ")")
elif(result == 0):
    print("Version1 (" + version1 + ") and Version2 (" + version1 + ") are the same")
getch()