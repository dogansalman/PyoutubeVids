import os
import json
import googleapiclient.discovery
import googleapiclient.errors
import google_auth_oauthlib.flow
import youtube_dl
scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
path = 'temp'

list_id = input("Please insert list id: ")
authtype = input("Are you want to use OAuth Y/N: ")

def main():
   
   
    if authtype.lower() == 'y':
        WithOauth()
    else:
        username = input("username: ")
        password = input("password: ")
        os.system("""cmd /c youtube-dl --username {0} --password {1} --extract-audio --audio-format mp3 -o "temp/%(title)s.%(ext)s" https://www.youtube.com/playlist?list={2}""".format(username, password, list_id))
	

def WithOauth():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "./secret.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)


    # Request playlist
    request = youtube.playlistItems().list(
        part="snippet,contentDetails",
        maxResults=50, #result max video content lenght
        playlistId= list_id
    )
    response = request.execute()

    # save playlist results
    with open("result.json", 'w') as outfile:  
        json.dump(response, outfile)

    # read results save vid
    with open("result.json") as json_file:  
        data = json.load(json_file)
    for i in data["items"]:
        saveToVids(i["contentDetails"]["videoId"])


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

def saveToVids(vidId):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '/temp/%(title)s-%(id)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'progress_hooks': [my_hook],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(["https://www.youtube.com/watch?v={}".format(vidId)])

if __name__ == "__main__":
    main()
