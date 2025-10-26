Image Fetcher is a Python script that downloads one or multiple images from given URLs and saves them safely in a local folder called Fetched_Images.
It uses the requests library to handle HTTP requests, validates image content, prevents duplicates using hashes, and handles connection errors gracefully.

⚙️ Features

✅ Download single or multiple images at once
✅ Automatically creates a folder Fetched_Images/
✅ Skips duplicate images using content hashing
✅ Checks that files are real images (using HTTP headers)
✅ Handles timeouts, broken links, and server errors
✅ Generates unique filenames automatically

🧠 How It Works

The script prompts you to enter one or more image URLs (comma-separated).
It creates the folder Fetched_Images if it doesn’t exist.

For each URL:
Sends a GET request with proper headers
Verifies the response status and content type
Prevents downloading the same image twice
Saves the image in binary mode (.jpg)
Displays progress and skips any invalid URLs.

🧩 Example Run
$ python fetch_images.py
Enter image URLs separated by commas:
https://upload.wikimedia.org/wikipedia/commons/3/3a/Cat03.jpg, https://upload.wikimedia.org/wikipedia/commons/e/ec/Stray_dog_in_Bangkok.jpg


Output:
✅ Saved: Cat03_2a4d7f3a.jpg
✅ Saved: Stray_dog_in_Bangkok_f5b3a2d8.jpg
🎉 All downloads processed.


Your images will now appear inside the Fetched_Images/ directory.

📁 Folder Structure
project/
│
├── fetch_images.py
├── README.md
└── Fetched_Images/
    ├── Cat03_2a4d7f3a.jpg
    └── Stray_dog_in_Bangkok_f5b3a2d8.jpg

🔒 Safety Precautions

When downloading files from unknown sources:
Always check Content-Type to ensure it’s an image
Avoid opening images from untrusted sources immediately
Use timeout in requests to prevent hanging connections
Optionally, check Content-Length to avoid downloading huge files
Keep downloaded files in a separate folder from your system files

🧾 Important HTTP Headers Checked
Header	Purpose
Content-Type	Ensures file is an image
Content-Length	(Optional) Check file size
Last-Modified	(Optional) See when the file was updated
ETag	Helps detect duplicates
User-Agent	Identifies your request politely to servers
🧰 Requirements

Python 3.x
requests library
Install dependency:
pip install requests

🚀 Future Enhancements

 Add progress bar (using tqdm)
 Add image preview after saving
 Add file size limit
 Add optional image format filter (.jpg/.png)
