import os
import shutil
import time

def convert_files(input_dir, output_dir):
    # Input ve Output dizinlerinin varlığını kontrol edin
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Sıralı numara için sayaç
    counter = 0
    
    # Input dizinindeki dosyaları tarayın
    for filename in os.listdir(input_dir):
        file_path = os.path.join(input_dir, filename)
        
        # Sadece dosyaları işleme alın
        if os.path.isfile(file_path):
            # Dosya uzantısını kontrol edin
            if filename.endswith('.0'):
                # Yeni dosya adını oluşturun
                new_filename = f"{counter:04}.jpg"
                new_file_path = os.path.join(output_dir, new_filename)
                
                # Dosyayı Output dizinine taşıyın ve yeniden adlandırın
                shutil.move(file_path, new_file_path)
                print(f"Dosya taşındı ve yeniden adlandırıldı: {new_file_path}")
                
                # Sayaç artırılır
                counter += 1

                # 1 saniye bekle
                time.sleep(0.5)

# Klasör yollarını belirleyin
input_dir = 'input'
output_dir = 'output'

# Fonksiyonu çağırın
convert_files(input_dir, output_dir)