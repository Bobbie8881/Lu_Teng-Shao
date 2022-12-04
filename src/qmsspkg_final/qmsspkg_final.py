
def get_best_teams(Stats):
    """
    Get the MLB teams that have the most players rank in the top of given stats category.
    ----------
    Stats : stats
      The stats that we want to look for.
    Returns
    -------
    list
      The names of the team that has the most players ranked in the given category.
    Examples
    --------
    >>> from qmsspkg_final import qmsspkg_final
    >>> Stats = 'Batting_Average'
    >>> qmsspkg_final.get_best_teams(Stats):
    ['Guardians']
    >>> Stats = 'Runs_Scored'
    >>> qmsspkg_final.get_best_teams(Stats):
    ['Astros']
    """

    import pandas as pd

    import os
    from dotenv import load_dotenv
    load_dotenv() 
    my_api_key = os.getenv('PRIVATE_API_KEY')

    import requests

    response = requests.get(
        'http://api.sportradar.us/mlb/trial/v7/en/seasons/2022/REG/leaders/statistics.json?',
        params={'api_key':my_api_key},
    )
    json_response = response.json()
    
    Teams = ['Braves', 'Marlins', 'Mets', 'Phillies', 'Nationals', 'Cubs', 'Reds', 'Brewers', 'Pirates', 'Cardinals',\
         'Diamondbacks', 'Rockies', 'Dodgers', 'Padres', 'Giants', 'Orioles', 'Red Sox', 'Yankees', 'Rays', 'Blue Jays', \
         'White Sox', 'Guardians', 'Tigers', 'Royals', 'Twins', 'Astros', 'Angels', 'Athletics', 'Mariners', 'Rangers']
    df = pd.DataFrame(index = Teams)
    BA_dic = {}
    for i in json_response['leagues'][0]['hitting']['batting_average']['players']:
        try:
            if i['team']['name'] in BA_dic.keys():
                BA_dic[i['team']['name']] += 1
            else:
                BA_dic[i['team']['name']] = 1
        except:
            pass
    df["Batting_Average"] = pd.Series(BA_dic)
    df = df.fillna(0)
    
    RS_dic = {}
    for i in json_response['leagues'][0]['hitting']['runs_scored']['players']:
        try:
            if i['team']['name'] in RS_dic.keys():
                RS_dic[i['team']['name']] += 1
            else:
                RS_dic[i['team']['name']] = 1
        except:
            pass
    df["Runs_Scored"] = pd.Series(RS_dic)
    df = df.fillna(0)
    
    Do_dic = {}
    for i in json_response['leagues'][0]['hitting']['doubles']['players']:
        try:
            if i['team']['name'] in Do_dic.keys():
                Do_dic[i['team']['name']] += 1
            else:
                Do_dic[i['team']['name']] = 1
        except:
            pass
    df["Doubles"] = pd.Series(Do_dic)
    df = df.fillna(0)
    
    Tr_dic = {}
    for i in json_response['leagues'][0]['hitting']['triples']['players']:
        try:
            if i['team']['name'] in Tr_dic.keys():
                Tr_dic[i['team']['name']] += 1
            else:
                Tr_dic[i['team']['name']] = 1
        except:
            pass
    df["Triples"] = pd.Series(Tr_dic)
    df = df.fillna(0)
    
    HR_dic = {}
    for i in json_response['leagues'][0]['hitting']['home_runs']['players']:
        try:
            if i['team']['name'] in HR_dic.keys():
                HR_dic[i['team']['name']] += 1
            else:
                HR_dic[i['team']['name']] = 1
        except:
            pass
    df["Home_Runs"] = pd.Series(HR_dic)
    df = df.fillna(0)
    
    RBI_dic = {}
    for i in json_response['leagues'][0]['hitting']['runs_batted_in']['players']:
        try:
            if i['team']['name'] in RBI_dic.keys():
                RBI_dic[i['team']['name']] += 1
            else:
                RBI_dic[i['team']['name']] = 1
        except:
            pass
    df["Runs_Batted_In"] = pd.Series(RBI_dic)
    df = df.fillna(0)
    
    Hit_dic = {}
    for i in json_response['leagues'][0]['hitting']['hits']['players']:
        try:
            if i['team']['name'] in Hit_dic.keys():
                Hit_dic[i['team']['name']] += 1
            else:
                Hit_dic[i['team']['name']] = 1
        except:
            pass
    df["Hits"] = pd.Series(Hit_dic)
    df = df.fillna(0)
    
    SB_dic = {}
    for i in json_response['leagues'][0]['hitting']['stolen_bases']['players']:
        try:
            if i['team']['name'] in SB_dic.keys():
                SB_dic[i['team']['name']] += 1
            else:
                SB_dic[i['team']['name']] = 1
        except:
            pass
    df["Stolen_Bases"] = pd.Series(SB_dic)
    df = df.fillna(0)
    
    ERA_dic = {}
    for i in json_response['leagues'][0]['pitching']['earned_run_average']['players']:
        try:
            if i['team']['name'] in ERA_dic.keys():
                ERA_dic[i['team']['name']] += 1
            else:
                ERA_dic[i['team']['name']] = 1
        except:
            pass
    df["ERA"] = pd.Series(ERA_dic)
    df = df.fillna(0)
    
    WHIP_dic = {}
    for i in json_response['leagues'][0]['pitching']['whip']['players']:
        try:
            if i['team']['name'] in WHIP_dic.keys():
                WHIP_dic[i['team']['name']] += 1
            else:
                WHIP_dic[i['team']['name']] = 1
        except:
            pass
    df["Whip"] = pd.Series(WHIP_dic)
    df = df.fillna(0)
    
    GW_dic = {}
    for i in json_response['leagues'][0]['pitching']['games_won']['players']:
        try:
            if i['team']['name'] in GW_dic.keys():
                GW_dic[i['team']['name']] += 1
            else:
                GW_dic[i['team']['name']] = 1
        except:
            pass
    df["Games_Won"] = pd.Series(GW_dic)
    df = df.fillna(0)
    
    SO_dic = {}
    for i in json_response['leagues'][0]['pitching']['strikeouts']['players']:
        try:
            if i['team']['name'] in SO_dic.keys():
                SO_dic[i['team']['name']] += 1
            else:
                SO_dic[i['team']['name']] = 1
        except:
            pass
    df["Strikeouts"] = pd.Series(SO_dic)
    df = df.fillna(0)
    
    GS_dic = {}
    for i in json_response['leagues'][0]['pitching']['games_saved']['players']:
        try:
            if i['team']['name'] in GS_dic.keys():
                GS_dic[i['team']['name']] += 1
            else:
                GS_dic[i['team']['name']] = 1
        except:
            pass
    df["Games_Saved"] = pd.Series(GS_dic)
    df = df.fillna(0)
    
    top = df[Stats].sort_values(ascending = False)[0]
    return df[df[Stats] == top].index.tolist()

