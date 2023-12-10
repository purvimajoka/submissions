import pandas as pd
import numpy as np

df=pd.read_csv('dataset-1.csv')

#Ans 1

df1=df.copy()
def generate_car_matrix(df1):
    df1=df.pivot(index='id_1',columns='id_2',values='car')
    df1.values[np.diag_indices_from(df1)]=0
    return df1

df_1=generate_car_matrix(df1)

#Ans 2

df2=df.copy()
def get_type_count(row):
    if row['car']<=15:
        return 'low'
    elif row['car']>15 and row['car']<=25:
        return 'medium'
    else:
        return 'high'
    
df2['car_type'] = df2.apply(get_type_count,axis=1)

#Ans 3 :-

df3=df.copy()
def get_bus_indexes(df):
    return list(df[df['bus']> (df['bus'].mean())*2].index)

get_bus_indexes(df3)


#Ans 4 :-

df4=df.copy()
def filter_routes(df):
    return sorted(list(df[df['truck'] > 7].route))

filter_routes(df4)

#Ans 5 :-

df5=df_1.copy()
def multiply_matrix(df5):
    res_df1=np.round(np.where(df5>20,df5*0.75,df5*1.25),1)
    res_df1 = pd.DataFrame(res_df1, columns=df5.columns)
    return res_df1

multiply_matrix(df5)

#Ans 6 :-
dataset_2=pd.read_csv('dataset-2.csv')

def check_completeness(df):
    # Assuming your DataFrame has columns like 'id', 'id_2', 'startday', 'starttime', 'endday', 'endtime'
    
    # Convert 'startday' and 'endday' to numerical representation (Monday is 1, Sunday is 7)
    days_mapping = {"Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6, "Sunday": 7}
    df['startDay'] = df['startDay'].map(days_mapping)
    df['endDay'] = df['endDay'].map(days_mapping)

    # Convert time strings to datetime objects
    df['start_datetime'] = pd.to_datetime(df['startTime'], format='%H:%M:%S')
    df['end_datetime'] = pd.to_datetime(df['endTime'], format='%H:%M:%S')

    grouped_data = df.groupby(['id', 'id_2']).agg({
        'startDay': 'unique',
        'endDay': 'unique',
        'start_datetime': 'min',
        'end_datetime': 'max'
    }).reset_index()

    for index, row in grouped_data.iterrows():
        start_days = set(row['startDay'])
        end_days = set(row['endDay'])

        # Check time span
        full_24_hour_span = (
            row['start_datetime'] == pd.Timestamp("00:00:00") and
            row['end_datetime'] == pd.Timestamp("23:59:59")
        )

        # Check day span
        full_week_span = start_days == end_days == set(range(1, 8))

        if full_24_hour_span and full_week_span:
            print(True)
        else:
            print(False)

# Example usage with a DataFrame named 'df'
# Replace this with your actual DataFrame


check_completeness(dataset_2)
