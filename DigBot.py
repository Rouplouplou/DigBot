import tweepy

auth = tweepy.OAuthHandler("L1GkcjE2sOZA2FbSknvozYihc", "KPDu8OCucoFPtk7EibeRZ9KJ1QJP3KPq9gM3wPZs9fvYMBZNjT")
auth.set_access_token("1507613364897341443-UlHBLbWjrX7jGLSIfDarfMxUPkZC8y", "ZMCtDJQ6DLxf7BKwSijkFWKyyn8frVqSWlYBmSkTF4Jrn")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print('yeah')
except:
    print('noo')