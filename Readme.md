# Film Öneri Sistemi

Bu uygulama, kullanıcıların belirli bir filmle ilgili film önerilerini alabileceği bir Flask web uygulamasıdır. Uygulama, kullanıcıdan bir film adı alır ve o filme benzer diğer filmleri önerir. Film önerileri, bir Film öneri API'sı kullanılarak alınmaktadır. Uygulama, hem film adı, hem de filmle ilgili ek bilgileri (tür, ortalama puan, oy sayısı) sunar.

## Karşılama Ekranı
![Ekran Resmi 2023-07-16 20 09 37](https://github.com/tolgaugurlu/Film-Oneri-Flask/assets/85436268/b5f76099-9c86-4f5b-a74a-64b4c1efe263)

## Benzer Filmler Aratıldıktan Sonra
![Ekran Resmi 2023-07-16 20 11 48](https://github.com/tolgaugurlu/Film-Oneri-Flask/assets/85436268/833329d6-1dd5-4fec-a7ce-c6454608a30b)


## Kurulum

1. Projeyi klonlayın: `git clone https://github.com/yourusername/your-repo-name.git`
2. Python sanal ortamınızı oluşturun ve etkinleştirin: `python3 -m venv venv` ve `source venv/bin/activate`
3. Bağımlılıkları yükleyin: `pip install -r requirements.txt`
4. Uygulamayı çalıştırın: `python app.py`
5. Tarayıcınızı açın ve `http://127.0.0.1:5000/` adresine gidin. Uygulama bu adreste çalışıyor olmalı.

## Kullanım

Uygulamanın ana sayfasında, bir film adı girmek için bir metin kutusu görürsünüz. Bir film adı girin ve "Film Önerilerini Getir" butonuna tıklayın. Ardından, girdiğiniz filme benzer filmlerin bir listesi gösterilir. Her film önerisi için film adı, tür, ortalama puan ve oy sayısı sunulur. Film adı bir IMDB bağlantısına bağlıdır, bu sayede kullanıcılar daha fazla bilgi için IMDB sayfasına kolayca erişebilirler.

## Lisans

Bu proje MIT lisansı altında yayınlanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın.

## Katkı

Bu projeye katkıda bulunmak isterseniz, lütfen önce `CONTRIBUTING.md` dosyasını okuyun.

## İletişim

Sorularınız ve önerileriniz için benimle [email](mailto:tolga97ugurlu@icloud.com) üzerinden iletişime geçebilirsiniz.
