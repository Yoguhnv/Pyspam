import webbrowser

# Açılacak URL
url = "https://www.google.com"

# 100 kez yeni bir sekme aç
for i in range(990):
    webbrowser.open_new_tab(url)
