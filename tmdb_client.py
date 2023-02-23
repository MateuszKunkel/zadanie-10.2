import requests


def get_authorized_dict():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "x"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_movies(how_many):
    data = get_authorized_dict()
    return data["results"][:how_many]

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


if __name__== "__main__":
    data = get_movies()
    print(data['results'][0])
