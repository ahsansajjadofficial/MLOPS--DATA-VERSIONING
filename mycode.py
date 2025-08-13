import pandas as pd
import os

data =  {'name': ['Alice', 'Bob', 'Charlie'],
         'age': [25, 30, 35],
         'city': ['New York', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)


new_row = {'name': 'David', 'age': 28, 'city': 'San Francisco'}
df.loc[len(df)] = new_row


new_row = {'name': 'AHSAN', 'age': 18, 'city': 'UK'}
df.loc[len(df)] = new_row





data_dir = 'data'
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

df.to_csv(os.path.join(data_dir, 'people.csv'), index=False)
print("Data saved to 'data/people.csv'")
print(df)