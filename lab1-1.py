import requests

def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break

def analyze_headers(headers):
    server_software = headers.get('Server', 'Not Found')
    print("Software used by the web server:", server_software)

    cookies = headers.get('Set-Cookie', None)
    if cookies:
        print("The site uses cookies.")
        cookie_names = [cookie.split(';')[0].split('=')[0] for cookie in cookies.split(',')]
        print("Cookie names:", cookie_names)
        # Παίρνουμε χρόνο διάρκειας του cookie (αν υπάρχει)
        for cookie in cookies.split(','):
            parts = cookie.split(';')
            for part in parts:
                if part.strip().startswith('Max-Age'):
                    max_age = part.split('=')[1]
                    print("Each cookie's name is valid for", max_age, "seconds.")
    else:
        print("The site does not use cookies.")

url = input("Enter the URL: ")  # ζητάμε URL από τον χρήστη

try:
    with requests.get(url) as response:  # απόκριση
        html = response.text
        more(html)
        print("\nAnalyzing HTTP response headers:")
        analyze_headers(response.headers)
except requests.exceptions.RequestException as e:
    print("Error occurred:", e)
