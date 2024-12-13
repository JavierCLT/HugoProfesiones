import os
import json
import frontmatter

# Directorio que contiene los archivos Markdown
content_dir = 'C:/Users/javit/profesiones/content/profesiones/'

# Carpeta de salida para search.json
output_dir = 'C:/Users/javit/profesiones/static/'
output_file = 'search.json'

search_data = []

# Recorrer todos los archivos .md en el directorio
for filename in os.listdir(content_dir):
    if filename.endswith('.md'):
        filepath = os.path.join(content_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
            title = post.get('title', '')
            content = post.content
            slug = post.get('slug', '')
            if not slug:
                slug = os.path.splitext(filename)[0]
            href = f"/profesiones/{slug}/"
            search_data.append({
                'title': title,
                'content': content,
                'href': href
            })

# Guardar el índice de búsqueda en search.json
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

output_path = os.path.join(output_dir, output_file)
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(search_data, f, ensure_ascii=False, indent=2)

print(f"{output_file} generado exitosamente en {output_dir}")
