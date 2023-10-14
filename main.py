import random
import matplotlib.pyplot as plt
import pandas as pd


def kubik(n: int):
    data = []
    while len(data) < n:
        data.append(random.randint(1, 6))
    return data

def countRate(kubData: list):

    kubRate = {}
    for i in kubData:
        if i in kubRate:
            continue
        else:
            kubRate[i] = kubData.count(i)
    for i in range(1, 6):
        if i not in kubRate:
            kubRate[i] = 0
    return kubRate

def sortRate (countedRate: dict):
    sortedRate = {}
    for key in sorted(countedRate.keys()):
        sortedRate[key] = countedRate[key]
    return sortedRate

def createDataframe (sortedDate: dict):
    df = pd.DataFrame(sortedDate, index=[0])
    df = df.T
    df = df.rename(columns={0: "Частота выпадения"})
    df.insert(0, "Количество выпадений", range(1, 1 + len(df)))
    return df

def propabilitySolving(dataframe: pd.DataFrame):
    sumRate = dataframe["Частота выпадения"].sum()
    propability = []
    for i in dataframe["Частота выпадения"]:
        propability.append(i / sumRate)
    dataframe["Вероятность выпадения"] = propability
    return dataframe

print(propabilitySolving(createDataframe(sortRate(countRate(kubik(100))))))
print("====================================================================")
print(propabilitySolving(createDataframe(sortRate(countRate(kubik(1000))))))
print("====================================================================")
print(propabilitySolving(createDataframe(sortRate(countRate(kubik(10000))))))
print("====================================================================")
print(propabilitySolving(createDataframe(sortRate(countRate(kubik(1000000))))))
print("====================================================================")

n1 = 100
diceData1 = kubik(n1)
diceRate1 = countRate(diceData1)
sortedRate1 = sortRate(diceRate1)
dataframe1 = createDataframe(sortedRate1)
proba = propabilitySolving(dataframe1)
a1 = proba["Вероятность выпадения"].plot(kind = 'bar', legend = True, color = "blue")
plt.show()
a1.figure.savefig("Вероятность100.png")

n2 = 1000
diceData2 = kubik(n2)
diceRate2 = countRate(diceData2)
sortedRate2 = sortRate(diceRate2)
dataframe2 = createDataframe(sortedRate2)
proba = propabilitySolving(dataframe2)
a2 = proba["Вероятность выпадения"].plot(kind = 'bar', legend = True, color = "red")
plt.show()
a2.figure.savefig("Вероятность1000.png")

n3 = 10000
diceData3 = kubik(n3)
diceRate3 = countRate(diceData3)
sortedRate3 = sortRate(diceRate3)
dataframe3 = createDataframe(sortedRate3)
proba = propabilitySolving(dataframe3)
a3 = proba["Вероятность выпадения"].plot(kind = 'bar', legend = True, color = "yellow")
plt.show()
a3.figure.savefig("Вероятность10000.png")

n4 = 1000000
diceData4 = kubik(n4)
diceRate4 = countRate(diceData4)
sortedRate4 = sortRate(diceRate4)
dataframe4 = createDataframe(sortedRate4)
proba = propabilitySolving(dataframe4)
a4 = proba["Вероятность выпадения"].plot(kind = 'bar', legend = True, color = "green")
plt.show()
a4.figure.savefig("Вероятность1000000.png")


