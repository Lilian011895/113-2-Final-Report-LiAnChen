mcdonalds_restaurants = [
    {
        'id': 1,
        'name': '麥當勞台中西屯店',
        'address': '台中市西屯區台灣大道三段251號',
        'phone': '04-2451-5678',
        'rating': 4.2,
        'reviews': 156,
        'hours': '24小時營業',
        'services': ['得來速', 'McCafe', '早餐', '宵夜'],
        'image': 'about-1.jpg',
        'lat': 24.1693,
        'lng': 120.6441
    },
    {
        'id': 2,
        'name': '麥當勞逢甲店',
        'address': '台中市西屯區逢甲路20巷16號',
        'phone': '04-2451-2345',
        'rating': 4.5,
        'reviews': 324,
        'hours': '06:00-02:00',
        'services': ['24小時外送', 'McCafe', '學生優惠'],
        'image': 'about-2.jpg',
        'lat': 24.1797,
        'lng': 120.6478
    },
    {
        'id': 3,
        'name': '麥當勞台中火車站店',
        'address': '台中市中區建國路172號',
        'phone': '04-2223-4567',
        'rating': 4.0,
        'reviews': 203,
        'hours': '05:30-24:00',
        'services': ['早餐', '交通便利', 'WiFi'],
        'image': 'about-3.jpg',
        'lat': 24.1369,
        'lng': 120.6857
    },
    {
        'id': 4,
        'name': '麥當勞一中店',
        'address': '台中市北區一中街91號',
        'phone': '04-2225-8901',
        'rating': 4.3,
        'reviews': 278,
        'hours': '07:00-01:00',
        'services': ['學生餐', 'McCafe', '外送'],
        'image': 'about-4.jpg',
        'lat': 24.1485,
        'lng': 120.6812
    }
]

popular_items = [
    {'name': '大麥克', 'price': 72, 'rating': 4.3, 'image': 'menu-1.jpg'},
    {'name': '薯條(大)', 'price': 50, 'rating': 4.6, 'image': 'menu-2.jpg'},
    {'name': '麥克雞塊(10塊)', 'price': 89, 'rating': 4.4, 'image': 'menu-3.jpg'},
    {'name': '可樂(中)', 'price': 25, 'rating': 4.2, 'image': 'menu-4.jpg'},
    {'name': '蘋果派', 'price': 25, 'rating': 4.1, 'image': 'menu-5.jpg'},
    {'name': '冰炫風奧利奧', 'price': 50, 'rating': 4.5, 'image': 'menu-6.jpg'}
]

# 模擬評價資料
sample_reviews = [
    {
        'id': 1,
        'restaurant_id': 1,
        'user_name': '王小明',
        'rating': 5,
        'comment': '服務很快，薯條很酥脆！24小時營業很方便。',
        'date': '2025-06-10'
    },
    {
        'id': 2,
        'restaurant_id': 1,
        'user_name': '李小華',
        'rating': 4,
        'comment': '環境乾淨，但人有點多要排隊。得來速很棒！',
        'date': '2025-06-11'
    },
    {
        'id': 3,
        'restaurant_id': 2,
        'user_name': '張大成',
        'rating': 5,
        'comment': '逢甲店位置超好，學生優惠很實在！',
        'date': '2025-06-12'
    },
    {
        'id': 4,
        'restaurant_id': 2,
        'user_name': '陳美玲',
        'rating': 4,
        'comment': 'McCafe的咖啡不錯，晚上營業到很晚。',
        'date': '2025-06-09'
    }
]
