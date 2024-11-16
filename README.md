
# Flask Google OAuth Authentication

This project implements Google OAuth 2.0 authentication in a Flask application, allowing users to log in using their Google accounts.

---

## Features

- **User authentication** using Google OAuth 2.0.
- Secure token handling and user data retrieval.
- Reads sensitive credentials (e.g., client ID and secret) from a `.env` file.
- Flask route handlers for login and user information display.

---

## Call Sequence

Below is a step-by-step overview of how the Google OAuth 2.0 flow works in this application:

1. **Visit `/`**  
   - The user accesses the homepage of the Flask app.  
   - The app displays a "Login with Google" button.

2. **Click "Login with Google"**  
   - The user clicks the login button.  
   - The app redirects the user to Google's OAuth 2.0 authorization page.

3. **Redirect to Google OAuth Authorization URL**  
   - The app specifies the required scopes (e.g., email, profile) and sends the user to Google's authorization server.

4. **User Logs In and Grants Permissions**  
   - The user logs in to their Google account and grants the requested permissions to the app.

5. **Redirect Back to `/oauth2callback`**  
   - After successful authentication, Google redirects the user back to the Flask app's `/oauth2callback` route with an authorization code.

6. **Exchange Authorization Code for Tokens**  
   - The Flask app sends the authorization code to Google.  
   - Google responds with an access token and an ID token.

7. **Parse the ID Token**  
   - The app parses the ID token to retrieve the user's email, name, and other profile information.

8. **Display User Info**  
   - The app displays the logged-in user's information (e.g., email, name) on the webpage.

**Set Up Google OAuth Credentials**
- Create a project in the Google Cloud Console.
- Enable the OAuth consent screen.
- Configure an OAuth 2.0 Client ID:
- Authorized redirect URI: http://localhost:5000/oauth2callback
- Save your credentials (Client ID and Client Secret).

