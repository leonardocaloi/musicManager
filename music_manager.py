import csv
import random


class MusicManager:

    def __init__(self, filename):
        self.songs = []
        self.load_songs(filename)

    def add_song(self, title, artist, year):
        with open('songs.csv', 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([f"'{title}'", f"'{artist}'", year])
        self.songs.append((title, artist, year))
        print("Song added successfully!")

    def search_by_title(self, title):
        found = False
        for song in self.songs:
            if song[0].lower() == title.lower():
                print(f"{song[0]} - {song[1]} ({song[2]})")
                found = True
        if not found:
            print("No songs found with this title.")

    def search_by_year(self, year):
        found = False
        for song in self.songs:
            if song[2] == year:
                print(f"{song[0]} - {song[1]} ({song[2]})")
                found = True
        if not found:
            print("No songs found for this year.")

    def random_playlist(self):
        if len(self.songs) == 0:
            print("There are no songs registered.")
            return
        playlist = random.sample(self.songs, len(self.songs))
        print("Random playlist:")
        for i, song in enumerate(playlist):
            print(f"{i+1}. {song[0]} - {song[1]} ({song[2]})")

    def load_songs(self, filename):
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                title, artist, year = row
                self.songs.append((title, artist, int(year)))
