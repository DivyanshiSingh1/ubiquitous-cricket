Problem Statement:

Given certain input parameters regarding an innings of a T20 cricket match, predict the total runs scored by the batting team at the end of 6 overs.
Programming Language to be used: only Python 3.8
Maximum size of zip file allowed: 50MB
Maximum permitted execution time: 10secs.

Packages used:
jupyter==1.0.0
numpy==1.19.5
pandas==1.2.4
scikit-learn==0.24.1
scipy==1.6.2
seaborn==0.11.1

Input Data:

The link to the Dataset (Source: cricsheet.org) which contains historic data of T20 matches that have occurred in the past.

Data Description (quoted directly from Cricsheet page: https://cricsheet.org/downloads/):

The CSV File provided follows the "NEW" format.
The "new" format consists of a single row for each delivery in a match (or group of matches).
The first row of each CSV file contains the headers for the file, with each subsequent row providing details on a single delivery. 
The headers in the file are:

match_id
season
start_date
venue
innings
ball
batting_team
bowling_team
striker
non_striker
bowler
runs_off_bat
extras
wides
noballs
byes
legbyes
penalty
wicket_type
player_dismissed
other_wicket_type
Other_player_dismissed

"innings" contains the number of the innings within the match. If a match is one that would normally have 2 innings, such as a T20 or ODI, then any innings 
of more than 2 can be regarded as a super over.

"ball" is a combination of the over and delivery. For example, "0.3" represents the 3rd ball of the 1st over.

If a wicket occurred on a delivery then "wicket_type" will contain the method of dismissal, while "player_dismissed" will indicate who was dismissed.
There is also the, admittedly remote, possibility that a second dismissal can be recorded on the delivery (such as when a player retires on the same 
delivery as another dismissal occurs). In this case "other_wicket_type" will record the reason, while "other_player_dismissed" will show who was dismissed.

Test Case Input:

The following will be provided as input test case data:
venue, innings, batting_team, bowling_team, batsmen who batted during the first 6 overs, bowlers who bowled during the first 6 overs.

Algorithm used: Random Forest Regression

Mean Absolute Error: 9.17 degrees.
Accuracy: 77.06 %.
