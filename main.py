import pandas as pd
import csv




def print_hi(name):
    print("---------------->")
    df = pd.read_csv("C:\\Users\\Vikash.Sharma\\Documents\\OneDrive_2022-09-28\\OneDrive_2022-09-28\\gapText adjustment - 09272022\\FL2023_Book_277_with_Standards.csv",
                     #header=0,
                     #expand=False,
                     usecols=["florida23_standard"]
                     )
    df["florida23_standard"] = df["florida23_standard"].str.split("=>", n=0, expand=False).str[0].str.split(" ", n=0, expand=False).str[0]
    with open("C:\\Users\\Vikash.Sharma\\Documents\\new_csv.csv", mode='w') as row_list:
        writer = csv.writer(row_list)
        for row in df["florida23_standard"].iteritems():
            writer.writerow(row)


if __name__ == '__main__':
    print_hi('PyCharm')