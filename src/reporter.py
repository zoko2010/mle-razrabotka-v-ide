class DataFrameReporter:
    #title = None
    def __init__(self, float_format='0.05f', percent_format='0.02%', include_all=False):
        self.float_format = float_format
        self.percent_format = percent_format
        self.include_all = include_all

    def show_report(self, df, title=None):
        if title is not None:
            print(title)
        count_columns = df.shape[1]
        count_row = df.shape[0]
        count_duplicated = df.duplicated().sum()
        if count_row > 0:
            d_duplicated = count_duplicated / count_row
        else:
            d_duplicated = 0
        print(f'Количество столбцов: {count_columns}')
        print(f'Количество строк: {count_row}')
        print(f'Количество дубликатов: {count_duplicated}')
        print(f'Доля дубликатов: {format(d_duplicated, self.percent_format)}')
                  
reporter = DataFrameReporter()

import pandas as pd

data = pd.read_csv('data/payments.csv')

# вызовите метод show_report для reporter, передав в него датафрейм
reporter.show_report(data)