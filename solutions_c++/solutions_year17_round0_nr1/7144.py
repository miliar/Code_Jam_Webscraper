#include <iostream>
#include <string>
using namespace std;

int main() {
  int tt;
  cin >> tt;
  for(int cc=1; cc<=tt; cc++) {
    cout << "Case #" << cc << ": ";

    string s;
    int k;
    cin >> s >> k;

    int flips = 0;
    for(int i=0; i<=s.length()-k; i++) {
      if(s[i] == '-') {
        // flip
        for(int j=0; j<k; j++) {
          if(s[i + j] == '-') {
            s[i + j] = '+';
          }
          else {
            s[i + j] = '-';
          }
        }
        flips++;
      }
    }

    bool possible = true;
    for(int i=s.length()-k+1; i<s.length(); i++) {
      if(s[i] == '-') {
        possible = false;
        break;
      }
    }

    if(possible) {
      cout << flips << endl;
    }
    else {
      cout << "IMPOSSIBLE" << endl;
    }
  }

  return 0;
}
