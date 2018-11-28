#include <iostream>

using namespace std;

int main() {

  int T;
  cin >> T;
  for (int t=1; t<=T; t++) {
  cout << "Case #" << t << ": ";

  string s;
  cin >> s;

  bool increasing = true;
  for (int i=0; i<s.length() - 1; i++) {
    if (s.at(i) > s.at(i+1)) {
      int j=i;
      while ((j >= 0) && (s.at(j) == s.at(i))) {
        j--;
      }
      j++;
      for (int k=0; k<j; k++) {
        cout << s.at(k);
      }
      char leading = s.at(j) -1;
      if (leading != '0') {
        cout << leading;
      }
      for (int k=j+1; k<s.length(); k++) {
        cout << '9';
      }
      increasing = false;
      break;
    }
  }
  if (increasing) {
    cout << s;
  }
  cout << endl;

  }

}



      


