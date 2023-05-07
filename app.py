from flask import Flask, render_template

app = Flask('__main__')

@app.route('/')
def main():
    return render_template('main.html')

if __name__ == '__main__':
    app.run()