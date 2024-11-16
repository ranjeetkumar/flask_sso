try:
    from authlib.integrations.flask_client import OAuth
    print("Authlib imported successfully!")
except ImportError as e:
    print(f"ImportError: {e}")
