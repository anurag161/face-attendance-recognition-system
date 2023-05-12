import eel

eel.init('face_attendance')


@eel.expose
def App():
	print('Application Running')


App()

eel.start('main.py', size=(500, 600))
