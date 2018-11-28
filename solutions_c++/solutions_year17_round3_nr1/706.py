#include <bits/stdc++.h>

using namespace std;

#define siz(x) ((int)(x).size())
#define all(x) (x).begin(),(x).end()
#define foreach(it,a) for(__typeof((a).begin()) it=(a).begin();it!=(a).end();it++)
#define rep(i,a,b) for (int i=(a),_ed=(b);i<_ed;i++)
#define per(i,a,b) for (int i=(b)-1,_ed=(a);i>=_ed;i--)

const double PI = acos(-1.0);
typedef long long ll;
typedef unsigned long long ull;

const int maxN  = 1000+13;

struct Pancake {
  double r, h, id;
  double s;
  friend bool operator < (Pancake& a, Pancake& b) {
    return a.s > b.s;
  }
};

int T;
int N,K;
Pancake a[maxN];

int main() {
#ifndef ONLINE_JUDGE
  freopen("A-large.in","r",stdin);
  freopen("A.out","w",stdout);
#endif
  cin >> T;
  rep(cas, 1, T+1) {
    cin >> N >> K;
    rep(i, 1, N+1) {
      cin >> a[i].r >> a[i].h;
      a[i].s = a[i].r * a[i].h * 2.0;
    }
    sort(a+1, a+1+N);
    double tr = 0; int id = -1;
    double ans = 0.0;
    for(int k = 1; k <= N; k++) {
      int ind = 0;
      double ta = a[k].r * a[k].r;
      ta += a[k].s;
      int i = 1;
      for(i = 1; i <= N && ind < K-1; i++) if(i!=k) {
        if(a[i].r <= a[k].r) {
          ta += a[i].s;
          ind ++;
        }
      }
      if(ind == K-1) {
        if(ta > ans) ans = ta;
      }
    }
    ans *= PI;
    printf("Case #%d: %.10lf\n", cas, ans);
  }

  //cout<<"time: "<<(ll)clock()*1000/CLOCKS_PER_SEC<<" ms"<<endl;

  return 0;
}

