import os

# Supported image file extensions
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']

# Get all image files in current directory
image_files = [f for f in os.listdir('.') if os.path.splitext(f)[1].lower() in image_extensions and os.path.isfile(f)]

# Sort files to rename in order
image_files.sort()

# Rename images
for i, filename in enumerate(image_files, start=1):
    ext = os.path.splitext(filename)[1]
    new_name = f'image{i}{ext}'
    
    # Skip renaming if the name is already correct
    if filename == new_name:
        continue

    # Check if new name already exists to avoid overwriting
    if os.path.exists(new_name):
        print(f'Skipping {filename} -> {new_name} (already exists)')
        continue

    os.rename(filename, new_name)
    print(f'Renamed: {filename} -> {new_name}')
