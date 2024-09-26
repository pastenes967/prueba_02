import requests

# Buscar un libro usando la API de Open Library
query = "Cien años de soledad"  # Reemplaza con el libro que desees buscar
url = f"https://openlibrary.org/search.json?q={query}"
response = requests.get(url)

# Convertir la respuesta en formato JSON
data = response.json()

# Mostrar el título y el identificador de Open Library del primer libro
if data['docs']:
    book = data['docs'][0]
    title = book['title']
    olid = book['edition_key'][0]
    
    print(f"Título: {title}")
    print(f"OLID: {olid}")
    
    # Descargar el libro si está disponible en formato digital
    download_url = f"https://openlibrary.org/books/{olid}.json"
    book_info = requests.get(download_url).json()
    
    if 'formats' in book_info and 'pdf' in book_info['formats']:
        pdf_url = book_info['formats']['pdf']['url']
        pdf_response = requests.get(pdf_url)
        
        with open(f"{title}.pdf", 'wb') as file:
            file.write(pdf_response.content)
        
        print(f"Libro {title} descargado.")
    else:
        print("Este libro no está disponible en formato digital.")
else:
    print("No se encontró el libro.")
