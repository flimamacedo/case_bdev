# pip3 install pandas
import pandas as pd
import os
import sys

# CONSTANTS
approvers_file = 'approvers.csv'
owners_file = 'owner.txt'

# Loading the approvers
df = pd.read_csv(approvers_file, delimiter=',')
approvers_list = df.columns.tolist()

rootdir = sys.argv[1]


def check_dirs(rootdir, approvers_list):
    permissions = []
    for dirpath, subdirs, files in os.walk(rootdir):
        if owners_file in files:
            with open(os.path.join(dirpath, owners_file), 'r') as owners:
                owner = owners.read()
                full_path = os.path.join(dirpath)
                if owner in approvers_list:
                    permissions.append({"folder": full_path, "owner": owner, "permission": True})  
        else:
            owner = "None"
            full_path = os.path.join(dirpath)
            permissions.append({"folder": full_path, "owner": owner, "permission": False})          
    print(permissions)


check_dirs(rootdir, approvers_list)

