import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


logfiles = list(Path('.').glob('**/*.txt'))
df = pd.read_csv("log.txt", sep=" ", header=2)
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

  
# display DataFrame
print(df)
df.to_csv('log.csv')

fig, ax = plt.subplots()
#df.plot(ax=ax, x ='Timestamp(ms)', y='gMain.CR2052.X2.Pin02.Aout', kind = 'scatter')	
#df['rolling'] = df["CarriageEncoder.In"].rolling(5000, min_periods=3000, center=True).mean()
#df.plot(ax=ax, x ='Timestamp(ms)', y='CarriageEncoder.In'df.plot(ax=ax, x ='Timestamp(ms)', y='rolling')	



df['rollingpA'] = df["gTestStand.PCarriageA.Pressure"].rolling(5000, min_periods=3000, center=True).mean()
df.plot(ax=ax, x ='Timestamp(ms)', y='gTestStand.PCarriageA.Pressure')
df['rollingpB'] = df["gTestStand.PCarriageB.Pressure"].rolling(5000, min_periods=3000, center=True).mean()
df.plot(ax=ax, x ='Timestamp(ms)', y='gTestStand.PCarriageB.Pressure')
df.plot(ax=ax, x ='Timestamp(ms)', y='rollingpA')
df.plot(ax=ax, x ='Timestamp(ms)', y='rollingpB')	
plt.show() # plt in place of ax