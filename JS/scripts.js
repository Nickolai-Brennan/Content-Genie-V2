document.addEventListener('DOMContentLoaded', function() {
    console.log('JavaScript is loaded and ready.');

    // Example: Add functionality to filter feed items
    const searchInput = document.getElementById('search-input');
    const feedItems = document.querySelectorAll('.feed-item');

    searchInput.addEventListener('input', function(event) {
        const searchTerm = event.target.value.toLowerCase();
        feedItems.forEach(item => {
            const title = item.querySelector('.feed-title').textContent.toLowerCase();
            if (title.includes(searchTerm)) {
                item.style.display = '';
            } else {
                item.style.display = 'none';
            }
        });
    });
});