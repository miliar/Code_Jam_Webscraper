#include <iostream>
using namespace std;

int checkTestCase(string s, int n);

int main() {
  int testCases = 0;
	cin >> testCases;
  string testCasesArr[testCases];
  int flipperLength[testCases];
  for(int i = 0; i < testCases; i++) {
    cin >> testCasesArr[i];
    cin >> flipperLength[i];
  }

  for(int i = 0; i < testCases; i++) {
		int result = checkTestCase(testCasesArr[i], flipperLength[i]);
    if(result != -1) {
		  cout << "Case #" << i + 1 << ": " << result << endl;
    } else {
		  cout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
    }
  }
  return 0;
}

int checkTestCase(string s, int n) {
  int count = 0;
  for(int i = 0; i < s.length(); i++) {
    if(s[i] == '-') {
      for(int j = 0; j < n; j++) {
        if(i + j == s.length()) {
          return -1;
        } else {
          if(s[i + j] == '-') {
            s[i + j] = '+';
          } else {
            s[i + j] = '-';
          }
        }
      }
      count++;
    }
  }
  return count;
}
