# 台中四間麥當勞分店評價網站 🍟

> 一個台中麥當勞分店查詢與評價網站（台中西屯店、逢甲店、台中一中店、台中南屯店）

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3+-green.svg)](https://flask.palletsprojects.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.0-purple.svg)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](#)

## 📋 專案介紹

台中麥當勞分店指南是一個基於 Flask 框架開發的響應式網頁應用程式，專為台中地區的麥當勞愛好者設計。本專案整合了分店資訊查詢、評價系統、營業時間顯示等功能，提供使用者完整的分店資訊服務。

### ✨ 主要功能

- 🏪 **分店瀏覽** - 精選台中地區優質麥當勞分店
- 📍 **詳細資訊** - 地址、電話、營業時間完整顯示
- ⭐ **評價系統** - 真實用戶評價與星級評分
- 🕒 **即時狀態** - 營業時間與當前狀態顯示
- 📱 **響應式設計** - 完美適配手機、平板、電腦
- 🎨 **現代化介面** - 使用 Bootstrap 5 打造美觀 UI

## 🚀 技術架構

### 後端技術
- **Flask 2.3+** - 輕量級 Python 網頁框架
- **Jinja2** - 模板引擎，動態生成 HTML
- **Werkzeug** - WSGI 工具庫

### 前端技術
- **HTML5** - 語義化標記結構
- **CSS3** - 現代化樣式設計
- **Bootstrap 5** - 響應式 UI 框架
- **JavaScript** - 互動功能實現

### 部署環境
- **PythonAnywhere** - 雲端託管平台
- **Git** - 版本控制系統

## 📦 快速開始

### 環境需求
- Python 3.10 或更高版本
- Flask 2.3+
- 現代網頁瀏覽器

### 本地安裝步驟

1. **複製專案**
   ```bash
   git clone https://github.com/Lilian011895/113-2-Final-Report-LiAnChen.git
   cd 113-2-Final-Report-LiAnChen
   ```

2. **安裝依賴套件**
   ```bash
   pip install -r requirements.txt
   ```

3. **啟動應用程式**
   ```bash
   python flask_app.py
   ```

4. **瀏覽網站**
   ```
   開啟瀏覽器前往: http://localhost:5000
   ```

## 📁 專案結構

```
113-2-Final-Report-LiAnChen/
├── flask_app.py              # Flask 主應用程式
├── restaurant_data.py        # 餐廳資料模組
├── requirements.txt          # Python 套件依賴清單
├── README.md                # 專案說明文件
├── templates/               # Jinja2 HTML 模板
│   ├── index.html          # 網站首頁模板
│   ├── restaurant_detail.html # 餐廳詳情頁模板
│   └── disclaimer.html     # 免責聲明頁面
└── static/                 # 靜態資源檔案
    └── css/
        └── style.css       # 自定義 CSS 樣式
```

## 🎯 功能展示

### 首頁特色
- **英雄區塊**: 吸引人的標題與搜尋功能
- **精選分店**: 展示台中地區熱門麥當勞分店
- **特色介紹**: 平台功能與服務說明

### 分店詳情頁
- **基本資訊**: 地址、電話、營業時間
- **設施介紹**: 座位數、停車場、得來速等資訊
- **用戶評價**: 真實評價與評分系統
- **菜單資訊**: 推薦餐點與價格

## 🗂️ 資料結構

### 分店資料格式
```python
{
    "id": 1,
    "name": "台中一中店",
    "address": "台中市北區一中街91號",
    "phone": "04-2225-1234",
    "hours": "06:00-24:00",
    "rating": 4.2,
    "is_24h": False,
    "has_drive_through": True,
    "has_parking": True
}
```

## 🔧 開發特色

### 響應式設計
- 使用 Bootstrap 5 網格系統
- 針對不同螢幕尺寸優化
- 觸控友善的使用者介面

### 資料管理
- 結構化的資料儲存格式
- 易於擴展的資料模型
- 清晰的資料分離架構

### 程式碼品質
- 模組化的程式結構
- 清晰的註解與文件
- 遵循 Python PEP 8 規範

## 📱 瀏覽器支援

- ✅ Chrome 90+
- ✅ Firefox 88+  
- ✅ Safari 14+
- ✅ Edge 90+
- ✅ 手機瀏覽器 (iOS/Android)

## 🚧 未來規劃

- [ ] 地圖整合功能
- [ ] 即時庫存查詢
- [ ] 會員評價系統
- [ ] 多語言支援
- [ ] 行動應用程式

## 📈 專案統計

- **程式語言**: Python 22.5%, HTML 39.9%, CSS 37.6%
- **檔案數量**: 10+ 檔案
- **程式碼行數**: 500+ 行
- **開發時間**: 2025年6月

## 🤝 貢獻指南

歡迎提交問題報告和功能建議！

1. Fork 本專案
2. 建立功能分支 (`git checkout -b feature/新功能`)
3. 提交變更 (`git commit -am '新增某功能'`)
4. 推送到分支 (`git push origin feature/新功能`)
5. 建立 Pull Request

## 📄 授權條款

本專案採用 MIT 授權條款。

## 👨‍💻 作者資訊

**李安真 (LiAnChen)**
- GitHub: [@Lilian011895](https://github.com/Lilian011895)
- 學校: 亞洲大學
- 科系: 資訊工程學系
- 課程: 113-2 期末專題報告

## 🙏 特別感謝

- 感謝授課老師的指導與建議
- 感謝 Flask 開發團隊提供優秀的框架
- 感謝 Bootstrap 團隊提供美觀的 UI 組件
- 感謝 PythonAnywhere 提供免費的託管服務

## 📞 聯絡方式

如有任何問題或建議，歡迎透過以下方式聯絡：
- GitHub Issues: [提交問題](https://github.com/Lilian011895/113-2-Final-Report-LiAnChen/issues)
- Email: [您的學校信箱]

---

⭐ 如果您覺得這個專案有幫助，請給個 Star 支持！

**最後更新**: 2025年6月14日
