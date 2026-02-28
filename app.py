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

    elif algorithm == 'selection':
        arr = array.copy()
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            steps.append(arr.copy())

    elif algorithm == 'insertion':
        arr = array.copy()
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j+1] = arr[j]
                j -= 1
                steps.append(arr.copy())
            arr[j+1] = key
            steps.append(arr.copy())

    return jsonify({'steps': steps})

if __name__ == '__main__':
    app.run(debug=True)