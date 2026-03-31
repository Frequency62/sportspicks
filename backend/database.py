#database.py

import sqlite3
from config import DB_PATH

#---- CONNECT TO DATABASE FILE - CREATE IF DOES NOT EXIST ----#
def get_connection(): 
    connection = sqlite3.connect(DB_PATH)
    return connection

#---- CREATE ALL TABLES IN DATABASE ----#
def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS players (
            player_id       TEXT PRIMARY KEY,
            name            TEXT NOT NULL,
            position        TEXT,
            team            TEXT,
            is_active       INTEGER
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS player_season_averages (
            player_id           TEXT NOT NULL,
            season              INTEGER NOT NULL,
            team                TEXT,
            games_played        INTEGER,
            minutes             REAL,
            points              REAL,
            rebounds            REAL,
            assists             REAL,
            steals              REAL,
            blocks              REAL,
            turnovers           REAL,
            threes              REAL,
            fg_pct              REAL,
            ft_pct              REAL,
            ts_pct              REAL,
            usage_rate          REAL,
            per                 REAL,
            PRIMARY KEY (player_id, season)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS player_game_logs (
            player_id           TEXT NOT NULL,
            game_date           TEXT NOT NULL,
            season              INTEGER NOT NULL,
            team                TEXT,
            opponent            TEXT,
            home_away           TEXT,
            minutes             REAL,
            points              INTEGER,
            rebounds            INTEGER,
            assists             INTEGER,
            steals              INTEGER,
            blocks              INTEGER,
            turnovers           INTEGER,
            threes              INTEGER,
            fga                 INTEGER,
            fgm                 INTEGER,
            fta                 INTEGER,
            ftm                 INTEGER,
            plus_minus          INTEGER,
            PRIMARY KEY (player_id, game_date)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS team_stats (
            team                TEXT NOT NULL,
            season              INTEGER NOT NULL,
            wins                INTEGER,
            losses              INTEGER,
            pace                REAL,
            off_rating          REAL,
            def_rating          REAL,
            net_rating          REAL,
            PRIMARY KEY (team, season)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS player_career_arc (
            player_id                   TEXT NOT NULL,
            season                      INTEGER NOT NULL,
            league                      TEXT NOT NULL,
            team                        TEXT,
            age                         INTEGER,
            games_played                INTEGER,
            points                      REAL,
            rebounds                    REAL,
            assists                     REAL,
            steals                      REAL,
            blocks                      REAL,
            turnovers                   REAL,
            threes                      REAL,
            fg_pct                      REAL,
            ft_pct                      REAL,
            era_normalized_pts          REAL,
            era_normalized_reb          REAL,
            era_normalized_ast          REAL,
            data_completeness           REAL,
            is_pre_tracking             INTEGER,
            source                      TEXT,
            PRIMARY KEY (player_id, season, league)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS odds (
            id                  INTEGER PRIMARY KEY AUTOINCREMENT,
            game_id             TEXT NOT NULL,
            sportsbook          TEXT NOT NULL,
            market              TEXT NOT NULL,
            player_id           TEXT,
            line                REAL,
            over_odds           INTEGER,
            under_odds          INTEGER,
            pulled_at           TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS picks (
            id                  INTEGER PRIMARY KEY AUTOINCREMENT,
            player_id           TEXT,
            game_id             TEXT NOT NULL,
            market              TEXT NOT NULL,
            projection          REAL NOT NULL,
            line                REAL NOT NULL,
            confidence          REAL,
            result              TEXT,
            actual_value        REAL,
            created_at          TEXT NOT NULL,
            was_placed          INTEGER
        )
    """)

    connection.commit()

if __name__ == "__main__":
    conn = get_connection()
    create_tables(conn)
    print("Tables created successfully")
    conn.close()