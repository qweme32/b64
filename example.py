from b64 import B64

print(B64.decode(B64.encode("Hello world!")))

simple_text = "Hello world!"
b64_steps = 16

b64_res = B64.encode(simple_text, b64_steps)

print("Encoded:", b64_res)
print("Encoded len:", len(b64_res))
print("Decoded:", B64.decode(b64_res, b64_steps))