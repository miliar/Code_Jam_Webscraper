#include <iostream>
#include <cstdio>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <cstring>
#include <stack>
#include <queue>
#include <vector>
#include <map>
#include <cmath>
#include <cassert>
#include <set>
#include <complex>
#include <bitset>
#include <sstream>
#include <iomanip>
#include <numeric>
#include <climits>
#include <string>
#include <array>

using namespace std;

typedef pair<int, int> pii;
typedef long long ll;

#define mp make_pair
#define fi first
#define se second
#define pb push_back
#define endl '\n'
#define eps 1e-8
#define io  ios_base::sync_with_stdio(0),cin.tie(0),cout.tie(0);
#define file freopen ("in.txt", "r", stdin),freopen ("out.txt", "w", stdout);
#define filein freopen ("in.txt", "r", stdin);
#define all(v) ((v).begin()), ((v).end())
//#define mid ((st + en) >> 1)


int dp[20][10][2];

string a;

bool f(int idx, int lst, bool less) {
  if(idx == (int)a.size()) {
    return true;
  }
  int &ret = dp[idx][lst][less];
  if(ret != -1)
    return ret;
  ret = 0;
  for(int i = 9; i >= lst && !ret; i--) {
    if(i > a[idx] - '0' && !less) {
      continue;
    }
    int nless = less | (i < a[idx] - '0');
    ret = f(idx + 1, i, nless);
  }
  return ret;
}

void trace(int idx, int lst, bool less, int leadingZero) {
  if(idx == (int)a.size()) {
    return;
  }
  for(int i = 9; i >= lst; i--) {
    if(i > a[idx] - '0' && !less) {
      continue;
    }
    int nless = less | (i < a[idx] - '0');
    if(f(idx + 1, i, nless)) {
      if(i != 0 || leadingZero == true) {
        putchar('0' + i);
      }
      leadingZero &= i == 0;
      trace(idx + 1, i, nless, leadingZero);
      return;
    }
  }
  return;
}

int main () {
  file;
  int T;
  cin >> T;
  for(int t = 1; t <= T; t++) {
    memset(dp, -1, sizeof dp);
    cin >> a;
    f(0, 0, 0);
    printf("Case #%d: ", t);
    trace(0, 0, 0, 0);
    puts("");
  }
}
