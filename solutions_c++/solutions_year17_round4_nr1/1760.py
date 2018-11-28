#include<bits/stdc++.h>

using namespace std;

int main() {
  int T;

  cin >> T;
  for(int caso = 1; caso <= T; caso++) {
    int N, P, n;
    cin >> N >> P;
    vector<int> resto(4, 0);

    for(int i = 0; i < N; i++) {
      cin >> n;
      resto[n%P]++;
    }

    int res = resto[0];

    if(P == 2) {
      res += (resto[1]+1)/2;
    } else if(P == 3) {
      res += min(resto[1], resto[2]);
      res += (max(resto[1], resto[2])-min(resto[1], resto[2])+2)/3;

    } else {
      res += min(resto[1], resto[3]) + resto[2]/2;
      res += (max(resto[1], resto[3])-min(resto[1], resto[3])+3)/4;
    }

    cout << "Case #" << caso << ": " << res;

    cout << endl;
  }

  return 0;
}
