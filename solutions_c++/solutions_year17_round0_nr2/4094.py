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

const int INF = 1 << 29;
const double EPS = 1e-9;
const ll MOD = 1000000007;

const int dx[] = {1, 0, -1, 0}, dy[] = {0, -1, 0, 1};
const int MAX_D = 20;
int dp[MAX_D][10][2];//digit,pre,lower
string result;
int memo(int pos, int pre, bool lower, string &ans, const string &val){
  if (not result.empty()){
    return 1;
  }
  if (pos >= val.size()){
    result = ans;
    return 1;
  }
  int &res = dp[pos][pre][lower];
  if (res >= 0){
    return res;
  }
  res = 0;
  int v = val[pos] - '0';
  for (int i = 9; i >= 0; i--){
    if (pre <= i){
      if (not lower){

        if (v < i)continue;
      }
      ans += to_string(i);
      res = memo(pos + 1, i, lower | (v > i), ans, val);
      if (res > 0){
        break;
      }
      ans.pop_back();
    }
  }
  return res;
}

void solve(const int test_case){
  ll N;
  cin >> N;
  ll left = 0;
  ll right = N + 1;
  while (right - left > 1){
    ll med = (right + left) / 2;
    if (med > N){
      med = right;
      continue;
    }
    result = "";
    memset(dp, -1, sizeof(dp));
    string val = to_string(med);
    string ans = "";
    int res = memo(0, 0, 0, ans, val);
    if (res > 0){
      left = med;
    }else{
      right = med;
    }
  }
  cout << "Case #" << test_case << ": " << atoll(result.c_str()) << endl;
}
int main() {
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++){
    solve(i);
  }
  return 0;
}
