#include <bits/stdc++.h>

using namespace std;

typedef long long     LL;
typedef pair<int,int> pii;

double PI  = acos(-1);
double EPS = 1e-7;
int INF    = 1000000000;
LL INFLL   = 1000000000000000000LL;

#define fi            first
#define se            second
#define mp            make_pair
#define pb            push_back

#define input(in)     freopen(in,"r",stdin)
#define output(out)   freopen(out,"w",stdout)

#define MIN(a, b)     (a) = min((a), (b))
#define MAX(a, b)     (a) = max((a), (b))

#define RESET(a, b)   memset(a,b,sizeof(a))
#define ALL(a)        (a).begin(), (a).end()
#define SIZE(a)       (int)a.size()
#define SORT(a)       sort(ALL(a))
#define UNIQUE(a)     (a).erase( unique( ALL(a) ), (a).end() )
#define FOR(a, b, c)  for (int (a)=(b); (a)<=(c); (a)++)
#define FORD(a, b, c) for (int (a)=(b); (a)>=(c); (a)--)
#define FORIT(a, b)   for (__typeof((b).begin()) a=(b).begin(); a!=(b).end(); a++)

int mx[8] = {-1,1,0,0,-1,-1,1,1};
int my[8] = {0,0,-1,1,-1,1,-1,1};

// ----- //

int main() {
  int tc;
  scanf("%d", &tc);
  for(int t = 1; t <= tc; t++) {
    printf("Case #%d: ", t);
    int n, k;
    scanf("%d%d", &n, &k);
    queue<pair<int, int>> q;
    q.push(make_pair(0, n+1));
    int ans = 0;
    pair<int, int> r;
    vector<pair<pair<int, int>, int>> v;
    while(!q.empty()) {
      while (!q.empty() && q.front().se - q.front().fi < 2)
        q.pop();
      if (q.empty()) {
        break;
      }
      r = q.front();
      q.pop();
      ans = (r.fi + r.se) / 2;
      //cout << ans << endl;
      v.pb(mp(mp(-ans+r.fi, -r.se+ans), r.fi));
      q.push(make_pair(r.fi, ans));
      q.push(make_pair(ans, r.se));
    }
    //cout << "V" << SIZE(v) << endl;
    sort(v.begin(), v.end());
    cout << -v[k-1].fi.se-1 << " " << -v[k-1].fi.fi-1 << endl;
  }
}