from flask import Flask, render_template, request, jsonify
import learning_algos

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('/templates/learning_recommendation.html')

@app.route('/run_script', methods=['POST'])
def run_script():
    try:
        data = request.json 
        
        user_query = "B.Tech Computers Student Data Scientist"
        recommendations = learning_algos.recommend_courses(user_query, top_n=5)        
        #result = my_script_file.my_function(data) 
        
        return jsonify({"success": True, "message": recommendations})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})

if __name__ == '__main__':
    app.run(debug=True)

