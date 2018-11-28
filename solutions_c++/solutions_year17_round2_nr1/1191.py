#include "bits/stdc++.h"

#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define sz(x) (int)x.size()
#define get(x) scanf("%d", &x)
#define all(x) (x).begin(),(x).end()

using namespace std;
typedef long long ll;
typedef pair <int, int> pii;
template <class T> inline void maxi(T &x,T y) {if (y > x) x = y;}
template <class T> inline void mini(T &x,T y) {if (y < x) x = y;}

const int N = 2000, B = 0x7fffffff;
int t;
pair <double, double> a[N];

int main(){
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  get(t);
  for (int tt = 1; tt <= t; tt++){
    int n;
    double d;
    cin >> d >> n;
    for (int i = 1; i <= n; i++) cin >> a[i].fi >> a[i].se;
    sort(a + 1, a + n + 1);
    double ma = 0;
    for (int i = 1; i <= n; i++){
      if (i != n && (d - a[i].fi) / a[i].se <= (d - a[i + 1].fi) / a[i + 1].se) continue;
      maxi(ma, (d - a[i].fi) / a[i].se);
    }
    printf("Case #%d: %.6lf\n", tt, d / ma);
  }
  return !!0;
}

