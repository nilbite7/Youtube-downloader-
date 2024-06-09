from flask import Flask, request, send_file
import cv2
import numpy as np
import io

app = Flask(__name__)

@app.route('/enhance', methods=['POST'])
def enhance_image():
    file = request.files['file']
    img = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_COLOR)

    # Apply sharpness filter
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    img = cv2.filter2D(img, -1, kernel)

    # Encode processed image to bytes
    _, buffer = cv2.imencode('.jpg', img)
    return send_file(io.BytesIO(buffer), mimetype='image/jpeg', as_attachment=True, attachment_filename='enhanced.jpg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
