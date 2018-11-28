#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long int llu;
typedef map<llu,llu>::reverse_iterator mrit;

int main() {
  int T;
  llu N, K;
  cin >> T;

  for(int caso = 1; caso <= T; caso++) {
    cin >> N >> K;

    map<llu, llu> Q, Q2;

    Q.insert(make_pair(N, 1));
    llu L, R;

    while(K > 0) {
      Q2.clear();
      for(mrit it = Q.rbegin(); it != Q.rend(); it++) {
        if(it->second < K) {
          llu l = it->first-1;
          Q2[l/2] += it->second;
          Q2[l/2 + l%2] += it->second;
          K -= it->second;
        } else {
          llu l = it->first-1;
          L = l/2+l%2;
          R = l/2;
          K = 0;
          break;
        }
      }

      Q = Q2;
    }

    cout << "Case #" << caso << ": " << L << " " << R << endl;
  }

  return 0;
}
