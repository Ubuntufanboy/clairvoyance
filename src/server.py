from flask import Flask, Response, render_template
import time

app = Flask(__name__)

def event_stream():
    prev = ""
    while True:
        while True:
            time.sleep(1)
            with open("event.txt", 'r') as f:
                data = f.read()
                if data != prev:
                    prev = data
                    break
                
        yield f"data: {data}\n\n"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/events')
def sse():
    return Response(event_stream(), content_type='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)

