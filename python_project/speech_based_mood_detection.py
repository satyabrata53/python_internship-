import pyaudio
import wave
import speech_recognition as sr
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

def record_audio(filename, duration=5):
    chunk = 1024
    sample_format = pyaudio.paInt16
    channels = 1
    fs = 44100

    p = pyaudio.PyAudio()
    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)
    
    print("Recording...")
    frames = []

    for _ in range(0, int(fs / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)
    
    print("Finished recording.")
    
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()

def transcribe_audio(filename):
    recognizer = sr.Recognizer()
    audio_file = sr.AudioFile(filename)
    
    with audio_file as source:
        audio_data = recognizer.record(source)
    
    try:
        text = recognizer.recognize_google(audio_data)
        print("Transcription: " + text)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def detect_mood(text):
    nltk.download('vader_lexicon')
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)
    
    print("Sentiment Analysis:", sentiment)
    
    if sentiment['compound'] >= 0.05:
        return "Positive"
    elif sentiment['compound'] <= -0.05:
        return "Negative"
    else:
        return "Neutral"

if __name__ == "__main__":
    filename = "output.wav"
    record_audio(filename, duration=5)
    transcribed_text = transcribe_audio(filename)
    
    if transcribed_text:
        mood = detect_mood(transcribed_text)
        print("Detected Mood:", mood)
