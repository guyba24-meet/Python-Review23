def create_youtube_video(title,description):
	youtube_video = {'title':title, 'description':description, 'likes':0, 'dislikes':0, 'comments': {}}
	print("your video has ", youtube_video['likes'], "likes, ", youtube_video['dislikes'], "dislikes, and ", len(youtube_video['comments']), "comments!")

def like():
	if 'likes' in youtube_video:
		youtube_video['likes'] = youtube_video['likes'] + 1
		return youtube_video
	else:
		print('error: video not avilable')

def dislike():
	if 'dislikes' in youtube_video:
		youtube_video['dislikes'] = youtube_video['dislikes'] + 1
		return youtube_video

	else:
		print('error: video not avilable')

def add_comment(comment_text, username):
	if 'comments' in youtube_video:
		username = input("What's Your username?: ")
		comment_text = input("Write your comment: ")
		youtube_video['comments']['username'] = username
		youtube_video['comments']['comment_text'] = comment_text
		return youtube_video

	else:
		print('error: video not avilable')

print("=========================================================================")
print("                                  YouTube                                ")
print("=========================================================================")
print("                                                                         ")
my_title = input("Let's create a new video! What should we call it?: ")
my_discription = input("Enter your discription: ")
create_youtube_video(my_title,my_discription)
while True:
	liking = input("Do you want to like the video? [Y/N] ")
	if liking == "Y":
		like()
	else:
		break
while True:
	disliking = input("Do you want to dislike the video? [Y/N] ")
	if disliking == "Y":
		dislike()
	else:
		break
while True:
	commenting = input("Do you want to add a comment to the video? [Y/N] ")
	if commenting == "Y":
		add_comment()
	else:
		break
print("your video has ", youtube_video['likes'], "likes, ", youtube_video['dislikes'], "dislikes, and ", len(youtube_video['comments'], "comments."))
