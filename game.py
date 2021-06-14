class PlayerProfile:
    def __init__(self, gamer_tag, email):
        self._gamer_tag = gamer_tag
        self._email = email
        self._games_played = []
        self._preferred_server = None
        self._system = None
        self._comms = "No Mics"
        self._time_online = None
        self._time_zone = None
        self._online_status = "Offline"
        self._valid_systems = ['ps3', 'xbox one', "nintendo_switch", 'ps4', 'ps5', 'xbox_series_x']

    def set_time_zone(self, timezone):
        pass

    def create_profile(self):
        for system_type in self._valid_systems:
            print(system_type)
        system = input("Which of these systems do you play on?")
        if system not in self._valid_systems:
            print("Please enter system from list")





    class Rating:
        def __init__(self, friendliness_rate, skill_rate, teamplay_rate):
            self._play_review = None
            self._game_skill_rating = skill_rate
            self._teamplay_rating = teamplay_rate
            self._friendliness_rate = friendliness_rate



class PlayerDatabase:
    def __init__(self):
        self._database = []