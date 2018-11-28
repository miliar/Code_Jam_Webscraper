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
  ll N,K;
  cin >> N >> K;
  priority_queue<int> pque;
  pque.emplace(N);
  for (int i = 0; i < K - 1; i++){
    int len = pque.top();
    pque.pop();
    if (len % 2 == 0){
      pque.emplace(len / 2);
      pque.emplace(len / 2 - 1);
    }else{
      pque.emplace(len / 2);
      pque.emplace(len / 2);
    }
  }
  int len = pque.top();
  int x,y;
  if (len % 2 == 0){
    x = len / 2 - 1;
    y = len / 2;
  }else{
    x = len / 2;
    y = len / 2;
  }
  cout << "Case #" << test_case << ": " << y << " " << x << endl;
}
int main() {
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++){
    solve(i);
  }
  return 0;
}
