import base64

# Simulated malicious payload (obfuscated)
data = "U29tZSByZWFsbHkgc3VzcGljaW91cyBlbmNvZGVkIHBheWxvYWQ="

decoded = base64.b64decode(data)
print(decoded)

