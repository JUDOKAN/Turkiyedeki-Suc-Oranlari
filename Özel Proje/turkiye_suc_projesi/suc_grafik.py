import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_turkey_crime_stats(csv_path, save_path="grafikler/turkiye_suc_oranlari.png"):
    """
    Türkiye'deki yıllık suç oranlarını çizgi grafiği olarak oluşturur ve kaydeder.
    :param csv_path: CSV dosyasının yolu
    :param save_path: Grafik kaydedilecek yol
    :return: Kaydedilen grafik dosyasının adı
    """
    df = pd.read_csv(csv_path)

    plt.figure(figsize=(12, 7))

    plt.plot(df["Yıl"], df["Cinayet"], marker="o", label="Cinayet", color="red")
    plt.plot(df["Yıl"], df["Hırsızlık"], marker="o", label="Hırsızlık", color="blue")
    plt.plot(df["Yıl"], df["Dolandırıcılık"], marker="o", label="Dolandırıcılık", color="green")

    plt.title("Türkiye'de Yıllara Göre Suç Oranları")
    plt.xlabel("Yıl")
    plt.ylabel("Vaka Sayısı")
    plt.legend()
    plt.grid(True)

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

    return save_path

# Test etmek için:
if __name__ == "__main__":
    dosya = plot_turkey_crime_stats("turkiye_suc_oranlari.csv")
    print("Grafik başarıyla kaydedildi:", dosya)
