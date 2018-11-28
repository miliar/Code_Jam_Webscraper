#include "bits/stdc++.h"
#include "cmath"
#include "math.h"

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

const int N = 1005, B = 0x7fffffff;
int t;
int n, k;
pair <double, double> a[N];
double p = 3.141592653589793238462643383279502884;
double dp[N][N][3];

double rec(int now, int hwm, bool bam){
  if (now == n + 1) return 0.0;
  double &ret = dp[now][hwm][bam];
  if (ret != -1.0) return ret;
  ret = 0.0;
  if (bam == 0){
    maxi(ret, rec(now + 1, 1, 1) + p * a[now].fi * a[now].fi + 2.0 * p * a[now].fi * a[now].se);
    maxi(ret, rec(now + 1, hwm, bam));
  }
  else{
    if (hwm + 1 <= k) maxi(ret, rec(now + 1, hwm + 1, bam) + 2.0 * p * a[now].fi * a[now].se);
    maxi(ret, rec(now + 1, hwm, bam));    
  }
  return ret;
}


int main(){
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  get(t);
  for (int tt = 1; tt <= t; tt++){
    get(n), get(k);
    for (int i = 1; i <= n; i++){
      cin >> a[i].fi;
      cin >> a[i].se;
    }
    sort(a + 1, a + n + 1);
    reverse(a + 1, a + n + 1);
    for (int i = 0; i <= n; i++){
      for (int j = 0; j <= n; j++) dp[i][j][0] = dp[i][j][1] = -1.0;
    }
    cout.precision(9);
    printf("Case #%d: ", tt);
    cout << fixed << rec(1, 0, 0) << '\n';
  }
  return !!0;
}