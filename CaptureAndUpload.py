import random
import time
import dropbox
import cv2

start_time = time.time()

def takeSnapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while result:
        ret, frame = videoCaptureObject.read()
        img_name = "IMG" + str(number) + '.jpg'
        cv2.imwrite(img_name, frame)
        start_time = time.time()
        result = False
    print("Snapshot taken!")
    videoCaptureObject.release()
    cv2.destroyAllWindows()
    return img_name

def upload_file(img_name):
    access_token = 'sl.BEe2UFDrplp82qeGZOIn8uqtX0Mch5kX_NwKEKOroK_zxXjHrNlkWnT2AR-3fAvHCPpEHuJfokI-x354_rXISgfTQRQuFPD5KPwLZxd6c6Ueq_wafhM1CdR3n0504BKMiHTm1Icb'
    dbx = dropbox.Dropbox(access_token)
    file_from = img_name
    file_to = '/test/' + file_from
    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)

def main():
    while(True):
        if(time.time() - start_time >= 10):
            name = takeSnapshot()
            upload_file(name)

main()