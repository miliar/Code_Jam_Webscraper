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

void solve(const int test_case){
  string line;
  int K;
  cin >> line >> K;
  int result = INF;
  {
    string tmp = line;
    int res = 0;
    for (int i = 0; i < tmp.size() - (K - 1); i++){
      if (tmp[i] == '-'){
        for (int j = 0; j < K; j++){
          tmp[i + j] = tmp[i + j] == '-' ? '+' : '-';

        }
        res++;
      }
    }
    bool ok = true;
    for (int i = 0; i < tmp.size(); i++){
      if (tmp[i] == '-'){
        ok = false;
      }
    }
    if (ok){
      result = min(result, res);
    }
  }
  {
    string tmp = line;
    reverse(tmp.begin(), tmp.end());
    int res = 0;
    for (int i = 0; i < tmp.size() - (K - 1); i++){
      if (tmp[i] == '-'){
        for (int j = 0; j < K; j++){
          tmp[i + j] = tmp[i + j] == '-' ? '+' : '-';
        }
        res++;
      }
    }
    bool ok = true;
    for (int i = 0; i < tmp.size(); i++){
      if (tmp[i] == '-'){
        ok = false;
      }
    }
    if (ok){
      result = min(result, res);
    }
  }
  string ans = "IMPOSSIBLE";
  if (result != INF){
    ans = to_string(result);
  }
  cout << "Case #" << test_case << ": " << ans << endl;
}
int main() {
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++){
    solve(i);
  }
  return 0;
}
