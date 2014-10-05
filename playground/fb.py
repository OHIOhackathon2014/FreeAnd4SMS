import facebook
import sys
import os
import os.path
import json
import time


oauth_access_token = "CAACEdEose0cBAPLqZBKGTVF9hKfL1RgR7XUTgH8przxyfzqq5rtYLW00VDLBZBg6m3EirQwadtIKZATZBrZApQm9HZBYaac7R4qWcMxRLb3KtYdMeLhs0l84zKu8i46AsAdgSSjxLHLwlcZCUniEjnXjq69eUo8HxJ24TNNmNHZAZBCzTeoSuyOZBsm3CJeZBQZBLGVBLHxIYEHTWCqZC5gapjSLQ"

def main():
    graph = facebook.GraphAPI(oauth_access_token)
    #profile = graph.get_object("me")
    args = {'fields' : 'id,type,created_time,message,object_id,link'}
    posts_dump = graph.get_object("344403585620607/feed", **args)#?fields=id,type,message,object_id,link")
    #friends = graph.get_connections("344403585620607", "feed?fields=message")
    #write_to_file(friends,'group-feed.json')
    write_to_file(posts_dump,'posts.json')
    #write_to_file(profile,'me.json')

    #print profile
    #print friends

def write_to_file(data, filename):
    #Converts to json and dumps the contents to a file
    with open(filename, 'w') as outfile:
        #Removing non-unicode characters from the dataset
        #self.parsed_data = unicode(self.parsed_data, errors='ignore')
        json.dump(data, outfile, indent=4)
        outfile.close()



if __name__ == "__main__": main()
