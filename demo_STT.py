from base64 import encode
import os
#import ffmpeg
from google.cloud import speech
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'fyp-stt-project-key.json'
speech_client = speech.SpeechClient()

main_dir = "C:/Users/jason/OneDrive/FYP project/yellow.mp3"

audio = speech.RecognitionAudio(uri = main_dir)

config = speech.RecognitionConfig(
    encoding = speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz = 48000,
    language_code = "en-US",
)

respone = speech_client.recognize(config = config, audio = audio)

for result in respone.results:
    print("text :" .format(result.alternatives[0].transcript))