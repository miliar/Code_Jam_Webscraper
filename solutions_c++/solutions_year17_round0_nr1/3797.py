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

const int N = 2005;
int cnt[N];

bool f(char c, int flip) {
  if(c == '+')
    return 1 ^ (flip & 1);
  return 0 ^ (flip & 1);
}

int main() {
  file;
  int T;
  cin >> T;
  for(int t = 1; t <= T; t++) {
    memset(cnt, 0, sizeof cnt);
    string a; int k;
    cin >> a >> k;
    int n = (int)a.size(), ret = 0;
    for(int i = 0, flip = 0; i < n;) {
      flip += cnt[i];
      if(!f(a[i], flip)) {
        if(i + k > n) {
          goto bad;
        }
        for(int j = i + 1; j < i + k; j++) {
          flip += cnt[j];
          if(f(a[j], flip)) {
            if(j + k > n)
              goto bad;
            ret++;
            flip++;
            cnt[j + k]--;
          }
        }
        i += k;
        ret++;
      }else {
        i++;
      }
    }
    printf("Case #%d: %d\n", t, ret);
    continue;
    bad:
      printf("Case #%d: IMPOSSIBLE\n", t);
  }
}
