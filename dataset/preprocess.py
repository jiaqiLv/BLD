import pandas as pd
from os.path import join,exists
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

def data_visualization(metric_dict):
    fig,axs = plt.subplots(7,10,figsize=(100,70))
    for i,metric in enumerate(metric_dict):
        # x = np.linspace(0,len(metric_dict[metric]))
        x = np.arange(len(metric_dict[metric]))
        print(len(x))
        axs[(int)(i/10),(int)(i%10)].plot(x,metric_dict[metric],'r',label=metric)
        axs[(int)(i/10),(int)(i%10)].set_title(metric)
        axs[(int)(i/10),(int)(i%10)].legend()
    plt.tight_layout()
    plt.savefig('metric.png')

def data_verification(df):
    result = (df['timestamp'] == df['accept_time']) & (df['accept_time'] == df['sink_time'])
    print(result)
    all_equal = result.all()
    print(all_equal)

if __name__ == '__main__':
    data_path = '/code/model/BLD/data/raw/metric.csv'
    df = pd.read_csv(data_path)
    df['timestamp'] = pd.to_datetime(df['timestamp'], format='%Y/%m/%d %H:%M')
    df['timestamp_unix'] = df['timestamp'].apply(lambda x: x.timestamp())

    metric_dict = {}
    metric_dfs = df.groupby('metric')
    # metric independent storage
    for name,metric_df in metric_dfs:
        metric_df = metric_df.sort_values(by='timestamp_unix')
        metric_dict[name] = metric_df['value']
        metric_df.to_csv(join('/code/model/BLD/data/processed',f'{name}.csv'),index=False)
    data_visualization(metric_dict=metric_dict)