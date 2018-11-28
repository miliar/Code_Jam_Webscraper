#include <iostream>
#include <string>
using namespace std;

string checkTestCase(string s);

int main() {
  int testCases = 0;
	cin >> testCases;
  string testCasesArr[testCases];
  for(int i = 0; i < testCases; i++) {
    cin >> testCasesArr[i];
  }
  for(int i = 0; i < testCases; i++) {
    string result = checkTestCase(testCasesArr[i]);
		cout << "Case #" << i + 1 << ": " << result << endl;
  }
  return 0;
}

string checkTestCase(string s) {
  int stringLength = s.length();
  string lastGoodNumber(stringLength, '9');
  if(stringLength == 1) {
    return s;
  }
  for(int i = 0; i < stringLength - 1; i++) {
    if(s[i] > s[i + 1]) {
      lastGoodNumber[i] = s[i] - 1;
      if(lastGoodNumber[i] == '0') {
        string eh(stringLength-1, '9');
        return eh;
      }
      return lastGoodNumber;
    } else {
      lastGoodNumber[i] = s[i];
    }
  }
  lastGoodNumber[stringLength-1] = s[stringLength-1];
  return lastGoodNumber;
}
