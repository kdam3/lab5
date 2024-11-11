#!/usr/bin/env python3
# Author ID: kdam3

# Function to read file content as a single string
def read_file_string(file_name):
    with open(file_name, 'r') as f:
        return f.read()

# Function to read file content as a list of lines
def read_file_list(file_name):
    with open(file_name, 'r') as f:
        return [line.strip() for line in f.readlines()]

# Function to append a string to a file
def append_file_string(file_name, string_of_lines):
    with open(file_name, 'a') as f:
        f.write(string_of_lines)

# Function to write a list of lines to a file
def write_file_list(file_name, list_of_lines):
    with open(file_name, 'w') as f:
        for line in list_of_lines:
            f.write(line + '\n')

# Function to copy file content to another file with line numbers
def copy_file_add_line_numbers(file_name_read, file_name_write):
    with open(file_name_read, 'r') as f_read, open(file_name_write, 'w') as f_write:
        line_number = 1
        for line in f_read:
            f_write.write(f"{line_number}:{line}")
            line_number += 1

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    
    append_file_string(file1, string1)
    print("Contents of seneca1.txt after append:")
    print(read_file_string(file1))
    
    write_file_list(file2, list1)
    print("Contents of seneca2.txt after write:")
    print(read_file_string(file2))
    
    copy_file_add_line_numbers(file2, file3)
    print("Contents of seneca3.txt after copy with line numbers:")
    print(read_file_string(file3))
