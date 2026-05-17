import cv2

imagem = cv2.imread('foto.jpg')

if imagem is None:
    print("Erro ao carregar a imagem.")
else:
    suavizada = cv2.GaussianBlur(imagem, (15, 15), 0)

    cv2.imshow('Imagem Original', imagem)
    cv2.imshow('Filtro Gaussiano', suavizada)

    cv2.imwrite('resultado_gaussiano.jpg', suavizada)

    cv2.waitKey(0)
    cv2.destroyAllWindows()