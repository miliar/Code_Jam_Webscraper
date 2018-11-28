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

struct range {
  int L, R;
  bool operator <(const range& that) const{
    if(R - L != that.R - that.L)
      return R - L < that.R - that.L;
    return L > that.L;
  }
};

int main () {
  file;
  int T;
  cin >> T;
  for(int t = 1; t <= T; t++) {
    int n, k;
    cin >> n >> k;
    priority_queue<range> pq;
    pq.push({1, n});
    int ansMin = n + 5, ansMax = 0;
    while(k--) {
      int L = pq.top().L, R = pq.top().R;
      pq.pop();
      int mid = (L + R) >> 1;
      if(L <= mid - 1)
        pq.push({L, mid - 1});
      if(mid + 1 <= R)
        pq.push({mid + 1, R});
      ansMin = min(R - mid, mid - L);
      ansMax = max(R - mid, mid - L);
    }
    printf("Case #%d: %d %d\n", t, ansMax, ansMin);
  }
  return 0;
}
