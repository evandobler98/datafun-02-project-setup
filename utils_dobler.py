''' FINAL Iteration

Module: Dobler Data: Delivering Baseball Insights

This module provides a simple, reusable foundation for my analytics projects. 
'''

import statistics


has_international_clients: bool = True
multiple_languages_offered: bool = True
years_in_operation: int = 7
players_per_session: int = 4
skills_offered: list = ["Strength", "Agility", "Flexibility", "Speed"]
highest_grossing_locations : list = ["Kansas City", "Dallas", "Miami", "Phoenix"]
client_satisfaction_scores: list = [4.2, 5.0, 4.8, 4.9, 4.9]
top_bat_speeds_before_training: list = [59.8, 62.4, 61.8, 63.4, 64.1]
top_bat_speeds_after_training: list = [61.2, 63.6, 62.9, 65.1, 65.7]
top_bat_speeds_change: list = [1.4, 1.2, 1.1, 1.7, 1.6]


#Calculate basic stats using built-in functions min(), max(), and statistics module functions mean() and stdev()
min_score: float = min(client_satisfaction_scores)
max_score: float = max(client_satisfaction_scores)
mean_score: float = statistics.mean(client_satisfaction_scores)
stdev_score: float = statistics.stdev(client_satisfaction_scores)

min_bat_speed_before: float = min(top_bat_speeds_before_training)
max_bat_speed_before: float = max(top_bat_speeds_before_training)
mean_bat_speed_before: float = statistics.mean(top_bat_speeds_before_training)
stdev_bat_speed_before: float = statistics.stdev(top_bat_speeds_before_training)

min_bat_speed_after: float = min(top_bat_speeds_after_training)
max_bat_speed_after: float = max(top_bat_speeds_after_training)
mean_bat_speed_after: float = statistics.mean(top_bat_speeds_after_training)
stdev_bat_speed_after: float = statistics.stdev(top_bat_speeds_after_training)

mean_bat_speed_change: float = statistics.mean(top_bat_speeds_change)
stdev_bat_speed_change: float = statistics.stdev(top_bat_speeds_change)


# Declare a global variable named byline.

byline: str = f"""
---------------------------------------------------
Dobler Data: Delivering Baseball Insights
---------------------------------------------------
Has International Clients:                  {has_international_clients}
Years in Operation:                         {years_in_operation}
Highest Grossing Locations:                 {highest_grossing_locations}
Players Per Session:                        {players_per_session}
Has Multiple Languages Offered:             {multiple_languages_offered}
Skills Offered:                             {skills_offered}
Client Satisfaction Scores:                 {client_satisfaction_scores}
Minimum Satisfaction Score:                 {min_score}
Maximum Satisfaction Score:                 {max_score}
Average Satisfaction Score:                 {mean_score:.2f}
Standard Deviation of Satisfaction Scores:  {stdev_score:.2f}

Top Bat Speeds Before Training:                  {top_bat_speeds_before_training}
Minimum Bat Speed Before Training:               {min_bat_speed_before}
Maximum Bat Speed Before Training:               {max_bat_speed_before}
Average Bat Speed Before Training:               {mean_bat_speed_before:.2f}
Standard Deviation of Bat Speed Before Training: {stdev_bat_speed_before:.2f}

Top Bat Speeds After Training:                    {top_bat_speeds_after_training}
Minimum Bat Speeds After Training:                {min_bat_speed_after}
Maximum Bat Speeds After Training:                {max_bat_speed_after}
Average Bat Speeds After Training:                {mean_bat_speed_after:.2f}
Standard Deviation of Bat Speeds After Training:  {stdev_bat_speed_after:.2f}

Top Bat Speeds Change:                   {top_bat_speeds_change}
Mean Bat Speed Change:                   {mean_bat_speed_change:.2f}
Standard Deviation of Bat Speed Change:  {stdev_bat_speed_change:.2f}
"""


def get_byline() -> str:
    '''Return a byline for my analytics projects.'''
    return byline 

def main() -> None:
    '''Print the byline to the console when this function is called.'''
    print(get_byline())

if __name__ == '__main__':
    main()