from flask import Flask, redirect, url_for, session
from authlib.integrations.flask_client import OAuth
import os
from dotenv import load_dotenv
import uuid

# Load environment variables from .env file
load_dotenv()

# Flask app setup
app = Flask(__name__)
app.secret_key = os.urandom(24)  # Use a strong random secret key
app.config['GOOGLE_CLIENT_ID'] = os.getenv('GOOGLE_CLIENT_ID')  # Get Google Client ID from .env
app.config['GOOGLE_CLIENT_SECRET'] = os.getenv('GOOGLE_CLIENT_SECRET')  # Get Google Client Secret from .env
app.config['GOOGLE_DISCOVERY_URL'] = "https://accounts.google.com/.well-known/openid-configuration"

# OAuth setup
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id=app.config['GOOGLE_CLIENT_ID'],
    client_secret=app.config['GOOGLE_CLIENT_SECRET'],
    server_metadata_url=app.config['GOOGLE_DISCOVERY_URL'],
    client_kwargs={
        'scope': 'openid email profile',
    },
)

@app.route('/')
def index():
    """Homepage."""
    return 'Welcome! <a href="/login">Login with Google</a>'

@app.route('/login')
def login():
    """Redirect to Google's OAuth page."""
    # Generate a random nonce
    nonce = str(uuid.uuid4())
    session['nonce'] = nonce  # Store nonce in session for later validation

    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri, nonce=nonce)  # Pass nonce in redirect

@app.route('/oauth2callback')
def authorize():
    """Handle the callback from Google."""
    # Retrieve the nonce stored in session
    nonce = session.get('nonce')

    # Fetch the token and parse the ID token, passing the nonce
    token = google.authorize_access_token()
    user_info = google.parse_id_token(token, nonce=nonce)  # Include nonce in parsing

    return f'Logged in as: {user_info["email"]}'

if __name__ == '__main__':
    app.run(debug=True)


