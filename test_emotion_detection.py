import unittest
from emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector_joy(self):
        result = emotion_detector("I am so happy today")
        self.assertEqual(result['dominant_emotion'], 'joy')
    
    def test_emotion_detector_anger(self):
        result = emotion_detector("I am really angry about this!")
        self.assertEqual(result['dominant_emotion'], 'anger')
    
    def test_emotion_detector_sadness(self):
        result = emotion_detector("This is so sad")
        self.assertEqual(result['dominant_emotion'], 'sadness')

if __name__ == '__main__':
    unittest.main()
