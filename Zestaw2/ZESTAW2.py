import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#ZESTAW 2

# x = np.array(['A', 'B', 'C', 'D', 'E'])
# y1 = np.array([35, 48, 14, 43, 42])
# y2 = np.array([-30, -33, -38, -35, -31])
#
# plt.subplot(1, 2, 1)
# plt.barh(x,y1,color=['#AFDCEC','#FFB7C5','#F88158','#ACACAC','#8B008B'])
# plt.title('Wykres Lewy')
# plt.xticks(np.arange(0,41,10))
# plt.subplot(1, 2, 2)
# plt.barh(x,y2,color=['#DA70D6','#17BECF','#17BECF','#8C564B','#BCBD22'])
# plt.title('Wykres Prawy')
# plt.xticks(np.arange(0,-31,-10))
# plt.savefig('Zad1.png')
# plt.show()

# zad2

# xlsx = pd.read_excel('ceny2.xlsx')
# df = pd.DataFrame(xlsx)
# produkty = df.groupby('Rodzaje towarów').agg({"Wartość": ["mean"]})
# print(produkty)
#
# a = df.loc[df["Rodzaje towarów"] == "ryż - za 1kg"]
# b = df.loc[df["Rodzaje towarów"] == "mąka pszenna - za 1kg"]
# cenaa=a['Wartość']
# cenab=b['Wartość']
# roka=a['Rok']
# rokb=b['Rok']
# plt.plot(roka,cenaa,label='ryż - za 1kg')
# plt.plot(rokb,cenab,label='mąka pszenna - za 1kg')
# plt.xlabel('Lata')
# plt.ylabel('Wartości w zł')
# plt.grid()
# plt.legend()
# plt.figtext(0.02, 0.02, '166324', size=12, color='pink')
# plt.savefig('Zad2.jpg')
# plt.show()


# zadanie 3

# csv = pd.read_csv('nieruchomosci2.csv', sep=';', header=None)
# df = pd.DataFrame(csv)
#
# print(df)
#
# df.loc[3,:] = df.loc[3,:].str.replace(' ','').astype(int)
# df = df.transpose()
#
# df.columns = ['rynek','metraż','rok','ilosc']
# print(df)
#
# grupa = df.where(df['rynek']=='rynek wtórny')
# grupa = grupa.groupby('metraż').agg({'ilosc':'sum'})
#
# grupa.plot(kind = 'pie',subplots = True, autopct='%.2f %%', fontsize = 10,figsize=(8,8))
# plt.legend(title='metraż',loc=3)
# plt.title('wykres przedstawiający stosunek ilości mieszkań poszczególnych metraży sprzedanych w 2018 roku')
#
# plt.show()
#
# grupa= df.where(df['rynek']=='rynek pierwotny')
#
# grupa = grupa.groupby('metraż').agg({'ilosc':'sum'})
# grupa.plot(kind='pie',subplots=True,autopct='%.2f %%',fontsize=10,figsize=(8,8))
# plt.legend(title='metraz',loc=3)
# plt.title('wykres przedstawiający stosunek ilości mieszkań poszczególnych metraży sprzedanych w 2018 roku')
# plt.show()
