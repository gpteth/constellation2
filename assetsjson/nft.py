import os
import json

# 设置 JSON 文件夹路径
json_folder = 'nft_json'  # 存放 JSON 文件的文件夹

# 确保 JSON 文件夹存在
if not os.path.exists(json_folder):
    os.makedirs(json_folder)

# 星座列表，按顺序循环
constellations = [
    "Capricorn", "Aquarius", "Aries", "Leo", "Libra", "Scorpio",
    "Cancer", "Sagittarius", "Pisces", "Virgo", "Gemini", "Taurus"
]

# 开始生成 JSON 文件
for idx in range(3000):
    constellation = constellations[idx % len(constellations)]  # 循环取星座
    
    nft_data = {
        "name": "SCGT",
        "description": "SCGT Constellation",
        "image": f"https://raw.githubusercontent.com/gpteth/constellation2/refs/heads/main/assets/{(idx % 12) + 1}.png",
        "external_url": "https://solana.com/zh",
        "attributes": [
            {
                "trait_type": "constellation",
                "value": constellation
            },
            {
                "trait_type": "trait2",
                "value": "value2"
            }
        ],
        "properties": {
            "files": [
                {
                    "uri": f"https://raw.githubusercontent.com/gpteth/constellation2/refs/heads/main/assets/{(idx % 12) + 1}.png",
                    "type": "image/png"
                }
            ],
            "category": "image"
        }
    }
    
    # 保存 JSON 文件
    json_filename = f"{idx+1}.json"
    json_path = os.path.join(json_folder, json_filename)
    
    with open(json_path, 'w') as json_file:
        json.dump(nft_data, json_file, indent=4)

print(f"✅ 已成功生成 3000 个 NFT JSON 文件！")