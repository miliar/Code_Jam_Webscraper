#include <iostream>
#include <stack>
#include <queue>
using namespace std;

int main() {
  int t;

  cin >> t;

  for( int z = 1; z <= t; z++ ) {
    string s;
    int k;
    queue<string> pan;
    queue<int> pos;
    queue<int> cnt;
    cin >> s >> k;

    pan.push(s);
    pos.push(-1);
    cnt.push(0);

    bool success = false;

    while ( pan.size() != 0 ) {
      string pa = pan.front();
      int cn = cnt.front();
      pan.pop();
      cnt.pop();
      if ( cn > pa.size() * 2 ) continue;

      queue<int> startPoint;

      bool t = true;

      for (int i = 0;  i <= (pa.size() - k) ; i++) {
        if ( pa[i] == '-' ) {
          startPoint.push(i);
          t = false;
        }
      }

      if ( t ) {
        bool f = false;
        for ( int i = 0; i < pa.size(); i++ ) {
          if ( pa[i] == '-' ) {
            f = true;
            break;
          }
        }

        if ( f ) continue;
        else {
          cout << "Case #" << z << ": " << cn << endl;
          success = true;
          break;
        }
      }


      while ( startPoint.size() != 0 ) {
        int start = startPoint.front();
        startPoint.pop();

        string tmp = pa;
        for (int i = start; i < (start + k); i++) {
          if ( tmp[i] == '+' ) {
            tmp[i] = '-';
          } else {
            tmp[i] = '+';
          }
        }

        pan.push(tmp);
        cnt.push(++cn);
      }
    }

    if ( !success ) {
      cout << "Case #" << z << ": " << "IMPOSSIBLE" << endl;
    }
  }

  return 0;
}