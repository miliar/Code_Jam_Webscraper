#include <algorithm>
#include <bitset>
#include <cassert>
#include <cfloat>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <memory>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

// c++11
#include <array>
#include <tuple>
#include <unordered_map>
#include <unordered_set>

#define mp make_pair
#define mt make_tuple
#define rep(i, n) for (int i = 0; i < (n); i++)

using namespace std;

using ll = long long;
using ull = unsigned long long;
using pii = pair<int, int>;

const ll INF = 1LL << 50;
const double EPS = 1e-9;
const ll MOD = 1000000007;

const int dx[] = {1, 0, -1, 0}, dy[] = {0, -1, 0, 1};
const int MAX_N = 1010;
ll dp[MAX_N][MAX_N][2];
bool visited[MAX_N][MAX_N][2];
vector<pair<ll, ll>> pans;
int N,K;
ll memo(int pos, int cnt, int empty){
  // cout << "N = " << N << " K = " << K << endl;
  // cout << pos << " " << cnt << " " << empty << endl;
  if (cnt == K){
    return 0;
  }
  if (pos >= N){
    return -INF;
  }

  if (visited[pos][cnt][empty]){
    return dp[pos][cnt][empty];
  }
  visited[pos][cnt][empty] = true;
  ll &res = dp[pos][cnt][empty];
  res = -INF;

  res = max(res, memo(pos + 1, cnt, empty));
  ll val;

  if (empty){
      val = pans[pos].first * pans[pos].first;
  }else{
    val = 0;
  }
  res = max(res, memo(pos + 1, cnt + 1, false) + val + 2LL * pans[pos].first * pans[pos].second);
  return res;
}

void solve(const int test_case){
  pans.clear();
  memset(dp, 0, sizeof(dp));
  memset(visited, false, sizeof(visited));
  cin >> N >> K;

  for (int i = 0; i < N; i++){
    int R,H;
    cin >> R >> H;
    pans.emplace_back(mp(R, H));
  }
  sort(pans.rbegin(), pans.rend());
  // sort(r.begin(), r.end());
  // for (int i = 0; i < r.size(); i++){
  //   if (dic_r.count(r[i]) == 0){
  //     dic_r[r[i]] = dic_r.size();
  //   }
  // }
  // //compress
  // for (int i = 0; i < N; i++){
  //   pans[i].first = dic_r[pans[i].first];
  // }
  // reverse(pans.begin(), pans.end());
  cout << "Case #" << test_case << ": ";

  ll res = memo(0, 0, true);
  double ans = res * M_PI;
  printf("%.10lf\n", ans);

}
int main() {
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++){
    solve(i);
  }
  return 0;
}
