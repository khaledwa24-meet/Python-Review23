def create_youtube_video(title, description):
	dic = {"title" : title, "description" : description, "likes" : 0 , "comments" : {}, "dislikes" : 0}
	return dic

def like(video):
	if ("likes" in video):
		vidoe["likes"] += 1
		return video

def dislike():
	if ("dislikes" in vidoe):
		video["dislikes"] += 1

def add_comment():








video = create_youtube_video(userTitle = input(" enter tittle"), userDescription = input("enter description") )