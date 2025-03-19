import time
import requests # type: ignore
from enum import Enum
import os

class wled_effect(Enum):
    """
    Enum for WLED effects. 
    Note: This is not exhaustive, add more as needed from the WLED documentation.
    """
    SOLID = 0
    BLINK = 1
    BREATHE = 2
    WIPE = 3
    WIPE_RANDOM = 4
    RANDOM_COLORS = 5
    SWEEP = 6
    DYNAMIC = 7
    COLORLOOP = 8
    RAINBOW = 9
    SCAN = 10
    SCAN_DUAL = 11
    FADE = 12
    THEATER = 13
    THEATER_RAINBOW = 14
    RUNNING = 15
    SAW = 16
    TWINKLE = 17
    DISSOLVE = 18
    DISSOLVE_RND = 19
    SPARKLE = 20
    SPARKLE_DARK = 21
    SPARKLE_PLUS = 22
    STROBE = 23
    STROBE_RAINBOW = 24
    STROBE_MEGA = 25
    BLINK_RAINBOW = 26
    ANDROID = 27
    CHASE = 28
    CHASE_RANDOM = 29
    CHASE_RAINBOW = 30
    CHASE_FLASH = 31
    CHASE_FLASH_RND = 32
    RAINBOW_RUNNER = 33
    COLORFUL = 34
    TRAFFIC_LIGHT = 35
    SWEEP_RANDOM = 36
    CHASE_2 = 37
    AURORA = 38
    STREAM = 39
    SCANNER = 40
    LIGHTHOUSE = 41
    FIREWORKS = 42
    RAIN = 43
    TETRIX = 44
    FIRE_FLICKER = 45
    GRADIENT = 46
    LOADING = 47
    ROLLING_BALLS = 48
    FAIRY = 49
    TWO_DOTS = 50
    FAIRYTWINKLE = 51
    RUNNING_DUAL = 52
    RSVD = 53
    CHASE_3 = 54
    TRI_WIPE = 55
    TRI_FADE = 56
    LIGHTNING = 57
    ICU = 58
    MULTI_COMET = 59
    SCANNER_DUAL = 60
    STREAM_2 = 61
    OSCILLATE = 62
    PRIDE_2015 = 63
    JUGGLE = 64
    PALETTE = 65
    FIRE_2012 = 66
    COLORWAVES = 67
    BPM = 68
    FILL_NOISE = 69
    NOISE_1 = 70
    NOISE_2 = 71
    NOISE_3 = 72
    NOISE_4 = 73
    COLORTWINKLES = 74
    LAKE = 75
    METEOR = 76
    METEOR_SMOOTH = 77
    RAILWAY = 78
    RIPPLE = 79
    TWINKLEFOX = 80
    TWINKLECAT = 81
    HALLOWEEN_EYES = 82
    SOLID_PATTERN = 83
    SOLID_PATTERN_TRI = 84
    SPOTS = 85
    SPOTS_FADE = 86
    GLITTER = 87
    CANDLE = 88
    FIREWORKS_STARBURST = 89
    FIREWORKS_1D = 90
    BOUNCING_BALLS = 91
    SINELON = 92
    SINELON_DUAL = 93
    SINELON_RAINBOW = 94
    POPCORN = 95
    DRIP = 96
    PLASMA = 97
    PERCENT = 98
    RIPPLE_RAINBOW = 99
    HEARTBEAT = 100
    PACIFICA = 101
    CANDLE_MULTI = 102
    SOLID_GLITTER = 103
    SUNRISE = 104
    PHASED = 105
    TWINKLEUP = 106
    NOISE_PAL = 107
    SINE = 108
    PHASED_NOISE = 109
    FLOW = 110
    CHUNCHUN = 111
    DANCING_SHADOWS = 112
    WASHING_MACHINE = 113
    BLENDS = 115
    TV_SIMULATOR = 116
    DYNAMIC_SMOOTH = 117
    SPACESHIPS = 118
    CRAZY_BEES = 119
    GHOST_RIDER = 120
    BLOBS = 121
    SCROLLING_TEXT = 122
    DRIFT_ROSE = 123
    DISTORTION_WAVES = 124
    SOAP = 125
    OCTOPUS = 126
    WAVING_CELL = 127
    PIXELS = 128
    PIXELWAVE = 129
    JUGGLES = 130
    MATRIPIX = 131
    GRAVIMETER = 132
    PLASMOID = 133
    PUDDLES = 134
    MIDNOISE = 135
    NOISEMETER = 136
    FREQWAVE = 137
    FREQMATRIX = 138
    GEQ = 139
    WATERFALL = 140
    FREQPIXELS = 141
    NOISEFIRE = 143
    PUDDLEPEAK = 144
    NOISEMOVE = 145
    NOISE2D = 146
    PERLIN_MOVE = 147
    RIPPLE_PEAK = 148
    FIRENOISE = 149
    SQUARED_SWIRL = 150
    DNA = 152
    MATRIX = 153
    METABALLS = 154
    FREQMAP = 155
    GRAVCENTER = 156
    GRAVCENTRIC = 157
    GRAVFREQ = 158
    DJ_LIGHT = 159
    FUNKY_PLANK = 160
    PULSER = 162
    BLURZ = 163
    DRIFT = 164
    WAVERLY = 165
    SUN_RADIATION = 166
    COLORED_BURSTS = 167
    JULIA = 168
    GAME_OF_LIFE = 172
    TARTAN = 173
    POLAR_LIGHTS = 174
    SWIRL = 175
    LISSAJOUS = 176
    FRIZZLES = 177
    PLASMA_BALL = 178
    FLOW_STRIPE = 179
    HIPHOTIC = 180
    SINDOTS = 181
    DNA_SPIRAL = 182
    BLACK_HOLE = 183
    WAVESINS = 184
    ROCKTAVES = 185
    AKEMI = 186

