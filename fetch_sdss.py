import requests

# Example to fetch an image from SDSS
def fetch_sdss_image(ra, dec, scale=0.2, width=400, height=400):
    url = "http://skyserver.sdss.org/dr16/SkyServerWS/ImgCutout/getjpeg"
    params = {
        'ra': ra,  # Right Ascension
        'dec': dec,  # Declination
        'scale': scale,
        'width': width,
        'height': height
    }
    response = requests.get(url, params=params)
    image_path = f"galaxy_{ra}_{dec}.jpg"
    if response.status_code == 200:
        with open(image_path, 'wb') as f:
            f.write(response.content)
        print(f"Image saved to {image_path}")
    else:
        print("Failed to retrieve image")

# Example usage
fetch_sdss_image(194.95, 27.98)
