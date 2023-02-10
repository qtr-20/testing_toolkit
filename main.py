# This is a sample Python script.
import fnmatch
import glob
import os
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from os import path
import pandas as pd


def read_spreadsheet(file_dir):
    import pandas as pd
    # import os

    print('Reading downloaded spreadsheet from given directory..')
    output = pd.read_excel(file_dir)
    # out_file_dir = os.path.join(os.getcwd(), file_dir[:-4]+"csv")
    # output.to_csv(out_file_dir)
    return output


def newton_csv_compile(directory=os.getcwd(), out_directory=os.getcwd()):

    directory = os.path.join(directory, "./samples")  # for debugging purposes

    file_list = os.listdir(directory)
    csv_list = fnmatch.filter(file_list, "*.csv")


    out = csv_list
    print(out)
    return None


def main():
    newton_csv_compile()

    # dir = r'./MT148 - Test Summary Sheet.xlsx'
    # rawd = read_spreadsheet(file_dir=dir)


    """
    rawd = rawd[rawd['File Name'].notna()]
    data = rawd[rawd['Max Load [lbs]'].notna()]
    # data = data[data['Valid Test'] != "to retest"]

    if path.exists("raw_data.csv") or path.exists("data.csv"):
        inp = input('raw_data.csv or data.csv exists, overwrite both (y/n)? ')
        if inp.lower() == 'n':
            print('Script stopped no permission to overwrite.')
            exit()
        else:
            rawd.to_csv("raw_data.csv")
            data.to_csv("data.csv")
            print("data files processed")
    """

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
