import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

jobs = pd.read_csv("NYC_Jobs.csv")

# desired_width = 320
# pd.set_option('display.width', desired_width)
# pd.set_option("display.max_columns", 28)


def print_10_rows(dataset):
    pd.set_option('display.width', 200)
    pd.set_option("display.max_columns", 28)
    print(dataset.head(10))


def print_agency_col(dataset):
    df = pd.DataFrame(dataset)
    selection = df.loc[:, "Agency"]
    print(selection.head(10))


def print_3_cols(dataset):
    df = pd.DataFrame(dataset)
    pd.set_option("display.max_columns", 3)
    selection = df.loc[:, ["Agency", "Business Title", "Work Location 1"]]
    print(selection.head(10))


def agency_names(dataset):
    df = pd.DataFrame(dataset)
    agency_counts = df["Agency"].value_counts()
    agency_counts.plot(kind="bar")
    plt.show()
    print(agency_counts)


def zal(dataset):
    df = pd.DataFrame(dataset)
    df['median'] = df.groupby('Salary Range From')['Salary Range To'].transform(np.mean)

    gb = df.groupby('Agency')
    data1 = pd.DataFrame([df.loc[gb.groups[n], 'mean'].values for n in gb.groups], index=gb.groups.keys())
    data1 = data1.mean(axis=1)
    data1.plot(kind='bar')
    plt.show()

    gb = df.groupby('Work Location')
    data1 = pd.DataFrame([df.loc[gb.groups[n], 'mean'].values for n in gb.groups], index=gb.groups.keys())
    data1 = data1.mean(axis=1)
    data1.head(50).plot(kind='bar')
    plt.show()


def start():
    while True:
        keypress = int(input("choice? "))
        if keypress == 1:
            print(jobs)
        elif keypress == 2:
            print_10_rows(jobs)
        elif keypress == 3:
            print_agency_col(jobs)
        elif keypress == 4:
            print_3_cols(jobs)
        elif keypress == 5:
            agency_names(jobs)
        elif keypress == 6:
            zal(jobs)
        elif keypress == 0:
            return False


start()
