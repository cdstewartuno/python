class Television:
    # Class constants
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        # Instance variables
        self._status = False
        self._muted = False
        self._volume = Television.MIN_VOLUME
        self._channel = Television.MIN_CHANNEL

    def power(self):
        """Turns the TV on and off by toggling the status."""
        self._status = not self._status
        if not self._status:
            self._muted = False  # TV is off, unmute it
            self._volume = Television.MIN_VOLUME  # Reset volume when powered off

    def mute(self):
        """Toggles the mute status, and un-mutes the TV if the volume is changed."""
        if self._status:
            self._muted = not self._muted
            if not self._muted:
                self._volume = max(self._volume, Television.MIN_VOLUME)  # Unmute and adjust volume
        else:
            self._muted = False  # Unmute when the TV is off

    def channel_up(self):
        """Increases the channel value. Loops back to the minimum channel after reaching the maximum."""
        if self._status:
            self._channel += 1
            if self._channel > Television.MAX_CHANNEL:
                self._channel = Television.MIN_CHANNEL

    def channel_down(self):
        """Decreases the channel value. Loops back to the maximum channel after reaching the minimum."""
        if self._status:
            self._channel -= 1
            if self._channel < Television.MIN_CHANNEL:
                self._channel = Television.MAX_CHANNEL

    def volume_up(self):
        """Increases the volume. Does nothing if muted or at max volume."""
        if self._status:
            if self._muted:
                self._muted = False  # Unmute if volume is changed
            self._volume = min(self._volume + 1, Television.MAX_VOLUME)

    def volume_down(self):
        """Decreases the volume. Does nothing if muted or at min volume."""
        if self._status:
            if self._muted:
                self._muted = False  # Unmute if volume is changed
            self._volume = max(self._volume - 1, Television.MIN_VOLUME)

    def __str__(self):
        """Returns the status of the TV in a formatted string."""
        return f"Power = {self._status}, Channel = {self._channel}, Volume = {self._volume}"
