#include <bits/stdc++.h>

using namespace std;

#define siz(x) ((int)(x).size())
#define all(x) (x).begin(),(x).end()
#define foreach(it,a) for(__typeof((a).begin()) it=(a).begin();it!=(a).end();it++)
#define rep(i,a,b) for (int i=(a),_ed=(b);i<_ed;i++)
#define per(i,a,b) for (int i=(b)-1,_ed=(a);i>=_ed;i--)

typedef long long ll;
typedef unsigned long long ull;

double D;
int T,N;
double ans = 0;

int main()
{
#ifndef ONLINE_JUDGE
  freopen("A-large.in","r",stdin);
  freopen("A.out","w",stdout);
#endif
  cin >> T;
  rep(cas, 1, T+1) {
    cin >> D >> N;
    ans = 0;
    rep(i, 0, N) {
      double tk, ts;
      cin >> tk >> ts;
      tk = D - tk;
      ts = tk / ts;
      if(ts > ans) ans = ts;
    }
    ans = D/ans;
    printf("Case #%d: %.9lf\n", cas, ans);
  }

  return 0;
}

