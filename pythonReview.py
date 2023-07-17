def create_youtube_video(title, description):
	video = {"title" : title, "description" : description, "likes" : 0 , "comments" : {}, "dislikes" : 0}
	return video

def like(video):
	if ("likes" in video):
		video["likes"] += 1
		return video

def dislike():
	if ("dislikes" in vidoe):
		video["dislikes"] += 1

def add_comment(video, username, comment_text):
	video["comments"][username] = comment_text
	return video

userTitle = input(" enter tittle: ")
userDescription = input("enter description: ")
video = create_youtube_video(userTitle , userDescription)

for i in range(496):
	like(video)
print(video)