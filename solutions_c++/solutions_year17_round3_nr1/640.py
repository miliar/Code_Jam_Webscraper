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

const double PI = 2 * acos(0);

double solve(vector<pair<double, ll> > &side, int cur, int N, int K) {
  ll maxR = side[cur].second;
  double res = 0;
  if(cur < N - K) {
    res = side[cur].first;
    --K;
  }
  for(int i = 0; i < K; ++i) {
    res += side[N - i - 1].first;
    maxR = max(maxR, side[cur].second);
  }
  res += PI * maxR * maxR;
  return res;
}

int main(void){
  int T;
  cin >> T;
  for (int tt = 0; tt < T; ++tt) {
    cout << "Case #" << tt+1 << ": ";

    int N, K;
    cin >> N >> K;
    vector<pair<double, ll> > side;
    for(int i = 0; i < N; ++i) {
      ll R, H;
      cin >> R >> H;
      side.push_back(make_pair(2 * PI * R * H, R));
    }
    sort(side.begin(), side.end());

    double res = 0;
    for(int i = 0; i < N; ++i)
      res = max(res, solve(side, i, N, K));
    printf("%.10lf\n", res);
  }

  return 0;
}
