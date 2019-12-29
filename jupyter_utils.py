import sys 

def maximize():
    try:
        from IPython.core.display import display, HTML
        display(HTML("<style>.container { width:100% !important; }</style>"))
    except Exception as e:
        print(f'Error while maximizing the notebook cells: {str(e)}')

def display_all_colums(pd):
    if pd is None:
        print('Please import pandas before calling this function.')
        return

    pd.set_option('display.expand_frame_repr', True)
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)

def cfg_sns(sns):
    sns.set(rc = {
            'figure.figsize': (11.7,8.27),
            'font.size': 20,
            'axes.titlesize': 20,
            'axes.labelsize': 20
        }, style='white')
    sns.set(font_scale=1.5)

