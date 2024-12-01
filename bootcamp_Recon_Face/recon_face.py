from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import OperationStatus
import time
import os

# Adicionar as crendicias do servilo de IA do Azure
key = "CMKGysBvwV0BqrI7J3ULyCOXca7uPvPoYhLyqjTPSz5WFPEjmH0VJQQJ99ALACYeBjFXJ3w3AAAEACOGvhHY"
endpoint = "https://btdioreconface01.cognitiveservices.azure.com/"

# Criar um client para o serviço do Face
face_client = FaceClient(endpoint, CognitiveServicesCredentials(key))
'''
def detect_faces(img_url):
    # Detecta o rosto em uma imagem
    faces = client.face.detect_with_url(url=img_url, return_face_attributes=['age', 'gender', 'emotion'])
    return faces

def verify_faces(face_id1):
    # Verifica se face
    verify_result = client.face.verify_face_to_face(face_id1)
    return verify_result.confidence
# Testando a aplicação
img_url = "https://drive.google.com/file/d/1Y58P9KWdNzNho7FiyoBmyX24hJMad2w0/view?usp=drive_link"
faces = detect_faces(img_url)
'''
def detect_single_face(img_path):
    # Detecção de apenas uma face em uma imagem local
    with open(img_path, "rb") as image_file:
        detect_single_face = face_client.face.detect_with_stream(
            image=image_file, 
            detection_model="detection_03",
            recognition_model="detection_04",
            return_face_attributes=["age", "gender", "emotion"]
        )
    return detect_single_face
    

    # Solicita ao usuário que escolha uma imagem
img_path = input("Digite o caminho completo da imagem: ")

    # Verifica se o arquivo existe
if not os.path.exists(img_path):
    print("Arquivo não encontrado.")

else:
    # Chama a função para detectar a face
    faces = detect_single_face(img_path)
    for face in faces:
    # Se o rosto for detectado, extraimos as informações necessaria.
       
        print("Age:", face.face_attributes.age)
        print("Gender:", face.face_attributes.gender)
        print("Emotions:", face.face_attributes.emotion)
