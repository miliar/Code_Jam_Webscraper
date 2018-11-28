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
pair<bool,double> check(vector<double> p, double val, double U){
  double res = 1.0;
  for (int i = 0; i < p.size(); i++){
    double tmp = max(0.0, val - p[i]);
    p[i] = max(p[i], val);
    U -= tmp;
    res *= p[i];
  }
  if (U >= 0){
    return mp(true, res);
  }
  return mp(false, res);
}
void solve(const int test_case){
  int N, K;
  cin >> N >> K;
  double U;
  cin >> U;
  vector<double> P(N);
  for (int i = 0; i < N; i++){
    cin >> P[i];
  }
  double left,right;
  left = 0;
  right = 1;
  double ans = 0;
  for (int i = 0; i < 300; i++){
    double med = (left + right) / 2;
    pair<bool,double> p = check(P, med, U);
    if (p.first){
      left = med;
      ans = max(ans, p.second);
    }else{
      right = med;
    }
  }
  cout << "Case #" << test_case << ": ";
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
