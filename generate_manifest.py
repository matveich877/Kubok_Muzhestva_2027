import os
import json

def generate_manifest():
    photos_dir = 'media/photos'
    manifest = []

    if os.path.exists(photos_dir):
        for f in sorted(os.listdir(photos_dir)):
            if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.gif')):
                manifest.append(f)

    manifest_path = os.path.join(photos_dir, 'manifest.json')
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print(f"✅ manifest.json создан: {len(manifest)} фото")
    for f in manifest:
        prefix = "  📦 partner" if f.startswith('partner_') else "  📷"
        print(f"{prefix} {f}")

if __name__ == '__main__':
    generate_manifest()
