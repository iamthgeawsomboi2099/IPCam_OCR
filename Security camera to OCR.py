#Importing Necessary Libraries
import cv2
import pytesseract

# Initialize the camera capture
camera_url = ''                                                 #Enter The IP Of the Security Camera Along with the port in the format
cap = cv2.VideoCapture(camera_url)                              # rtsp://(username):(Password)@(ip of Camera):(Port)/(File Path of Stream)

# Initialize extracted data list
extracted_data = []

# Function to extract text from frame
def extract_text_from_frame(frame):
    text = pytesseract.image_to_string(frame)
    return text

# Capture and process frames
try:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        text = extract_text_from_frame(frame)
        extracted_data.append(text)

        cv2.imshow('Camera Feed', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    print("Text extraction success")
except Exception as e:
    print("Error during text extraction:", e)

# Release the camera capture
cap.release()
cv2.destroyAllWindows()

# Save extracted data to a text file
output_file_path = '' #Enter File path to where tthe extracted data needs to be saved 

try:
    with open(output_file_path, 'w') as output_file:
        for item in extracted_data:
            output_file.write("%s\n" % item)
    print("Data saved to", output_file_path)
except Exception as e:
    print("Error during data saving:", e)
    