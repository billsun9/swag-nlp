import pandas as pd

COLS = ['id','vid-id','fold-id','startphrase','sent1','sent2','gold-source','ending0','ending1','ending2','ending3','label']

train = pd.read_csv('swag-train.csv', skiprows=[0], names=COLS)
dev = pd.read_csv('swag-val.csv', skiprows=[0], names=COLS)
# %%
