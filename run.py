# from PIL import Image

# input_path = "images/pose_estimation_topdown.png"
# output_path = "pose_estimation_topdown.png"

# TARGET_W = 1200
# TARGET_H = 800
# TARGET_RATIO = TARGET_W / TARGET_H  # 1.5

# img = Image.open(input_path).convert("RGB")

# w, h = img.size
# current_ratio = w / h

# # Determine padded canvas size
# if current_ratio > TARGET_RATIO:
#     # Image too wide -> pad height
#     new_w = w
#     new_h = round(w / TARGET_RATIO)
# else:
#     # Image too tall -> pad width
#     new_h = h
#     new_w = round(h * TARGET_RATIO)

# # Create white padded canvas
# canvas = Image.new(
#     "RGB",
#     (new_w, new_h),
#     (255, 255, 255)
# )

# # Center original image
# x = (new_w - w) // 2
# y = (new_h - h) // 2

# canvas.paste(img, (x, y))

# # Resize final image
# canvas = canvas.resize(
#     (TARGET_W, TARGET_H),
#     Image.Resampling.LANCZOS
# )

# canvas.save(output_path, quality=95)

# print(f"Saved: {output_path}")
# print(f"Output size: {canvas.size}")


from PIL import Image

input_path = "images/mocap_recognition.png"
output_path = "mocap_recognition.png"

TARGET_W = 1200
TARGET_H = 800
TARGET_RATIO = TARGET_W / TARGET_H

# Keep alpha channel
img = Image.open(input_path).convert("RGBA")

w, h = img.size
current_ratio = w / h

# Pad to 3:2 ratio
if current_ratio > TARGET_RATIO:
    new_w = w
    new_h = round(w / TARGET_RATIO)
else:
    new_h = h
    new_w = round(h * TARGET_RATIO)

# White RGBA canvas
canvas = Image.new(
    "RGBA",
    (new_w, new_h),
    (255, 255, 255, 255)
)

# Center image
x = (new_w - w) // 2
y = (new_h - h) // 2

# Use alpha channel as mask
canvas.paste(img, (x, y), img)

# Convert AFTER compositing
canvas = canvas.convert("RGB")

# Resize
canvas = canvas.resize(
    (TARGET_W, TARGET_H),
    Image.Resampling.LANCZOS
)

canvas.save(output_path, quality=95)

print(f"Saved: {output_path}")