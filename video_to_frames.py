import os
import sys
import cv2

video_file = sys.argv[1]
save_dir = sys.argv[2]

video = cv2.VideoCapture(video_file)

if not video.isOpened():

    print("Could not open video file")
    video.release()
    exit()

frame_count = 0

while video.isOpened():

    status, frame = video.read()

    if not status:
        break

    frame_count += 1

    out_file = save_dir + os.path.sep + 'frame_' + str(frame_count) + '.jpg'

    print('writing file to .. ', out_file)

    cv2.imwrite(out_file, frame)
    

video.release()
