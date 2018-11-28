#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cctype>

#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>

using namespace std;

#define rep(i,n) for (int (i)=0; (i)<(n); ++(i))
#define fup(i, a, b) for (__typeof(a) i = (a); i != (b); ++i)
#define fdown(i, a, b) for (__typeof(a) i = (a); i != (b); --i)
#define all(x) (x).begin(),(x).end()
#define forall(i, x) fup(i, (x).begin(),(x).end())
#define debug(x) cout << #x << " = " << x << "\n"

#define K first
#define S second

int main() {
  int t, c = 0;
  int d, n;
  pair<int,int> h[1010];

  for (scanf("%d", &t); t--;) {
    scanf("%d %d", &d, &n);
    rep(i,n) scanf("%d %d", &h[i].K, &h[i].S);

    sort(h,h+n);

    int j = n-1;
    double tt = double(d-h[j].K) / h[j].S;
    for (int i = n - 2; i >= 0; --i) {
    double aux = double(d-h[i].K) / h[i].S;
      if (aux > tt) {
        j = i;
        tt = double(d-h[j].K) / h[j].S;
      }
    }

    printf("Case #%d: %lf\n", ++c, d / tt);
  }

  return 0;
}
