import random
import pandas as pd
import datetime as dt
import time

prompt = ''

print('How many datapoints would you like to add?')

prompt = int(input())

num = 0
while num < prompt:

    time.sleep(1)

    df = pd.read_csv('data.csv')

    new_data = [dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), random.randint(0, 100)]

    df.loc[len(df)] = new_data

    df.to_csv('data.csv', index=False)

    print('Datapoint added')

    num+=1
