def create_youtube_video(title, description):
	video = {"title" : title, "description" : description, "likes" : 0 , "comments" : {}, "dislikes" : 0}
	return video

def like(video):
	if ("likes" in video):
		video["likes"] += 1
		return video

def dislike(video):
	if ("dislikes" in video):
		video["dislikes"] += 1
		return video

def add_comment(video, username, comment_text):
	video["comments"][username] = comment_text
	return video

userTitle = input(" enter tittle: ")
userDescription = input("enter description: ")
video = create_youtube_video(userTitle , userDescription)
username = input("enter username: ")
comment_text = input("entetr a comment: ")
print(dislike(video))
print(add_comment(video, username, comment_text))
for i in range(496):
	like(video)
print(add_comment(video,'Ali','Kbeeer' ))
print(video)