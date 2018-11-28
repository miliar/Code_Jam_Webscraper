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



int main(void){
  int T;
  cin >> T;
  for (int tt = 0; tt < T; ++tt) {
    cout << "Case #" << tt+1 << ": ";

    int N, C, M;
    cin >> N >> C >> M;
    assert(C == 2);

    int sum[C];
    int cnts[N][C];
    fill_n(sum, C, 0);
    for(int i = 0; i < N; ++i)
      fill_n(cnts[i], C, 0);
    for(int i = 0; i < M; ++i) {
      int P, B;
      cin >> P >> B;
      ++cnts[P-1][B-1];
      ++sum[B-1];
    }
    int L = max(sum[0], sum[1]);
    int pro = 0;
    for(int i = 0; i < N; ++i) {
      if(cnts[i][0] + cnts[i][1] > L) {
        assert(pro == 0);
        if(i == 0)
          L = cnts[i][0] + cnts[i][1];
        else
          pro += cnts[i][0] + cnts[i][1] - L;
      }
    }
    cout << L << " " << pro << endl;
  }

  return 0;
}
