from flask import Flask, render_template, request, redirect, url_for
from detailed_data import detailed_restaurants, complete_menu, sample_reviews
from datetime import datetime

app = Flask(__name__)

reviews = sample_reviews.copy()

@app.route("/")
def index():
    # 首頁只顯示前兩家作為精選
    featured_restaurants = detailed_restaurants[:2]
    
    # 簡化熱門商品，避免複雜的結構問題
    popular_items = [
        {
            "name": "大麥克",
            "price": 75,
            "description": "經典雙層牛肉漢堡",
            "rating": 4.5,
            "image": "menu-1.jpg"
        },
        {
            "name": "麥克雞塊",
            "price": 55,
            "description": "酥脆雞塊，外酥內嫩",
            "rating": 4.3,
            "image": "menu-2.jpg"
        },
        {
            "name": "薯條",
            "price": 35,
            "description": "金黃酥脆薯條",
            "rating": 4.6,
            "image": "menu-3.jpg"
        },
        {
            "name": "可樂",
            "price": 25,
            "description": "冰涼可口可樂",
            "rating": 4.2,
            "image": "menu-4.jpg"
        }
    ]
    
    return render_template("index.html", restaurants=featured_restaurants, popular_items=popular_items)

@app.route("/restaurants")
def restaurants():
    # 支援多種搜尋參數名稱
    search = request.args.get("search", "") or request.args.get("q", "")
    filtered_restaurants = detailed_restaurants
    
    if search:
        search_lower = search.lower()
        filtered_restaurants = [
            r for r in detailed_restaurants 
            if search_lower in r["name"].lower() 
            or search_lower in r["address"].lower()
            or any(search_lower in service["name"].lower() for service in r.get("services", []))
        ]
        print(f"搜尋關鍵字: '{search}', 找到 {len(filtered_restaurants)} 家餐廳")
    
    return render_template("restaurants.html", restaurants=filtered_restaurants, search=search)

@app.route("/restaurant/<int:restaurant_id>")
def restaurant_detail(restaurant_id):
    restaurant = next((r for r in detailed_restaurants if r["id"] == restaurant_id), None)
    if restaurant:
        restaurant_reviews = [r for r in reviews if r["restaurant_id"] == restaurant_id]
        if restaurant_reviews:
            avg_rating = sum(r["rating"] for r in restaurant_reviews) / len(restaurant_reviews)
            restaurant["avg_rating"] = round(avg_rating, 1)
        else:
            restaurant["avg_rating"] = restaurant["rating"]
        return render_template("restaurant_detail.html", restaurant=restaurant, reviews=restaurant_reviews)
    return "餐廳未找到", 404

@app.route("/add_review/<int:restaurant_id>", methods=["POST"])
def add_review(restaurant_id):
    if request.method == "POST":
        new_review = {
            "id": len(reviews) + 1,
            "restaurant_id": restaurant_id,
            "user_name": request.form.get("user_name", "匿名用戶"),
            "rating": int(request.form.get("rating", 5)),
            "comment": request.form.get("comment", ""),
            "date": datetime.now().strftime("%Y-%m-%d"),
            "helpful_count": 0
        }
        reviews.append(new_review)
    return redirect(url_for("restaurant_detail", restaurant_id=restaurant_id))

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/disclaimer')
def disclaimer():
    return render_template('disclaimer.html')

@app.route('/search')
def search():
    return "搜尋功能開發中"

@app.route('/about')
def about():
    return "關於我們頁面開發中"
