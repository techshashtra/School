// Function to open the lightbox
function openLightbox(imgElement) {
    var lightbox = document.getElementById('lightbox');
    var lightboxImg = document.getElementById('lightbox-img');
    
    // Display the image in lightbox
    lightboxImg.src = imgElement.src;
    lightbox.style.display = 'flex';
}

// Function to close the lightbox
function closeLightbox() {
    var lightbox = document.getElementById('lightbox');
    lightbox.style.display = 'none';
}
