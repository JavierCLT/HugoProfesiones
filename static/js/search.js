document.addEventListener("DOMContentLoaded", function() {
  // Load the search index
  fetch('/search.json')
    .then(response => response.json())
    .then(data => {
      // Initialize Lunr
      const idx = lunr(function () {
        this.ref('href')
        this.field('title')
        this.field('content')
        
        data.forEach(function (doc) {
          this.add(doc)
        }, this)
      })

      // Handle search input with debounce
      const searchBox = document.getElementById('search-box')
      const searchResults = document.getElementById('search-results')
      let debounceTimer

      searchBox.addEventListener('input', function() {
        const query = this.value.trim()

        clearTimeout(debounceTimer)
        debounceTimer = setTimeout(() => {
          if (query.length < 2) {
            searchResults.innerHTML = ''
            return
          }

          const results = idx.search(query)
          let html = ''

          results.forEach(result => {
            const match = data.find(doc => doc.href === result.ref)
            if (match) {
              html += `<div class="search-result">
                        <a href="${match.href}">${match.title}</a>
                      </div>`
            }
          })

          searchResults.innerHTML = html || '<p>No se encontraron resultados.</p>'
        }, 300) // 300ms debounce delay
      })
    })
})
