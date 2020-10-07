import time 
from plyer import notification 


if __name__=="__main__": 

		notification.notify( 
			title = "Hello Mayank Biswas , You are selected as a campus ambassador.", 
			message=" Coffee Hours Club is one of the great communities in India " ,
            app_icon = r'C:\Users\LENOVO\Documents\drink\Custom-Icon-Design-Mono-Business-2-Coffee.ico',
			
			timeout = 5
) 
		# waiting time 
		time.sleep(7)

