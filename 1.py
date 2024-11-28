F = open("index.html", "w")

# تعريف محتوى ملف HTML
html = """
<html>
<head>
    <title>طريق الهداية للعلوم الشرعية</title>
    <link rel="stylesheet" href="index.css">
</head>

<body>
 <center>
 <h1>قناة طريق الهداية للعلوم الشرعية</h1>
 <hr>
 <h2>تقريب العلوم الشرعية</h2>

 </center>
</body>
</html>
"""

# كتابة محتوى HTML إلى الملف
F.write(html)

# إغلاق الملف
F.close()
