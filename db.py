import mysql.connector

def get_db():
    """Connect to the MySQL database and create necessary tables if they do not exist."""
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="music_db"
    )
    
    cursor = db.cursor()

    # Create 'users' table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL
        )
    """)

    # Create 'playlists' table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS playlists (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            user_id INT,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        )
    """)

    # Create 'songs' table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS songs (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            artist VARCHAR(255) NOT NULL,
            album VARCHAR(255),
            duration TIME
        )
    """)

    # Create 'playlist_songs' table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS playlist_songs (
            id INT AUTO_INCREMENT PRIMARY KEY,
            playlist_id INT,
            song_id INT,
            song_order INT DEFAULT 0,
            FOREIGN KEY (playlist_id) REFERENCES playlists(id) ON DELETE CASCADE,
            FOREIGN KEY (song_id) REFERENCES songs(id) ON DELETE CASCADE
        )
    """)

    db.commit()
    return db
