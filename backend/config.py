#---- SEASON SETTINGS ----#
START_SEASON = 2014
END_SEASON = 2026
COVID_SEASONS = [2020, 2021]

#---- API KEYS ----#
ODDS_API_KEY = ""
BALLDONTLIE_API_KEY = ""

#---- REFRESH SETTINGS ----#
ODDS_REFRESH_INTERVAL = 4 * 60 * 60     # 4 HOURS
STATS_REFRESH_INTERVAL = 4 * 60 * 60    # 4 HOURS
LIVE_TRACKER_POLL = 30

#---- DATABASE SETTINGS ----#
DB_PATH = "data/sportspicks.db"

#---- SPORTSBOOKS ----#
SUPPORTED_BOOKS = [
    {"name": "FanDuel", "key": "fanduel", "is_primary": True},
    {"name": "DraftKings", "key": "draftkings", "is_primary": False},
    {"name": "BetMGM", "key": "betmgm", "is_primary": False},
    {"name": "Caesars", "key": "caesars", "is_primary": False},]

#---- SUPPORTED BETS ----#
BET_TYPES = ["points", "rebounds", "assists", 
             "steals", "blocks", "threes", 
             "turnovers", "minutes"]

#---- DATA RANGES ----#
SEASON_RANGE = list(range(2014, 2027))

#---- INTERNATIONAL LEAGUE CONFIG ----#
INTERNATIONAL_LEAGUES = {
    "euroleague": {
        "name": "EuroLeague",
        "bbr_path": "/international/euroleague/",
        "strength": 0.92,
        "has_api": True,        # USE API PACKAGE
        "api_code": "E",        # API COMPETITION CODE
        "bet_markets": True,    # AVAILABLE ON US SPORTSBOOKS
    },
    "eurocup": {
        "name": "EuroCup Basketball",
        "bbr_path": "/international/eurocup/",
        "strength": 0.86,
        "has_api": True,        # USE API PACKAGE
        "api_code": "U",        # API COMPETITION CODE
        "bet_markets": False,
    },
    "acb": {
        "name": "Liga ACB",
        "bbr_path": "/international/acb/",
        "strength": 0.88,
        "has_api": False,
        "api_code": None,
        "bet_markets": False,
    },
    "lega": {
        "name": "Lega Basket Serie A",
        "bbr_path": "/international/italy-lega/",
        "strength": 0.83,
        "has_api": False,
        "api_code": None,
        "bet_markets": False,
    },
    "lnb": {
        "name": "LNB Pro A",
        "bbr_path": "/international/france-pro-a/",
        "strength": 0.82,
        "has_api": False,
        "api_code": None,
        "bet_markets": False,
    },
    "bsl": {
        "name": "Turkish BSL",
        "bbr_path": "/international/turkey-super-league/",
        "strength": 0.83,
        "has_api": False,
        "api_code": None,
        "bet_markets": False,
    },
    "gbl": {
        "name": "Greek Basket League",
        "bbr_path": "/international/greece/",
        "strength": 0.80,
        "has_api": False,
        "api_code": None,
        "bet_markets": False,
    },
    "bbl": {
        "name": "German Basketball Bundesliga",
        "bbr_path": "/international/germany/",
        "strength": 0.80,
        "has_api": False,
        "api_code": None,
        "bet_markets": False,
    },
    "nbl": {
        "name": "Australian NBL",
        "bbr_path": "/international/australia/",
        "strength": 0.78,
        "has_api": False,
        "api_code": None,
        "bet_markets": False,
    },
    "aba": {
        "name": "ABA League",
        "bbr_path": "/international/adriatic/",
        "strength": 0.76,
        "has_api": False,
        "api_code": None,
        "bet_markets": False,
    },
    "ipl": {
        "name": "Israeli Premier League",
        "bbr_path": "/international/israel/",
        "strength": 0.75,
        "has_api": False,
        "api_code": None,
        "bet_markets": False,
    },
    "cba": {
        "name": "Chinese CBA",
        "bbr_path": "/international/china/",
        "strength": 0.65,
        "has_api": False,
        "api_code": None,
        "bet_markets": False,
    },}

#---- CONVENIENCE LOOKUP ----#
LEAGUE_STRENGTH = {k: v["strength"] for k, v in INTERNATIONAL_LEAGUES.items()}