import pandas as pd

# Functions to get data
def fetch_data(client, query):
    '''
    fetches query results from a clickhouse database and writes to a csv file

    Parameters:
    - client(clickhouse_connect.client)
    - query (A SQL select query)

    Returns: None
    '''
    # Execute the query
    output = client.query(query)
    rows = output.result_rows
    cols = output.column_names

    # Close the Client
    client.close()

    # Write to pandas df and csv file
    df = pd.DataFrame(rows, columns=cols)
    df.to_csv('tripdata.csv', index=False)

    print(f'{len(df)} Rows successsfully extracted')