from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sort', methods=['POST'])
def sort():
    data = request.json
    array = data['array']
    algorithm = data['algorithm']
    steps = []

    if algorithm == 'bubble':
        arr = array.copy()
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                steps.append(arr.copy())

    return jsonify({'steps': steps})

if __name__ == '__main__':
    app.run(debug=True)