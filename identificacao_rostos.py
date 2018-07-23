"""
Fernando Amaro
Identificacao de rostos utilizando OpenCV
Pressione <esc> para sair OU <s> para salvar.

OBS.: Antes de executar definir o caminho do XML Haarcascades na instalacao do OpenCV

"""

import cv2

#insert haarcascades xml full path
face_cascade = cv2.CascadeClassifier('C:\\Python27\\libs\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_default.xml');
eye_cascade = cv2.CascadeClassifier('C:\\Python27\\libs\\opencv\\sources\\data\\haarcascades\\haarcascade_eye.xml');

def show_webcam(mirror=False):
    
    cam = cv2.VideoCapture(0)
    cam.set(cv2.CAP_PROP_FPS, 100);
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 900);
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 640);
       
    while True:
        # Capture frame-by-frame
        ret_val, img = cam.read()
        
        if ret_val == True:
            
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray,
                                              scaleFactor=1.3,
                                              minNeighbors=5,
                                              minSize=(30, 30),
                                              flags=cv2.CASCADE_SCALE_IMAGE
                                              )           
            if mirror:
                img = cv2.flip(img, 1,0)
                # detect MultiScale / faces 
                # Draw a rectangle around the faces
                for (x,y,w,h) in faces:
                         cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                         roi_gray = gray[y:y+h, x:x+w]
                         roi_color = img[y:y+h, x:x+w]
                         eyes = eye_cascade.detectMultiScale(roi_gray)
                         for (ex,ey,ew,eh) in eyes:
                             cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
                             cv2.imshow('Identificar Rosto', img)
                k=cv2.waitKey(1)       
                if k == 27:
                   break  # esc to quit
                elif k == ord('s'): #s to save
                     cv2.imwrite('captura.png',img)
                     cv2.destroyAllWindows()

def main():
    show_webcam(mirror=True)


if __name__ == '__main__':
    main()

# When everything is done, release the capture
cv2.destroyAllWindows()
