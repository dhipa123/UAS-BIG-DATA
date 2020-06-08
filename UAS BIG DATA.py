import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# input array menggunakan numpy
x = np.array([394, 396, 407, 415, 420, 443, 455, 465, 482])
y = np.array([394, 396, 407, 415, 420, 443, 455, 465, 482])


# convert ke panda dataframe
data = {'x': x, 'y': y}
df = pd.DataFrame(data)

# plot menggunakan barplot
sns.barplot(x='x', y='y', data=df)

plt.ylabel('Total_Kasus ')
plt.xlabel('Di Wilayah BALI (394 = 24 Maret) > (482 = 1 Juni)')
plt.title('Total Kasus Covid-19 24 Maret sampai 1 Juni Tahun 2020')
plt.show()

