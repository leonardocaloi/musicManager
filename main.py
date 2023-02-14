from music_manager import MusicManager


def console():
    print("Welcome to the music manager system!")

    while True:
        print("\nAvailable commands:")
        print("  add: Add a new song to the list.")
        print("  search_title: Search for a song by its title.")
        print("  search_year: Search for all songs released in a given year.")
        print("  playlist: Generate a random playlist with all songs.")
        print("  exit: Quit the program.")
        command = input("Enter a command: ").strip().lower()

        if command == "add":
            title = input("Enter the song title: ").strip()
            artist = input("Enter the artist name: ").strip()
            while True:
                try:
                    year = int(input("Enter the year of release: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")
            manager.add_song(title, artist, year)

        elif command == "search_title":
            title = input("Enter the song title: ").strip()
            manager.search_by_title(title)

        elif command == "search_year":
            while True:
                try:
                    year = int(input("Enter the year to search: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")
            manager.search_by_year(year)

        elif command == "playlist":
            manager.random_playlist()

        elif command == "exit":
            print("Goodbye!")
            break


if __name__ == '__main__':
    manager = MusicManager('songs.csv')
    console()