class wled_palette(Enum):   
    """
    Enum for WLED color palettes.
    Note: This is not exhaustive, add more as needed from the WLED documentation.
    """
    DEFAULT = 0
    RANDOM_CYCLE = 1
    COLOR_1 = 2
    COLORS_1_2 = 3
    COLOR_GRADIENT = 4
    COLORS_ONLY = 5
    PARTY = 6
    CLOUD = 7
    LAVA = 8
    OCEAN = 9
    FOREST = 10
    RAINBOW = 11
    RAINBOW_BANDS = 12
    SUNSET = 13
    RIVENDELL = 14
    BREEZE = 15
    RED_BLUE = 16
    YELLOWOUT = 17
    ANALOGOUS = 18
    SPLASH = 19
    PASTEL = 20
    SUNSET_2 = 21
    BEACH = 22
    VINTAGE = 23
    DEPARTURE = 24
    LANDSCAPE = 25
    BEECH = 26
    SHERBET = 27
    HULT = 28
    HULT_64 = 29
    DRYWET = 30
    JUL = 31
    GRINTAGE = 32
    REWHI = 33
    TERTIARY = 34
    FIRE = 35
    ICEFIRE = 36
    CYANE = 37
    LIGHT_PINK = 38
    AUTUMN = 39
    MAGENTA = 40
    MAGRED = 41
    YELMAG = 42
    YELBLU = 43
    ORANGE_TEAL = 44
    TIAMAT = 45
    APRIL_NIGHT = 46
    ORANGERY = 47
    C9 = 48
    SAKURA = 49
    AURORA = 50
    ATLANTICA = 51
    C9_2 = 52
    C9_NEW = 53
    TEMPERATURE = 54
    AURORA_2 = 55
    RETRO_CLOWN = 56
    CANDY = 57
    TOXY_REAF = 58
    FAIRY_REAF = 59
    SEMI_BLUE = 60
    PINK_CANDY = 61
    RED_REAF = 62
    AQUA_FLASH = 63
    YELBLU_HOT = 64
    LITE_LIGHT = 65
    RED_FLASH = 66
    BLINK_RED = 67
    RED_SHIFT = 68
    RED_TIDE = 69
    CANDY2 = 70

