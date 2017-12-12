import requests
from InstagramAPI import InstagramAPI

'''Get absolute url like per example. convert:
from 'https://www.instagram.com/p/BckYyAXjHD7/?taken-by=juana'
to 'https://instagram.com/p/BckYyAXjHD7''''


def get_absolute_url(url):
    url_array = url.split('/')
    if len(url_array) == 5:
        url_array = url_array[:-1]
    else:
        url_array = url_array
    absolute_url = '/'.join(url_array)
    return absolute_url

# Get media_id, from json request


def get_media_id(url):
    req = requests.get('https://api.instagram.com/oembed/?url={}'.format(url))
    media_id = req.json()['media_id']
    return media_id

def insta_farmer_likers(username, pwd, media_id):
    likers_usernames = []
    API = InstagramAPI(username, pwd)
    API.login()

    request_api = API.getMediaLikers(media_id)

    # get individual users to store 
    for user in API.LastJson['users']:
        likers_usernames.append(user['username'])

    if likers_usernames:
        return likers_usernames
    else:
        print("there is not likers")

def insta_farmer_users_commented(username, pwd, media_id):
    # loging in Instagram 
    API = InstagramAPI(username, pwd)
    API.login()

    request_api = API.getMediaLikers(media_id)

    # get individual users to store
    for user in API.LastJson['users']:
        likers_usernames.append(user['username'])

    if likers_usernames:
        return likers_usernames
    else:
        print("there is not likers")


def insta_farmer_users_commented(username, pwd, media_id):
    # loging in Instagram
    API = InstagramAPI(username, pwd)
    API.login()

    # inicialization bucle
    has_more_comments = True
    comments_usernames = []
    max_id = ''

    # bucle for get all usernames from comments
    while has_more_comments:
        # call all comments
        request_api = API.getMediaComments(mediaId=media_id, max_id=max_id)
        
        for comment in reversed(API.LastJson['comments']):
            # add usernames to comments_usernames
            comments_usernames.append(comment['user']['username'])
        # Ask if is there more comments
        has_more_comments = API.LastJson.get('has_more_comments', False)

        # go to next page
        if has_more_comments:
            max_id = API.LastJson.get('next_max_id', '')
            time.sleep(3)

    if comments_usernames:
        return comments_usernames
    else:
        print("it has not comment")  


if __name__ == '__main__':
    
    #inputs
    username = 'yourusername'
    pwd      = 'yourpassword'
    media_url = 'postURL'
    absolute_url = get_absolute_url(media_url)
    media_id = get_media_id(absolute_url)

    insta_farmer_likers(username, pwd, media_id)
    insta_farmer_users_commented(username, pwd, media_id)
