from flask import Flask, request, jsonify
from query import query, init_model, chunk_list, path_list

app = Flask(__name__)

# Initialize the model once
model = init_model()

@app.route('/query', methods=['POST'])
def query_endpoint():
    if request.method == 'POST':
        try:
            data = request.json
            question = data.get('question', None)
            if question is None:
                return jsonify({"error": "Question is missing in the request."}), 400

            # Perform the query using the `query` function from query.py
            related_chunks = query(question)

            response = {
                "question": question,
                "related_chunks": related_chunks
            }

            return jsonify(response)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
