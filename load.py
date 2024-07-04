import pandas as pd 

def load_csv_to_postgres(csv_file_path, table_name, engine, schema):
    '''
    Load data from a csv file to pandas dataframe and then to a postgres DB table

    Parameters:
    - csv_file_path (str): Path to scv file
    - table_name (str): a postgres db table
    - engine (sqlalchemy.engine): an SQL alchemy engine object
    - schema (str): a postgres DB schema
    '''
    # Read csv to pandas and to sql
    df = pd.read_csv(csv_file_path)
    df.to_sql(table_name, con=engine, if_exists='replace', index=False, schema=schema)

    print(f'{len(df)} rows loaded to staging successfully')