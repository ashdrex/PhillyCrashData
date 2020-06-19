# keep crash_year, hour_of_day, latitude, longitude

import sys
import os
import pandas as pd

# delete all columns except 6, 10, 29, 30


def simplify_csv(csv_read_path, csv_write_path):
    data_csv = pd.read_csv(f'{csv_read_path}')
    data_csv.drop(data_csv.columns.difference(['crash_year', 'hour_of_day', 'latitude', 'longitude']), 1, inplace=True)
    data_csv.to_csv(f'{csv_write_path}', index=False)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Error: Not enough arguments.')
        sys.exit(1)

    _, csv_read_path, csv_write_path = sys.argv[:3]
    if not os.path.exists(csv_read_path):
        print('Error: {0} does not exist.'.format(csv_read_path))
        sys.exit(1)

    simplify_csv(csv_read_path, csv_write_path)
