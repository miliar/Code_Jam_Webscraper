#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

#define REP(i,s,n) for(int i=(int)(s);i<(int)(n);i++)

using namespace std;
typedef long long int ll;
typedef vector<int> VI;
typedef vector<ll> VL;
typedef pair<int, int> PI;
const ll mod = 1e9 + 7;


int calc(vector<int> rem, int p) {
  if (p == 2) {
    return rem[0] + (rem[1] + 1) / 2;
  }
  if (p == 3) {
    int cnt = rem[0];
    int s = min(rem[1], rem[2]);
    cnt += s;
    rem[1] -= s;
    rem[2] -= s;
    return cnt + (rem[1] + rem[2] + 2) / 3;
  }
  return -1;
}

int main(void){
  cin.tie(0);
  ios::sync_with_stdio(0);
  int t;
  cin >> t;
  REP(loop_cnt, 0, t) {
    int n, p;
    cin >> n >> p;
    vector<int> g(n);
    vector<int> rem(p);
    REP(i, 0, n) {
      cin >> g[i];
      rem[g[i] % p] += 1;
    }
    cout << "Case #" << loop_cnt + 1 << ": " << calc(rem, p) << "\n";
  }
}
