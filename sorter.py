import os
import shutil

def find_duplicates(folder1, folder2):
    """
    Find duplicate images in two folders based on file names.
    """
    folder1_images = set(os.listdir(folder1))
    folder2_images = set(os.listdir(folder2))

    # Find intersection (duplicates)
    duplicates = folder1_images.intersection(folder2_images)

    # Find non-duplicates
    non_duplicates = folder1_images.union(folder2_images) - duplicates

    return duplicates, non_duplicates

def move_duplicates_and_non_duplicates(duplicates, non_duplicates, folder1, folder2, duplicate_folder, non_duplicate_folder):
    """
    Move duplicate images to duplicate folder and non-duplicate images to non-duplicate folder.
    """
    if not os.path.exists(duplicate_folder):
        os.makedirs(duplicate_folder)
    if not os.path.exists(non_duplicate_folder):
        os.makedirs(non_duplicate_folder)

    for image in duplicates:
        if image in os.listdir(folder1):
            shutil.move(os.path.join(folder1, image), duplicate_folder)
        elif image in os.listdir(folder2):
            shutil.move(os.path.join(folder2, image), duplicate_folder)

    for image in non_duplicates:
        if image in os.listdir(folder1):
            shutil.move(os.path.join(folder1, image), non_duplicate_folder)
        elif image in os.listdir(folder2):
            shutil.move(os.path.join(folder2, image), non_duplicate_folder)

def main():
    folder1 = "img_folder1"
    folder2 = "img_folder2"
    duplicate_folder = "duplicate"
    non_duplicate_folder = "non_duplicate"

    duplicates, non_duplicates = find_duplicates(folder1, folder2)
    move_duplicates_and_non_duplicates(duplicates, non_duplicates, folder1, folder2, duplicate_folder, non_duplicate_folder)

if __name__ == "__main__":
    main()
