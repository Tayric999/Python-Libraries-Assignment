import requests
import os
import hashlib
from urllib.parse import urlparse

# 🔹 Function to safely download one image
def download_image(url, save_dir):
    try:
        # Send GET request with headers
        headers = {"User-Agent": "Mozilla/5.0 (compatible; ImageFetcher/1.0)"}
        response = requests.get(url, headers=headers, timeout=10)

        # Check HTTP status
        response.raise_for_status()  # Raises an error for 4xx/5xx responses

        # Check content type (must be an image)
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"⚠️ Skipped: {url} is not an image (Content-Type: {content_type})")
            return

        # Extract filename from URL or generate one
        path = urlparse(url).path
        filename = os.path.basename(path)
        if not filename:  # if URL doesn't contain filename
            ext = content_type.split("/")[-1]
            filename = f"image_{hashlib.md5(url.encode()).hexdigest()[:8]}.{ext}"

        # Compute file hash to prevent duplicates
        image_hash = hashlib.md5(response.content).hexdigest()
        existing_hashes = [f.split("_")[-1].split(".")[0] for f in os.listdir(save_dir)]
        if image_hash[:8] in existing_hashes:
            print(f"🟡 Duplicate skipped: {filename}")
            return

        # Save image
        filename = f"{filename.split('.')[0]}_{image_hash[:8]}.jpg"
        filepath = os.path.join(save_dir, filename)

        with open(filepath, "wb") as file:
            file.write(response.content)

        print(f"✅ Saved: {filename}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to fetch {url}: {e}")

# 🔹 Main function
def main():
    # Step 1: Create directory
    save_dir = "Fetched_Images"
    os.makedirs(save_dir, exist_ok=True)

    # Step 2: Ask for multiple URLs
    urls = input("Enter image URLs separated by commas:\n").split(",")

    # Step 3: Download each image
    for url in [u.strip() for u in urls if u.strip()]:
        download_image(url, save_dir)

    print("\n🎉 All downloads processed.")

# Run program
if __name__ == "__main__":
    main()
