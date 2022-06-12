import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# x = np.arange(0.5, 10.5, 0.1)
# plt.plot(x, np.log(2*x), label='f(x) = log(2*x)',color='red',linestyle=':')
# plt.plot(x, -4*x+2, label='f(x) = -4*x+2',color='green',linestyle='--')
# plt.plot(x, 2*np.cos(x), label='f(x) = 2*np.cos(x)',color='blue',linestyle='-.')
#
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.legend()
# plt.title('Wykresy trzech funkcji na jednym wykresie')
# plt.savefig('ZAD1.png')
# plt.show()

# ZADANIE2

# miesiace = ['styczeń', 'luty', 'marzec', 'kwiecień', 'maj', 'czerwiec', 'lipiec', 'sierpień', 'wrzesień', 'październik',
#             'listopad', 'grudzień']
#
# df = pd.read_excel('ceny41.xlsx')
# print(df)
# a = df.groupby('Rodzaje towarów i usług').mean('Wartosc')
# print(a)
# pro = df['Rodzaje towarów i usług'].unique()
# for x in pro:
#     b = df[df['Rodzaje towarów i usług'] == x].groupby(["Miesiące"]).sum("Wartosc")
#     b = b.reindex(miesiace)
#     plt.plot(b["Wartosc"])
#
# x = df['Miesiące']
# y = df['Wartosc']
# # plt.plot(x,y)
# plt.xticks(rotation=90)
# plt.tight_layout()
# plt.legend(pro)
# plt.savefig("zad2.jpg")
# plt.show()

#ZADANIE 3

dane = pd.read_csv("cechy41.csv", sep=";", decimal=",")
cecha1 = dane["Cecha1"]
cecha2 = dane["Cecha2"]
cat = [0, 50, 100, 150, 200]
p1 = pd.cut(cecha1, bins=cat)
koszyk1 = pd.value_counts(p1, sort=False)
p2 = pd.cut(cecha2, cat)
koszyk2 = pd.value_counts(p2, sort=False)
x = np.arange(4)

print(x)
plt.subplot(1, 2, 1)
plt.barh(x, koszyk1, color='red')
plt.xlabel("Cecha1",color='red')
plt.xticks(np.arange(0,240,50))
plt.subplot(1, 2, 2)
plt.barh(x,koszyk2,color='green')
plt.xlabel("Cecha2", color='green')
plt.xticks(np.arange(0,240,50))
plt.show()