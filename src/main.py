"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

try:
    from .recommender import load_songs, recommend_songs
except ImportError:
    from recommender import load_songs, recommend_songs


def print_recommendations(profile_name: str, user_prefs: dict, songs: list) -> None:
    mode = user_prefs.get("scoring_mode", "balanced")
    recommendations = recommend_songs(user_prefs, songs, k=5, mode=mode)

    print(f"\n=== {profile_name} ===")
    print(f"Scoring Mode: {mode}")
    print(f"Preferences: {user_prefs}")
    print("Top 5 recommendations:\n")

    for idx, rec in enumerate(recommendations, start=1):
        song, score, explanation = rec
        reasons = [reason.strip() for reason in explanation.split(";") if reason.strip()]

        print(f"{idx}. {song['title']} by {song['artist']}")
        print(f"   Score   : {score:.2f}")
        print("   Reasons :")
        for reason in reasons:
            print(f"   - {reason}")
        print()

def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    profiles = [
        (
            "Genre-First Pop Explorer",
            {
                "genre": "pop",
                "mood": "euphoric",
                "energy": 0.78,
                "preferred_mood_tags": ["party", "bold"],
                "preferred_decade": 2010,
                "scoring_mode": "genre-first",
            },
        ),
        (
            "Mood-First Dream Listener",
            {
                "genre": "indie",
                "mood": "dreamy",
                "energy": 0.55,
                "likes_acoustic": True,
                "preferred_mood_tags": ["nostalgic", "introspective", "dreamy"],
                "scoring_mode": "mood-first",
            },
        ),
        (
            "Energy-Focused Gym Session",
            {
                "genre": "rap",
                "mood": "intense",
                "energy": 0.92,
                "min_popularity": 75,
                "target_lyrical_density": 0.55,
                "scoring_mode": "energy-focused",
            },
        ),
        (
            "Balanced All-Rounder",
            {
                "genre": "pop",
                "mood": "sad",
                "energy": 0.9,
                "likes_acoustic": True,
                "max_explicitness": 0.3,
                "scoring_mode": "balanced",
            },
        ),
    ]

    for profile_name, user_prefs in profiles:
        print_recommendations(profile_name, user_prefs, songs)


if __name__ == "__main__":
    main()
