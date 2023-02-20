from gendiff.parsers import parser
from gendiff.compare_data import compare_data
from gendiff.formatters.stylish import get_stylish_format


def generate_diff(first_file, second_file, format='stylish'):
    print(first_file)
    first_file_data = parser(first_file)
    second_file_data = parser(second_file)
    compared_data = compare_data(first_file_data, second_file_data)
    formatted_data = get_stylish_format(compared_data)
    return formatted_data
