# فتح ملف CSS
F = open("index.css", "w")

# تعريف محتوى CSS
css = """
body {
    background-color: black;
}
"""

# كتابة CSS إلى الملف
F.write(css)

# إغلاق الملف
F.close()
