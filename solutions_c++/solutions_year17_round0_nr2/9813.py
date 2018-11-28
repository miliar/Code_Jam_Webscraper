#include <iostream>

using namespace std;

bool isGood(const string& s) {
  for (int i=0;i<(int)s.length()-1;i++) {
    if (s[i] > s[i+1]) {
      return false;
    }
  }

  return true;
}

int main()
{
  int t;
  cin >> t;
  int count = 0;
  while (t-->0) {
    string s;
    cin >> s;

    while(true) {
      if (isGood(s)) {
        break;
      }

      for (int i = (int)s.length() -2 ; i>=0;i--) {
        if (s[i] > s[i-1]) {
          s[i]--;
          for (int j=i+1;j<(int)s.length();j++) {
            s[j] = '9';
          }
          break;
        }
      }
    }

    // Delete all prefix 0's.
    while(true) {
      int finder = s.find('0');
      if (finder == 0) {
        s.erase(0,1);
        continue;
      }
      break;
    }

    cout << "Case #" << ++count <<": " << s << endl;
  }
}
