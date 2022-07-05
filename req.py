import requests

def fetch_url(url: str, session: requests.Session):
    response = session.request(method="GET", url=url)
    print(response.text.strip())

def get_url():
    with requests.Session() as session:
        for i in range(50):
            fetch_url("https://commitment.herokuapp.com/txt", session)

if __name__ == "__main__":
    get_url()

