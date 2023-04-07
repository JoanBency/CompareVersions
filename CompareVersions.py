# from msvcrt import getch


def compare_versions(version1, version2):
    # All elements or numbers in the version string are separated as list items setting the delimiter as '.'
    elements_in_version1 = version1.split('.')
    elements_in_version2 = version2.split('.')
    # Every element in the list are converted into integer
    numbers_in_version1 = list(map(int, elements_in_version1))
    numbers_in_version2 = list(map(int, elements_in_version2))
    # Length of each list is calculated
    length_of_version1 = len(numbers_in_version1)
    length_of_version2 = len(numbers_in_version2)
    # Smallest in length among both the lists
    smallest_length = min(length_of_version1, length_of_version2)
    # Only the first few numbers in the list are gonna be compared,
    # but a zero is appended to the end of the smaller list for checking
    # Eg: to check version 1.3 and 1.3.4, a zero is added to the end of first one
    # and the lists would be [1, 3, 0] and [1, 3, 4]
    if length_of_version1 > length_of_version2:
        numbers_in_version2.append(0)
    elif length_of_version2 > length_of_version1:
        numbers_in_version1.append(0)
    else:
        smallest_length = length_of_version1 - 1
        # when length of both string are the same, no extra element added to the list
    i = 0
    while i <= smallest_length:
        # If the number in list of version 1 are ever greater than version 2
        if numbers_in_version1[i] > numbers_in_version2[i]:
            return 1
        # If the number in list of version 2 are ever greater than version 1
        elif numbers_in_version2[i] > numbers_in_version1[i]:
            return -1
        # If both are equal just check for the next element in the lists
        else:
            i = i + 1
    # This means the numbers were always equal
    return 0


# ------------ Code for the executable to input versions and display the results -------------------


# version_1 = input("Enter the First Version : ")
# version_2 = input("Enter the Second Version : ")
# result = compare_versions(version_1, version_2)
# print(result)
# if result == 1:
#     print("Version1 (" + version_1 + ") is larger than Version2 (" + version_2 + ")")
# elif result == -1:
#     print("Version2 (" + version_2 + ") is larger than Version1 (" + version_1 + ")")
# elif result == 0:
#     print("Version1 (" + version_1 + ") and Version2 (" + version_1 + ") are the same")
# getch()
