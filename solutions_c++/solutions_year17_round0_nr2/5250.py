// author: gary
#include <bits/stdc++.h>
using namespace std;
#define FOR(i,a,b) for(int (i)=a;(i)<=(b);++i)
#define REP(i,n) FOR(i,0,(n-1))
#define ALL(x) (x).begin(), x.end()
#define SZ(x) ( (int) (x).size() )
#define dbg(x) cerr << #x << " = " << x << endl;
#define mp make_pair
#define pb push_back
#define fi first
#define se second
template<typename T> inline bool cmin(T &a, const T &b) { return a > b ? a = b, 1 : 0; }
template<typename T> inline bool cmax(T &a, const T &b) { return a < b ? a = b, 1 : 0; }
typedef long long ll;
typedef pair<int, int> pii;

const int inf = 1e9;
const int N = 22;

char s[N];
int n;
int a[N];

int main() {
  int tt;
  scanf("%d", &tt);
  for(int qq = 1; qq <= tt; qq++) {
    printf("Case #%d: ", qq);
    scanf("%s", s);
    n = strlen(s);
    for(int i = 0; i < n; i++)
      a[i] = s[i] - '0';
    ll ans = 0;
    int go = 1;
    for(int i = 0; i < n; i++) {
      if(go) {
        int low = 0;
        for(int j = i + 1; j < n; j++) {
          low |= a[i] < a[j];
          go &= low || a[i] <= a[j];
        }
        if(!go)
          a[i]--;
        ans = ans * 10 + a[i];
      } else {
        ans = ans * 10 + 9;
      }
    }
    printf("%lld\n", ans);
  }
  return 0;
}
