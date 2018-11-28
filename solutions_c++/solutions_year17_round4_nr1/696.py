#include <iostream>
#include <string>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

int main() {
  int T;

  cin >> T;

  for (int t=1;t<=T;t++) {
    int N, P;
    cin >> N >> P;

    vector<int> n(P+2, 0);
    for (int i=0;i<N;i++) {
      int g;
      cin >> g;
      n[g%P]++;
    }

    int ans = 0;
    ans += n[0];
    int match = 0;

    if (P == 3 || P == 4) {
      match = min(n[1], n[P-1]);
      ans += match;
      n[1] -= match;
      n[P-1] -= match;
    }

    if (P%2==0) {
      match = n[P/2]/2;
      ans += match;
      n[P/2] -= match*2;
    }

    switch (P) {
      case 2:
        if (n[1] == 1) { ans++; n[1]--; }
      break;
      case 3:
        {
          int groups = (n[1] + n[2]);
          match = groups/3;
          ans += match;
          groups -= match*3;
          if (groups > 0) ans++;
        }
      break;
      case 4:
        {
          int rem = (n[1] + n[3] + n[2]*2);
          match = (n[1] + n[3] + n[2]*2)/4;

          ans += match;
          if (rem > 0) ans++;
        }
      break;
    }

    printf("Case #%d: %d\n", t, ans);
  }

}
