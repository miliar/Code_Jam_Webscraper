#include <bits/stdc++.h>

using namespace std;

#define siz(x) ((int)(x).size())
#define all(x) (x).begin(),(x).end()
#define foreach(it,a) for(__typeof((a).begin()) it=(a).begin();it!=(a).end();it++)
#define rep(i,a,b) for (int i=(a),_ed=(b);i<_ed;i++)
#define per(i,a,b) for (int i=(b)-1,_ed=(a);i>=_ed;i--)

typedef long long ll;
typedef unsigned long long ull;

const int maxN = 100+13;

int T,N,Q;
int s[maxN],e[maxN];
int m[maxN][maxN];
double f[maxN];

int u1,v1;
int main()
{
#ifndef ONLINE_JUDGE
  freopen("C-small-attempt0.in","r",stdin);
  freopen("C.out","w",stdout);
#endif
  cin >> T;
  rep(cas, 1, T+1) {
    cin >> N >> Q;
    rep(i, 1, N+1) {
      cin >> e[i] >> s[i];
    }
    for(int i = 1; i <= N; i++) {
      for(int j = 1; j <= N; j++) {
        cin >> m[i][j];
      }
    }
    cin >> u1 >> v1;
    for(int i = 1; i <= N; i++) {
      f[i] = 1e13;
    }
    f[1] = 0;
    for(int i = 1; i <= N; i++) {
      int tt = 0;
      //cout << i << ":" << endl;
      for(int j = i+1; j <=N; j++) {
        tt += m[j-1][j];
        if(tt > e[i]) break;
        //cout << j << endl;
        //cout << tt << ' ' << f[i]+(double)tt/s[i] << endl;
        f[j] = min(f[j], f[i]+(double)tt/s[i]);
      }
    }
    printf("Case #%d: %.9lf\n", cas, f[N]);
  }

  //cout<<"time: "<<(ll)clock()*1000/CLOCKS_PER_SEC<<" ms"<<endl;

  return 0;
}

