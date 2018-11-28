#include <iostream>
#include <algorithm>
using namespace std;

string solve() {
  int N;
  cin >> N;
  int R,B,Y,O,G,V;
  int a[3];
  string s = "";
  cin >> a[0] >> O >> a[1] >> G >> a[2] >> V;
  int prev = -1;
  for(int i = 0;i<N;i++) {
    switch (prev) {
      case -1:
        if(a[0]) {
          a[0]--;
          s += "R";
        }
        else if(a[1]) {
          a[1]--;
          s+= "Y";
        }
        else if(a[2]) {
          a[2]--;
          s+="B";
        }
        break;
      case 0: // R
        if(a[1]>=a[2]) {
          if(a[1]) {
            a[1]--;
            s+="Y";
          }
          else
            return "IMPOSSIBLE";
        }
        else {
          if(a[2]) {
            a[2]--;
            s+="B";
          }
          else
            return "IMPOSSIBLE";
        }
        break;
        case 1: // R
          if(a[0]>=a[2]) {
            if(a[0]) {
              a[0]--;
              s+="R";
            }
            else
              return "IMPOSSIBLE";
          }
          else {
            if(a[2]) {
              a[2]--;
              s+="B";
            }
            else
              return "IMPOSSIBLE";
          }
          break;
          case 2: // R
            if(a[0]>=a[1]) {
              if(a[0]) {
                a[0]--;
                s+="R";
              }
              else
                return "IMPOSSIBLE";
            }
            else {
              if(a[1]) {
                a[1]--;
                s+="Y";
              }
              else
                return "IMPOSSIBLE";
            }
            break;
    }
    if(s[i] == 'R')
      prev = 0;
    else  if(s[i] == 'Y')
        prev = 1;
    else
      prev = 2;

  }
  if(s[N-1] == s[0])
    return "IMPOSSIBLE";
  return s;
}

int main() {
  int T;
  cin >> T;
  for(int i = 1;i<=T;i++) {
    cout << "Case #" << i << ": ";
    cout << solve();
    cout << endl;
  }
}
