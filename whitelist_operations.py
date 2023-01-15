import json
import sqlite3
from rcon.source import Client


def add_to_whitelist(player_name, telegram_id):
    with open('config.json', 'r') as f:
        data = json.loads(f.read())
    con = sqlite3.connect('players_whitelist.sqlite')
    cur = con.cursor()
    x = cur.execute(f'''SELECT name FROM players
                    WHERE name == "{player_name}"
                     OR telegram_id == {telegram_id}''').fetchall()
    if len(x) == 0:
        cur.execute(f'''INSERT INTO players (name, telegram_id)
                        VALUES ("{player_name}", {telegram_id})''')
        con.commit()
        with Client(data.get('host'), data.get('port'),
                    passwd=data.get('pas')) as client:
            ans = client.run(f'whitelist add {player_name}')
        return True
    return False