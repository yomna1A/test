'''
import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase Admin SDK with the service account key
def init_firebase():
    cred = credentials.Certificate("/home/pi/Downloads/CT_repo_pi_v_5.8_hw_TEST/e2i-mes-firebase-adminsdk-b2iha-69e4542fd3.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://e2i-mes-default-rtdb.firebaseio.com'
    })

# Function to push data to Firebase Realtime Database
def push_to_firebase(speed, availability):
    ref = db.reference('/RealTimeData')  # Reference to the 'data' node in the database
    ref.update({
        'speed': speed * 100,
        'availability': availability
    })
    print("Data sent to Firebase")

# Sample data from your functions
#speed_data = 1 # put here function thet return the speed
#availability_status = 1 # put here function thet return the availability

# Call the function to push the data to Firebase
#push_to_firebase(oee_application.get_SpeedRatio(), oee_availability.get_MachineStatus())
'''