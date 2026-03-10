import os

slides = sorted(os.listdir("slides"))

slides_html = ""

for slide in slides:
    slides_html += f"<section><img src='slides/{slide}' style='width:100%'></section>\n"

html = f"""
<!doctype html>
<html>

<head>
<meta charset="utf-8">

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js/dist/reveal.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js/dist/theme/black.css">

</head>

<body>

<div class="reveal">
<div class="slides">

{slides_html}

</div>
</div>

<script src="https://cdn.jsdelivr.net/npm/reveal.js/dist/reveal.js"></script>

<script>
Reveal.initialize();
</script>

</body>

</html>
"""

with open("index.html", "w") as f:
    f.write(html)
