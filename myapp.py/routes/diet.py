from flask import Blueprint, request, jsonify

diet_bp = Blueprint('diet', __name__)

@diet_bp.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    calories = data.get('calories')
    nutrient = data.get('nutrient')
    # Dummy logic
    recommendation = {
        "meal": "Rajma Chawal",
        "calories": 420,
        "nutrient": "protein-rich"
    }
    return jsonify(recommendation)
