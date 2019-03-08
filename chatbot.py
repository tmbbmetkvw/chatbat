
import time
import webbrowser
new=2;

url = "https://www.google.com/search?source=hp&ei=YLOBXNuVOqrZ5gLx8a6QCg&q=pizza+delivery&oq=pizza&gs_l=psy-ab.1.0.35i39j0i67l2j0l7.11184.11818..12510...2.0..0.146.655.1j5......0....1..gws-wiz.....6..0i131j0i20i263.loPt0C-DUv4"


print "hello, I'm Nea.\n I don't think we've met before..."
time.sleep(2)

print "what is your name?"

name = raw_input("> ")
if "Tay" in name:
	print "hey! that's my developer's name! I'll be sure to tell her :)"
else:
	print "hi, %s. " % name

print "now that we've gotten the boring stuff out of the way, tell me...\n ...what's your favorite color?"

color_list = ['blue', 'green', 'purple', 'brown', 'pink', 'black', 'white', 'yellow', 'orange', 'pink', 'red', 'grey', 'magenta', 'aqua']

color = raw_input('> ')

if color in (color_list):
	print "wow, I really like %s, too!" % color
else:
	print "that's a weird color... but that's okay, I forgive you."

time.sleep(1)

#create options for dev info 
print "why are you here?"

here = raw_input('> ')

if "help" in here:
	print "how can I help you, %s?" % name

	assistance = raw_input('> ')
	if "find" in assistance:
		print "have you tried Google.com? I hear that's where you can find anything.."
	elif "lost" in assistance:
		print "well too bad you aren't a computer, I never get lost! :D"
	elif "sad" in assistance:
		print "I'm not sure how to help with that. do you want to talk about it, %s ?" % name
	elif "hungry" in assistance:
		print "would you like to order a pizza?"
		pizza_answer = raw_input("> ")
		if "yes" in pizza_answer:
			print "have you tried using google? here, I'll open it for you..."
			time.sleep(2)
			webbrowser.open(url,new=new) 
	else:
		print "have you tried asking someone smarter than me?"
elif "hungry" in here:
		print "would you like to order a pizza?"
		pizza_answer = raw_input("> ")
		if "yes" in pizza_answer:
			print "have you tried using google? here, I'll open it for you..."
			time.sleep(2)
			webbrowser.open(url,new=new) 


elif "bored" in here:
	print "I'm sorry you're bored %s..do you want to play a game or hear a joke?" % name


elif "you" in here:
	print "well what would you like to know about me?"
	bot_info = raw_input("> ")
	if "age" in bot_info:
		print "I am exactly 'none of your business' years old.."

elif "sad" in here:
	print "okay, tell me more about what's bothering you, %s" % name

else:
	print "well, I'm not sure if I can do that. my developer may not have created that task for me yet. \n would you like to know more about her?"

