import requests

def main():
    print("KOD ISHLAYAPTI!")  # test qatori
    url = "https://api.github.com"
    response = requests.get(url)
    print(f"Status code: {response.status_code}")
    print("Response headers:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()

