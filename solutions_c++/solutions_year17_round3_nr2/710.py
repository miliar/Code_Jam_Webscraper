#include <bits/stdc++.h>

using namespace std;

#define siz(x) ((int)(x).size())
#define all(x) (x).begin(),(x).end()
#define foreach(it,a) for(__typeof((a).begin()) it=(a).begin();it!=(a).end();it++)
#define rep(i,a,b) for (int i=(a),_ed=(b);i<_ed;i++)
#define per(i,a,b) for (int i=(b)-1,_ed=(a);i>=_ed;i--)

typedef long long ll;
typedef unsigned long long ull;

const int maxN = 2000+13;
const int inf = 0x3f3f3f3f;

struct tu{
  int t,u;
};

bool cmp(tu& x,tu& b) {
  return x.t < b.t;
}

int T;
int ac, aj;
int tl[maxN];
tu a[maxN];
int f[maxN][maxN][2][2];

int main() {
#ifndef ONLINE_JUDGE
  freopen("B-large.in","r",stdin);
  freopen("B.out","w",stdout);
#endif
  cin >> T;
  rep(cas, 1, T+1) {
    memset(tl,-1,sizeof(tl));
    cin >> ac >> aj;
    int N = ac+aj;
    int ind = 0;
    rep(i,0,ac) {
      int st,ed;
      cin >> st >> ed;
      rep(j, st, ed) {
        tl[j] = 0;
      }
    }
    rep(i,0,aj) {
      int st,ed;
      cin >> st >> ed;
      rep(j, st, ed) {
        tl[j] = 1;
      }
    }
    //f[i][j][st][now]
    // time ctime st 
    // 0 == c
    // 1 == j
    memset(f,inf,sizeof(f));
    if(tl[0] == -1) {
      f[0][1][0][0] = 0;
      f[0][0][1][1] = 0;
    }
    if(tl[0] == 1) {
      f[0][0][1][1] = 0;
    }
    if(tl[0] == 0) {
      f[0][1][0][0] = 0;
    }
    for(int i = 1; i < 1440; i++) {
      for(int j = 0; j <= min(i+13,720); j++) {
        rep(st, 0 ,2) {
          if(tl[i] == -1) {
            if(j!=0)
              f[i][j][st][0] = min(f[i-1][j-1][st][0],f[i-1][j-1][st][1]+1);
            f[i][j][st][1] = min(f[i-1][j][st][1],f[i-1][j][st][0]+1);
          }
          if(tl[i] == 0) {
            if(j!=0)
              f[i][j][st][0] = min(f[i-1][j-1][st][0],f[i-1][j-1][st][1]+1);
          }
          if(tl[i] == 1) {
            f[i][j][st][1] = min(f[i-1][j][st][1],f[i-1][j][st][0]+1);
          }
        }
      }
    }
    int ans = inf;
    rep(st,0,2) {
      rep(ed,0,2) {
        ans = min(ans, f[1439][720][st][ed]+(st!=ed));
      }
    }
    printf("Case #%d: %d\n", cas, ans);
  }
  //cout<<"time: "<<(ll)clock()*1000/CLOCKS_PER_SEC<<" ms"<<endl;

  return 0;
}

