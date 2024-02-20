import os

def get_character_classes(choice):
    character_classes = {
        '1': '0123456789',
        '2': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        '3': 'abcdefghijklmnopqrstuvwxyz',
        '4': '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        '5': '0123456789abcdefghijklmnopqrstuvwxyz',
        '6': '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
        '7': 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
    }
    return character_classes.get(choice, None)

def generate_combinations(char_classes, current_combination, size, file):
    if size == 0:
        file.write(current_combination + '\n')
        return
    for char in char_classes:
        generate_combinations(char_classes, current_combination + char, size - 1, file)

def generate_dictionary(filename, char_classes, min_size, max_size):
    with open(filename, 'w') as file:
        for size in range(min_size, max_size + 1):
            generate_combinations(char_classes, '', size, file)

def main():
    filename = input('Please enter the file name: ')
    
    char_classes = None
    while not char_classes:
        choice = input(
            '1) Numbers\n'
            '2) Capital Letters\n'
            '3) Lowercase Letters\n'
            '4) Numbers + Capital Letters\n'
            '5) Numbers + Lowercase Letters\n'
            '6) Numbers + Capital Letters + Lowercase Letters\n'
            '7) Capital Letters + Lowercase Letters\n'
            'Please select the character class by number: '
        )
        char_classes = get_character_classes(choice)
        if not char_classes:
            print("Invalid choice, please try again.")
    
    min_size = int(input("What is the min size of the word? "))
    max_size = int(input("What is the max size of the word? "))
    
    generate_dictionary(filename, char_classes, min_size, max_size)

if __name__ == '__main__':
    main()