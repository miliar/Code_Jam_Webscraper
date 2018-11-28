#include <bits/stdc++.h>
using namespace std;

#define REP(i,n) for(int i=0;i<(int)(n);i++)
#define ALL(x) (x).begin(), (x).end()

typedef long double ld;

int main(){
  int T;
  cin >> T;
  REP(t, T) {
    int K, N;
    cin >> N >> K;
    vector<pair<int,int>> pc(N);
    REP(i,N) {
      int R, H;
      cin >> R >> H;
      pc[i] = make_pair(R, H);
    }
    sort(ALL(pc));

    ld res = 0;
    for(int i = K - 1; i < N; ++i) {
      vector<ld> tmp;
      REP(j,i) tmp.push_back(2 * M_PI * pc[j].first * pc[j].second);
      sort(tmp.rbegin(), tmp.rend());
      ld area = M_PI * pc[i].first * pc[i].first
              + 2 * M_PI * pc[i].first * pc[i].second;
      REP(j,K - 1) area += tmp[j];
      res = max(res, area);
    }

    cout << "Case #" << t + 1 << ": " << fixed << setprecision(10) << res << endl;
  }
  return 0;
}

