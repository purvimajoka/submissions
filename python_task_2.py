import pandas as pd
import numpy as np
import networkx as nx

df=pd.read_csv('dataset-3.csv')

#Ans 1

def calculate_distance_matrix(df1):
    G = nx.DiGraph()
    
    for _, row in df1.iterrows():
        G.add_edge(row['id_start'], row['id_end'], weight=row['distance'])
        G.add_edge(row['id_end'], row['id_start'], weight=row['distance'])  # Bidirectional
    
    distance_matrix = nx.floyd_warshall_numpy(G, weight='weight')
    
    distance_df = pd.DataFrame(distance_matrix, index=G.nodes, columns=G.nodes)

    return distance_df

res_df=calculate_distance_matrix(df)
res_df

#Ans - 2

def unroll_distance_matrix(distance_df):

    unrolled_data = []

    for i in range(len(distance_df)):
        for j in range(i + 1, len(distance_df)):
            id_start = distance_df.index[i]
            id_end = distance_df.columns[j]
            distance = distance_df.iloc[i, j]

 
            unrolled_data.append({'id_start': id_start, 'id_end': id_end, 'distance': distance})

    unrolled_df = pd.DataFrame(unrolled_data)

    return unrolled_df


resulting_unrolled_df = unroll_distance_matrix(res_df)
print(resulting_unrolled_df)


#Ans-3

#Ans -4 

def calculate_toll_rate(resulting_unrolled_df):
    # Define rate coefficients for each vehicle type
    rate_coefficients = {'moto': 0.8, 'car': 1.2, 'rv': 1.5, 'bus': 2.2, 'truck': 3.6}

    # Create new columns for each vehicle type with their respective toll rates
    for vehicle_type, rate_coefficient in rate_coefficients.items():
        distance_df[vehicle_type] = distance_df['distance'] * rate_coefficient

    return distance_df

# Example usage:
# Assuming distance_df is the DataFrame created in Question 2
result_df = calculate_toll_rate(resulting_unrolled_df)
print(result_df)

#Ans-5



