#include <bits/stdc++.h>

using namespace std;

int main() {
  char res[1001];
  int T;
  cin >> T;

  for(int caso = 1; caso <= T; caso++) {
    int N, R, O, Y, G, B, V;
    cin >> N >> R >> O >> Y >> G >> B >> V;

    memset(res, 0, sizeof(res));

    int M = R;
    char chosen = 'R';
    if(Y > M) {
      M = Y;
      chosen = 'Y';
    }
    if(B > M) {
      M = B;
      chosen = 'B';
    }

    int cur = 0;
    bool possible = true;

    for(int i = 0; i < M; i++) {
      if(cur >= N) {
        possible = false;
        break;
      }
      res[cur] = chosen;
      cur += 2;
    }

    if(possible) {
      if(chosen == 'R') R = 0;
      if(chosen == 'Y') Y = 0;
      if(chosen == 'B') B = 0;

      M = R;
      chosen = 'R';
      if(Y > M) {
        M = Y;
        chosen = 'Y';
      }
      if(B > M) {
        M = B;
        chosen = 'B';
      }
      cur = N-1;
      for(int i = 0; i < M; i++) {
        if(cur < 0) {
          possible = false;
          break;
        }
        if(res[cur] == 0){
          res[cur] = chosen;
          cur--;
        } else {
          i--;
        }
        cur--;
      }

      if(possible) {
        if(chosen == 'R') R = 0;
        if(chosen == 'Y') Y = 0;
        if(chosen == 'B') B = 0;
        M = R;
        chosen = 'R';
        if(Y > M) {
          M = Y;
          chosen = 'Y';
        }
        if(B > M) {
          M = B;
          chosen = 'B';
        }

        cur = N-1;
        for(int i = 0; i < M; i++) {
          if(cur < 0) {
            possible = false;
            break;
          }
          if(res[cur] == 0)
            res[cur] = chosen;
          else i--;
          cur--;
        }
      }
    }

    possible = possible && res[0] != res[N-1];

    if(possible) {
      cout << "Case #" << caso << ": " << res << endl;
    } else {
      cout << "Case #" << caso << ": IMPOSSIBLE" << endl;
    }

  }

  return 0;
}
