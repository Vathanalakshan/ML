import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns;

sns.set()

data = pd.read_csv('challenger.csv')
print(data.shape)

data = data.drop_duplicates()

print(data.shape)
kill = ["kills_bottom_duo_support_team_2", "kills_bottom_duo_support_team_1", "kills_bottom_duo_carry_team_2",
        "kills_bottom_duo_carry_team_1", "kills_top_team_1", "kills_top_team_2", "kills_middle_team_1",
        "kills_middle_team_2", "kills_jungle_team_1", "kills_jungle_team_2"]
k = []
for i, row in data.iterrows():
    for j in kill:
        if (row[j] > 40):
            k.append(i)
            break

data = data.drop(k, axis=0)
print(data.shape)
gold_earned1=["gold_earned_top_team_1","gold_earned_jungle_team_1","gold_earned_middle_team_1","gold_earned_bottom_duo_carry_team_1","gold_earned_bottom_duo_support_team_1"]
gold_earned2=["gold_earned_top_team_2","gold_earned_jungle_team_2","gold_earned_middle_team_2","gold_earned_bottom_duo_carry_team_2","gold_earned_bottom_duo_support_team_2"]


input = data.drop(data.iloc[:, : 50]

,axis='columns')
target = data["win"]

i_train,i_test,t_train,t_test=train_test_split(input,target,test_size=0.2)

DTree= DecisionTreeClassifier()
DTree.fit(i_train,t_train)
print(DTree.score(i_test,t_test))


sns.heatmap(data.corr(), annot=True)
plt.show()
