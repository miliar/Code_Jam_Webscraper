#include <iostream>
#include <cmath>
#include <climits>
#include <cstdlib>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cstdio>
#include <queue>
#include <cstring>
#include <cassert>

using namespace std;

typedef long long ll;

pair<int, char> hs[3];

int main(void){
  int T;
  cin >> T;
  for (int tt = 0; tt < T; ++tt) {
    cout << "Case #" << tt+1 << ": ";

    int N;
    int R, O, Y, G, B, V;
    cin >> N >> R >> O >> Y >> G >> B >> V;

    hs[0] = make_pair(R, 'R');
    hs[1] = make_pair(Y, 'Y');
    hs[2] = make_pair(B, 'B');
    sort(hs, hs+3);

    if(hs[2].first * 2 > N) {
      cout << "IMPOSSIBLE" << endl;
      continue;
    }

    char res[N+1];
    fill_n(res, N+1, '\0');

    int i = 0;
    while(hs[2].first > 0) {
      res[i] = hs[2].second;
      --hs[2].first;
      i += 2;
    }
    assert(hs[2].first == 0);
    if(i == N) i = 1;
    while(hs[1].first > 0) {
      assert(res[i] == '\0');
      res[i] = hs[1].second;
      --hs[1].first;
      i += 2;
      if(i >= N) i = 1;
    }
    assert(hs[1].first == 0);
    for(int j = 0; j < N; ++j)
      if(res[j] == '\0') {
        res[j] = hs[0].second;
        --hs[0].first;
      }
    assert(hs[0].first == 0);
    cout << res << endl;
  }

  return 0;
}
