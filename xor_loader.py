payload = [72, 101, 108, 108, 111]
key = 42

decoded = "".join(chr(b ^ key) for b in payload)
print(decoded)

