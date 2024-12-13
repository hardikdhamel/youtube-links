import requests

def get_youtube_links(search_query, api_key, max_results=5):
    search_url = "https://www.googleapis.com/youtube/v3/search"
    
    params = {
        "part": "snippet",
        "q": search_query,
        "type": "video",
        "key": api_key,
        "maxResults": max_results
    }
    
    response = requests.get(search_url, params=params)
    
    if response.status_code != 200:
        raise Exception(f"Error fetching data from YouTube API: {response.status_code}")
    
    data = response.json()
    
    video_links = [
        f"https://www.youtube.com/watch?v={item['id']['videoId']}"
        for item in data.get("items", [])
    ]
    
    return video_links

if __name__ == "__main__":
    API_KEY = "YOUR_API_KEY"
    search_term = "Python tutorials"
    
    try:
        links = get_youtube_links(search_term, API_KEY)
        print(f"Top {len(links)} results for '{search_term}':")
        for link in links:
            print(link)
    except Exception as e:
        print(e)