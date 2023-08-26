import requests

def download_image(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)
    print("Image downloaded.")

image_url = input("Enter the image URL: ")
file_name = input("Enter the desired file name: ")
download_image(image_url, file_name)