class wled_ctl:
    """
    A class for controlling a WLED device.
    """

    def __init__(self, ip_address):
        """
        Initializes a new WLED object.

        Args:
            ip_address (str): The IP address of the WLED device.
        """
        self._ip_address = ip_address
        self._base_url = f"http://{self._ip_address}/json/state"


    # Sends a JSON request to the WLED device.
    # Args:
    #     payload (dict): The JSON payload to send.
    # Returns:
    #     bool: True if the request was successful, False otherwise.
    def _send_request(self, payload):
        """
        Sends a JSON request to the WLED device.

        Args:
            payload (dict): The JSON payload to send.

        Returns:
            bool: True if the request was successful, False otherwise.
        """
        try:
            response = requests.post(self._base_url, json=payload)
            response.raise_for_status()  # Raise an exception for bad status codes
            return True
        except requests.exceptions.RequestException as e:
            print(f"Error sending request: {e}")
            return False

    # Turns on the wled strip
    def turn_on(self):
        """Turns the WLED device on."""
        payload = {"on": True}
        return self._send_request(payload)

    # Turns off the wled strip
    def turn_off(self):
        """Turns the WLED device off."""
        payload = {"on": False}
        return self._send_request(payload)

    # Sets the brightness of the WLED device.
    # Args:
    #     brightness (int): The brightness level (0-255).
    def set_brightness(self, brightness):
        """
        Sets the brightness of the WLED device.

        Args:
            brightness (int): The brightness level (0-255).
        """
        payload = {"bri": brightness}
        return self._send_request(payload)

    # Sets the effect of the WLED device.
    # Args:
    #     effect (WLEDEffect): The enum value for the effect.
    def set_effect(self, effect: wled_effect):
        """
        Sets the effect of the WLED device.

        Args:
            effect (WLEDEffect): The enum value for the effect.
        """
        payload = {"seg": [{"fx": effect.value}]}
        return self._send_request(payload)

    # Sets the color palette of the WLED device.
    # Args:
    #     palette (WLEDPalette): The enum value for the color palette.
    def set_palette(self, palette: wled_palette):
        """
        Sets the color palette of the WLED device.

        Args:
            palette (WLEDPalette): The enum value for the color palette.
        """
        payload = {"seg": [{"pal": palette.value}]}
        return self._send_request(payload)

    # Sets the color of the WLED device.
    # Args:
    #     red (int): The red value (0-255).
    #     green (int): The green value (0-255).
    #     blue (int): The blue value (0-255).
    def set_color(self, red, green, blue):
        """
        Sets the color of the WLED device.

        Args:
            red (int): The red value (0-255).
            green (int): The green value (0-255).
            blue (int): The blue value (0-255).
        """
        payload = {"seg": [{"col": [[red, green, blue]]}]}  # Note the nested list for color
        return self._send_request(payload)

    # Checks a connection to a wled device
    def _check_connection(self,ip_address):
        """Pings a wled devcie and returns true if it is reachable."""
        command = f"ping -c 4 {ip_address}"  # -c 4 limits to 4 pings
        process = os.popen(command)
        output = process.read()
        if "0 received" in output:
            return False
        else:
            return True

    def refresh_is_connected(self):
        '''
        Refreshes the is_connected property.
        '''
        self._is_connected = self._check_connection(self._ip_address)

    @property
    def is_connected(self):
        """The is_connected property."""
        return self._is_connected
    @is_connected.setter
    def is_connected(self, value):
        self._is_connected = value

if __name__ == "__main__":
    ip_ipaddress1 = '192.168.1.1'
    wlctl = wled_ctl(ip_ipaddress1)
    wlctl = wled_ctl(ip_ipaddress1)
    wlctl.refresh_is_connected()
    if wlctl.is_connected:
        wlctl.turn_off()
        wlctl.set_palette(wled_palette.RAINBOW)
        wlctl.set_effect(wled_effect.FIREWORKS_STARBURST)
        wlctl.turn_on()