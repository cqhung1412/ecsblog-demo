from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return """
          ##         .\n
    ## ## ##        ==\n
 ## ## ## ## ##    ===\n
/\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\___/ ===\n
{                       /  ===-\n
\______ O           __/\n
 \    \         __/\n
  \____\_______/\n
Hello from Docker!
"""

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)