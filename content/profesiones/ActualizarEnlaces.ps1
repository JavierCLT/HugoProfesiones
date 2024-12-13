# ActualizarEnlaces.ps1

# Definir la ruta al directorio de profesiones
$directory = "C:\Users\javit\profesiones\content\profesiones\"

# Definir el patrón de búsqueda y reemplazo
$pattern = '/tecnología/'
$replacement = '/profesiones/'

# Obtener todos los archivos .md en el directorio y subdirectorios
$files = Get-ChildItem -Path $directory -Filter *.md -Recurse

foreach ($file in $files) {
    # Leer el contenido del archivo
    $content = Get-Content -Path $file.FullName

    # Reemplazar el patrón
    $newContent = $content -replace [regex]::Escape($pattern), $replacement

    # Escribir el contenido actualizado de vuelta al archivo
    Set-Content -Path $file.FullName -Value $newContent

    Write-Host "Actualizado: $($file.FullName)"
}

Write-Host "¡Reemplazo completado!"
