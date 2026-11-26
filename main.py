full_name = "ANGELITO LOMBRINO GABASA"

def get_unique_name(name):
    unsorted_letters = []
    for character in name:
        if(character.isalpha() and character not in unsorted_letters):
            unsorted_letters.append(character)
    return unsorted_letters

def insertion_letter(letter):
    sorted_letters = letter.copy()
    for i in range(1, len(sorted_letters)):
        key = sorted_letters[i]
        j = i - 1
        while j >= 0 and sorted_letters[j] > key:
            sorted_letters[j + 1] = sorted_letters[j]
            j -= 1
        sorted_letters[j + 1] = key
    return sorted_letters


unsorted_letters = get_unique_name(full_name)
sorted_letters = insertion_letter(unsorted_letters)

print('\nName:',full_name,' |  Section: BSIT 2B  |  Assessment 3.7')
print()
print("-" *73)
print(' Unsorted: ', unsorted_letters)
print(' Sorted  : ', sorted_letters)
print("-" *73)

