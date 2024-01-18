import cv2
import os

input_folder = "./video"
output_folder = "./frame"

# Создаем папку для сохранения кадров, если ее нет
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Проходим по всем файлам в папке input_folder
for filename in os.listdir(input_folder):
    # Проверяем, что файл является видео
    if filename.endswith(".mp4") or filename.endswith(".avi"):
        # Открываем видеофайл
        video = cv2.VideoCapture(os.path.join(input_folder, filename))
        # Создаем папку для сохранения кадров из текущего видео
        video_output_folder = os.path.join(output_folder, os.path.splitext(filename)[0])
        if not os.path.exists(video_output_folder):
            os.makedirs(video_output_folder)
        # Считываем кадры из видео и сохраняем их в папку video_output_folder
        success, image = video.read()
        count = 0
        while success:
            cv2.imwrite(os.path.join(video_output_folder, "frame%d.jpg" % count), image)
            success, image = video.read()
            count += 1
