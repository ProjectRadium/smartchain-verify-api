#/usr/bin/env python
# -*- coding: utf-8 -*-
import requests, json

# Tests
class tests():
    def __init__(self):
        self.score = 0.0
        self.out_of = 0.0
        self.api_url = "http://127.0.0.1:8000/api?url="
        self.to_test = [
            (0, "https://github.com/ProjectRadium/Radium/releases/download/v1.4.2.1/Radium-qt-1.4.2.1.dmg"), # Should pass (Code 0)
            (1, "https://github.com/ProjectRadium/Radium/releases/download/v1.4.2.1/Radium-qt-1.4.2.1.exe"), # Should pass (Code 0)
            (2, "https://github.com/ProjectRadium/Radium/releases/download/v1.4.2.1/radiumd-1.4.2.1.exe"), # Should pass (Code 0)
            (3, "https://github.com/tm2013/Radium/releases/download/v1.4.1.10/Radium-qt-1.4.1.10.dmg"), # Should fail (Code 2)
            (4, "https://github.com/tm2013/Radium/releases/download/v1.4.1.10/Radium-qt-1.4.1.10.exe"), # Should fail (Code 2)
            (5, "https://google"), # Should fail (Code 3)
            (6, "http://www.projectradium.org/downloads/RadiumQuickDeploy_3.17.16.exe") # Should fail (Code 4)
        ]

    # API Tests
    def api_tests(self):
        for url in self.to_test:
            self.out_of += 1
            print("Testing URL #%s..." % (url[0]+1))
            api_data = requests.get("%s%s" % (self.api_url, url[1])).content
            api_data = json.loads(api_data)
            if url[0] <= 2:
                if api_data['code'] == 0:
                    self.score += 1
                    print("passed\n")
                else:
                    print("failed\n")
            if 3 <= url[0] <= 4:
                if api_data['code'] == 2:
                    self.score += 1
                    print("passed\n")
                else:
                    print("failed\n")
            if url[0] == 5:
                if api_data['code'] == 3:
                    self.score += 1
                    print("passed\n")
                else:
                    print("failed\n")
            if url[0] == 6:
                if api_data['code'] == 4:
                    self.score += 1
                    print("passed\n")
                else:
                    print("failed\n")

    # Run All Tests
    def run_all(self):
        self.api_tests()
        print('%s (%s/%s) of tests passed.' % ('{:.1%}'.format(self.score / self.out_of), str(self.score), str(self.out_of))) # Call all tests above this

# Run Tests
if __name__ == '__main__':
    tests().run_all()