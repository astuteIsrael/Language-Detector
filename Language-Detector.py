from langdetect import detect, DetectorFactory

DetectorFactory.seed = 0

text = input("Enter a sentence to detect: ")

detected_language = detect(text)

print(f"The detected language is: {detected_language}")