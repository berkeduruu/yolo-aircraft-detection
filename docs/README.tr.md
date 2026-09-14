# YOLO Aircraft Detection — Türkçe kısa rehber

Bu repo, sabit kanatlı uçak tespiti için YOLOv11 eğitim, inference, ROI ve TensorRT export araçlarını içerir.

Hızlı başlangıç için sanal ortam oluşturup `pip install -r requirements.txt` çalıştırın. Dahil olan `models/N_new720p.pt` veya `models/S_new720p.pt` ağırlığını kullanarak ilgili inference scriptindeki giriş/çıkış yollarını güncelleyin.

Dataset akışı: [Video Frame Grabber](https://github.com/berkeduruu/Video-Frame-Grabber) ile frame çıkarın → [YOLO Annotation Tool](https://github.com/berkeduruu/yolo-annotation-tool) ile etiketleyin → notebook ile eğitin. Jetson deployment için [DeepStream pipeline reposuna](https://github.com/berkeduruu/jetson-deepstream-yolo-pipelines) bakın.
