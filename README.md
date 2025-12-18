# Ex.07 Restaurant Website
# Date:18.12.2025
# AIM:
To develop a static Restaurant website to display the food items and services provided by them.

# DESIGN STEPS:
## Step 1:
Requirement collection.

## Step 2:
Creating the layout using HTML and CSS.

## Step 3:
Updating the sample content.

## Step 4:
Choose the appropriate style and color scheme.

## Step 5:
Validate the layout in various browsers.

## Step 6:
Validate the HTML code.

## Step 7:
Publish the website in the given URL.

# PROGRAM:
```
index.html:
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <title>FRESH FUSION</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>

{% include 'navbar.html' %}

<header>
    <h1>Welcome to Fresh Fusion</h1>
    <p>Fresh Sea Food • Authentic Taste • Best Quality</p>
    <img src="{% static 'images/home.png' %}" class="center-img">
</header>

</body>
</html>

menu.html:
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <title>Menu</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>

{% include 'navbar.html' %}

<h2 align="center">Our Menu</h2>

<div class="menu-grid">

<div class="food-card">
<img src="{% static 'images/gobi.png' %}">
<h3>Gobi Rice</h3>
<p>₹130</p>
</div>

<div class="food-card">
<img src="{% static 'images/ghee.png' %}">
<h3>Ghee Rice</h3>
<p>₹100</p>
</div>

<div class="food-card">
<img src="{% static 'images/ambur biriyani.png' %}">
<h3>Chicken Biriyani</h3>
<p>₹180</p>
</div>

<div class="food-card">
<img src="{% static 'images/fish.png' %}">
<h3>Fish Fry</h3>
<p>₹150</p>
</div>

<div class="food-card">
<img src="{% static 'images/prawn.png' %}">
<h3>Prawn Gravy</h3>
<p>₹200</p>
</div>

</div>

</body>
</html>

contact.html:

{% load static %}
<!DOCTYPE html>
<html>
<head>
    <title>Contact</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>

{% include 'navbar.html' %}

<div class="contact-box">
<h3>Contact Us</h3>
<p>📍 Chennai</p>
<p>📞 9876543210</p>
<p>📧 sandyspoon@gmail.com</p>
</div>

</body>
</html>

about.html:
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <title>About</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body class="about-page">

{% include 'navbar.html' %}

<h2 align="center">About Us</h2>

<img src="{% static 'images/about1.png' %}" class="about-img">
<img src="{% static 'images/about2.png' %}" class="about-img">
<img src="{% static 'images/about3.png' %}" class="about-img">
<img src="{% static 'images/about4.png' %}" class="about-img">

<p align="center">
Sandy Spoon offers traditional and modern sea food with authentic taste.
</p>

adminpage.html:
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <title>Admin</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>

{% include 'navbar.html' %}

<h2 align="center">Admin Panel</h2>

<table>
<tr>
<th>Food</th>
<th>Price</th>
</tr>
<tr><td>Gobi Rice</td><td>₹130</td></tr>
<tr><td>Ghee Rice</td><td>₹140</td></tr>
<tr><td>Ambur Biriyani</td><td>₹180</td></tr>
<tr><td>Fish Fry</td><td>₹130</td></tr>
<tr><td>Prawn Gravy</td><td>₹120</td></tr>
</table>

</body>
</html>

navbar.html:
<nav>
    <a href="/">Home</a>
    <a href="/menu/">Menu</a>
    <a href="/about/">About</a>
    <a href="/contact/">Contact</a>
    <a href="/adminpage/">Admin</a>
</nav>
style.css:
body{
    margin:0;
    font-family: Arial;
    background:#fffaf0;
}

nav{
    background:#7b1e1e;
    padding:12px;
    text-align:center;
}

nav a{
    color:white;
    text-decoration:none;
    margin:15px;
    font-weight:bold;
}

nav a:hover{
    text-decoration:underline;
}

header{
    text-align:center;
    padding:30px;
}

.center-img{
    display:block;
    margin:auto;
    width:80%;
    border-radius:15px;
}

.menu-grid{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(200px,1fr));
    gap:20px;
    padding:20px;
}

.food-card{
    background:white;
    padding:10px;
    border-radius:10px;
    text-align:center;
    box-shadow:0 4px 8px rgba(0,0,0,0.1);
}

.food-card img{
    width:100%;
    height:150px;
    object-fit:cover;
    border-radius:10px;
}

.about-page{
    background-image:url("/static/images/bg.jpg");
    background-size:cover;
    min-height:100vh;
}

.about-img{
    width:50%;
    display:block;
    margin:auto;
    border-radius:15px;
}

.contact-box{
    width:50%;
    margin:40px auto;
    background:white;
    padding:20px;
    border-radius:10px;
}

table{
    width:60%;
    margin:auto;
    border-collapse:collapse;
}

table, th, td{
    border:1px solid #ccc;
    padding:10px;
}

th{
    background:#7b1e1e;
    color:white;
}


```
# OUTPUT:
![alt text](<Screenshot (34).png>)
![alt text](<Screenshot (35).png>)
![alt text](<Screenshot (36).png>)
![alt text](<Screenshot (37).png>)
![alt text](<Screenshot (38).png>)

# RESULT:
The program for designing software company website using HTML and CSS is completed successfully.
