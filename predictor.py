### Custom definitions and classes if any ###
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("all_matches.csv", low_memory=False)

remove_columns = ['season', 'start_date', 'striker', 'non_striker', 'bowler', 'byes', 'legbyes', 'noballs',
                  'penalty', 'wicket_type', 'player_dismissed', 'other_wicket_type', 'other_player_dismissed', 'wides']
df.drop(labels = remove_columns, axis = 1, inplace = True)
df = df.fillna(0)
df['score'] = (df["runs_off_bat"] + df["extras"]).astype("int")
df = df[["match_id", "venue", "innings", "batting_team", "bowling_team", "ball", "score"]]
df = df[df.ball <= 6.0]

current_teams = ['Kolkata Knight Riders', 'Chennai Super Kings', 'Rajasthan Royals', 'Mumbai Indians', 
                 'Kings XI Punjab', 'Royal Challengers Bangalore', 'Delhi Daredevils', 'Sunrisers Hyderabad']
current_venues = ['M Chinnaswamy Stadium', 'Eden Gardens', 'MA Chidambaram Stadium', 'Wankhede Stadium', 
                  'Arun Jaitley Stadium']
df = df[(df['batting_team'].isin(current_teams)) &(df['bowling_team'].isin(current_teams))]
df = df[(df['venue'].isin(current_venues))]

df['score_6'] = df.groupby(['match_id', 'innings'])['score'].transform('sum')

dummies = pd.get_dummies(df.venue)
merged = pd.concat([df,dummies],axis='columns')
df = merged.drop(['venue'],axis='columns')

dummies2 = pd.get_dummies(df.batting_team)
merged2 = pd.concat([df,dummies2],axis='columns')
df = merged2.drop(['batting_team'],axis='columns')

dummies3 = pd.get_dummies(df.bowling_team)
merged3 = pd.concat([df,dummies3],axis='columns')
df = merged3.drop(['bowling_team'],axis='columns')

df = df.drop(['match_id'],axis='columns')

X = df.drop('score_6',axis=1)
y = df['score_6']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.9, random_state=0)
regressor = RandomForestRegressor(n_estimators = 1000, random_state = 42)
regressor.fit(X_train, y_train)

def predictRuns(testInput):
    prediction = regressor.predict(X_test)
    return prediction
	

