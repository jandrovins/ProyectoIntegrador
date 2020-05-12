# Para hacer un envío por POST de un dato, y crear una instancia de Measure
curl -d type=temperatura -d value=1111 -d scale=K http://127.0.0.1:8000/measure/

# Para recibir de la base de datos todos los valores que hayan sido ingresados anteriormente (GET)
curl http://127.0.0.1:8000/measure/
