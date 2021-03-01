class Track:

    def __init__(self, name, artiste, timesplayed):
        self._name = name
        self._artiste = artiste
        self._timesplayed = timesplayed

    def __str__(self):
        return 'Track name: ' + self._name + '\nArtiste: ' + self._artiste + '\nTimes Played: ' + str(self._timesplayed)

    def get_name(self):
        return self._name

    def get_artiste(self):
        return self._artiste

    def get_times_played(self):
        return str(self._timesplayed)

    def play(self):
        self._timesplayed += 1
        return 'Playing: ' + self._name + '; ' + self._artiste + ' (' + str(self._timesplayed) + ')\n'


class TrackNode:

    def __init__(self, track, nextnode=None, prevnode=None):
        self._track = track
        self._next = nextnode
        self._prev = prevnode

    def get_track(self):
        return self._track

    def get_next(self):
        return self._next

    def set_next(self, nextnode):
        self._next = nextnode

    def get_prev(self):
        return self._prev

    def set_prev(self, prevnode):
        self._prev = prevnode


class PyToonz:

    def __init__(self):
        self._head = None
        self._tail = None
        self._cursor = None
        self._count = 0

    def __str__(self):
        if self._head is None:
            return 'Empty playlist'
        curr_node = self._head
        curr_track = curr_node.get_track()
        string_to_send = 'Playlist:\n'
        while curr_track is not None:
            if curr_node == self._cursor:
                string_to_send += '-->'
            string_to_send += curr_track.get_name()
            string_to_send += '; ' + curr_track.get_artiste()
            string_to_send += ' (' + curr_track.get_times_played() + ')'
            string_to_send += '\n'
            curr_node = curr_node.get_next()
            if curr_node is not None:
                curr_track = curr_node.get_track()
            else:
                curr_track = None

        return string_to_send

    def length(self):
        return self._count

    def add_track(self, track):
        new_node = TrackNode(track, None, self._tail)
        if self._count == 0:
            self._head = new_node
            self._cursor = new_node
        else:
            self._tail.set_next(new_node)
        self._tail = new_node
        self._count += 1

    def get_current(self):
        return self._cursor.get_track()

    def add_after(self, track):
        curr_track = self._cursor
        next_track = curr_track.get_next()
        new_node = TrackNode(track, next_track, curr_track)
        curr_track.set_next(new_node)
        next_track.set_prev(new_node)
        self._count += 1

    def next_track(self):
        next_track = self._cursor.get_next()
        if next_track is None:
            self._cursor = self._head
        else:
            self._cursor = next_track

    def prev_track(self):
        prev_track = self._cursor.get_prev()
        if prev_track is None:
            self._cursor = self._tail
        else:
            self._cursor = prev_track

    def reset(self):
        self._cursor = self._head

    def play(self):
        if self._cursor is None:
            print("No track is selected")
        else:
            track_played = self._cursor.get_track().play()
            print(track_played)

    def remove_current(self):
        curr_track = self._cursor
        if curr_track is not None:
            prev_track = curr_track.get_prev()
            next_track = curr_track.get_next()
            if self._count > 1:
                self.next_track()
            else:
                self._cursor = None
            if prev_track is not None:
                prev_track.set_next(next_track)
            else:
                self._head = next_track
            if next_track is not None:
                next_track.set_prev(prev_track)
            else:
                self._tail = prev_track
            self._count -= 1
