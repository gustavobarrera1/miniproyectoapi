# Ingresar a la pagina y descargar un gif, luego mostrarlo en pantalla
# hacer un bucle para que se repita el proceso hasta unos X gifs mostrados

import requests
import cv2
import time


def run():

    num = int(input("Ingrese la cantidad de gif que quiere ver: "))

    for i in range(num):

        # descarga de la imagen/gif

        f = open("gato.gif", "wb")
        response = requests.get(
            "https://cataas.com/cat/gif"
        )  # consulta a la pagina de gif aleatorios
        f.write(response.content)
        f.close()

        for i in range(2):  # repeticion del gif para visualizarlo mejor

            gif = cv2.VideoCapture("gato.gif")

            # Abrir y mostrar gif

            while gif.isOpened():
                res, frame = gif.read()  # lee imagen x imagen

                if (
                    res == False
                ):  # si deja de tener fotogramas o imagenes a mostrar se cierra

                    break

                cv2.imshow("gato", frame)

                cv2.waitKey(1)

                time.sleep(1 / 30)  # delay para que funcione a 30fps


if __name__ == "__main__":
    run()

gif.release()
cv2.destroyAllWindows
