#include <iostream>
#include <string>
using namespace std;

int main() {
  int tt;
  cin >> tt;
  for(int cc=1; cc<=tt; cc++) {
    cout << "Case #" << cc << ": ";

    string n;
    cin >> n;

    for(int i=0; i<n.length()-1; i++) {
      if(n[i] > n[i + 1]) {
        for(int j=i; j>=0; j--) {
          if(n[j] > n[j+1]) {
            n[j + 1] = '9';
            if(n[j] == '0') {
              n[j] = '9';
            }
            else {
              n[j]--;
            }
          }
        }

        // trailing 9s
        for(int j=i+1; j<n.length(); j++) {
          n[j] = '9';
        }

        break;
      }
    }

    if(n[0] == '0') {
      cout << n.substr(1) << endl;
    }
    else {
      cout << n << endl;
    }
  }

  return 0;
}
