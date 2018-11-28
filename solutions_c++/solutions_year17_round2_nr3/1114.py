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
typedef long double LB;
template <class T> inline void maxi(T &x,T y) {if (y > x) x = y;}
template <class T> inline void mini(T &x,T y) {if (y < x) x = y;}

const int N = 200, B = 0x7fffffff;
int t;
pair <LB, LB> a[N];
LB d[N][N];
int lim[N];
int n, q;
LB dp[N][N];

LB rec(int now, int wh){
  if (now == n) return 0.0;
  LB &ret = dp[now][wh];
  if (ret != -1.0) return ret;
  ret = 100000000000000000.0;
  if (now + 1 <= lim[wh]) mini(ret, rec(now + 1, wh) + d[now][now + 1] / a[wh].se);
  mini(ret, rec(now + 1, now) + d[now][now + 1] / a[now].se);
  return ret;
}

int main(){
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  get(t);
  for (int tt = 1; tt <= t; tt++){
    get(n), get(q);
    for (int i = 1; i <= n; i++) cin >> a[i].fi >> a[i].se;
    for (int i = 1; i <= n; i++){
      for (int j = 1; j <= n; j++) cin >> d[i][j];
    }
    int ax, bx;
    get(ax), get(bx);
    for (int i = 1; i <= n; i++){
      ll nas = 0;
      for (int j = i + 1; j <= n; j++){
        nas += d[j - 1][j];
        if (nas <= a[i].fi) lim[i] = j;
        else break;
      }
    }
    for (int i = 1; i <= n; i++){
      for (int j = 1; j <= n; j++) dp[i][j] = -1.0;
    }
    cout.precision(9);
    printf("Case #%d: ", tt);
    cout << rec(1, 1) << '\n';
  }

  return !!0;
}

