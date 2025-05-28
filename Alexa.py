/* Basic Reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body Styling */
body {
    font-family: 'Roboto', sans-serif;
    line-height: 1.7;
    background-color: #f8f9fa;
    color: #333;
    text-rendering: optimizeLegibility;
    scroll-behavior: smooth;
}

/* Center Utility */
.center {
    text-align: center;
    margin-top: 40px;
}

/* Header */
.logo {
    width: 150px;
    margin: 20px auto;
    display: block;
}

/* Navigation Bar */
.navbar {
    background-color: #0d6efd;
    padding: 12px 20px;
    display: flex;
    justify-content: center;
    gap: 25px;
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
}

.nav-link {
    font-size: 18px;
    color: white;
    padding: 12px 18px;
    text-decoration: none;
    border-radius: 6px;
    transition: background-color 0.3s ease, transform 0.3s ease;
}

.nav-link:hover {
    background-color: rgba(13, 110, 253, 0.85);
    transform: translateY(-3px);
}

/* Main Image */
.main-image {
    width: 90%;
    max-width: 1200px;
    margin: 20px auto;
    border-radius: 12px;
    display: block;
    box-shadow: 0px 6px 10px rgba(0, 0, 0, 0.15);
}

/* Description Text */
.description {
    font-size: 20px;
    line-height: 1.8;
    margin: 30px auto;
    width: 80%;
    max-width: 1000px;
    text-align: justify;
}

/* Button */
.button {
    font-size: 17px;
    background-color: #0d6efd;
    color: white;
    padding: 12px 24px;
    text-decoration: none;
    border-radius: 6px;
    transition: background-color 0.3s ease, transform 0.3s ease;
    display: inline-block;
}

.button:hover {
    background-color: rgba(13, 110, 253, 0.85);
    transform: scale(1.08);
}

/* Gallery */
.gallery {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 25px;
    margin: 50px auto;
    padding: 10px;
}

.gallery-img {
    width: 30%;
    max-width: 300px;
    border-radius: 10px;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    cursor: pointer;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
}

.gallery-img:hover {
    transform: scale(1.1);
    box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.3);
}

/* Lightbox */
.lightbox {
    display: none;
    position: fixed;
    z-index: 1000;
    padding: 50px;
    background-color: rgba(0, 0, 0, 0.9);
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    justify-content: center;
    align-items: center;
    transition: opacity 0.3s ease;
}

.lightbox-content {
    max-width: 80%;
    max-height: 80%;
    border-radius: 10px;
}

.close {
    position: absolute;
    top: 20px;
    right: 30px;
    color: white;
    font-size: 40px;
    font-weight: bold;
    cursor: pointer;
}

/* Video Section */
.video {
    width: 70%;
    max-width: 800px;
    margin: 30px auto;
    border-radius: 10px;
    display: block;
    box-shadow: 0px 5px 12px rgba(0, 0, 0, 0.2);
}

/* Footer */
footer {
    margin-top: 50px;
    padding: 25px;
    background-color: #343a40;
    color: #fff;
    text-align: center;
    font-size: 16px;
}
