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

int T,N,P;
int g[maxN];

int main()
{
#ifndef ONLINE_JUDGE
  freopen("A-large (1).in","r",stdin);
  freopen("A.out","w",stdout);
#endif
  cin >> T;
  rep(cas, 1, T+1) {
    cin >> N >> P;
    rep(i, 1, N+1) {
      cin >> g[i];
    }
    if(P == 2) {
      int count_even = 0;
      rep(i, 1, N+1) {
        if(g[i]%2 == 0) count_even++;
      }
      int ans = count_even;
      ans += (N - count_even +1) /2;
      printf("Case #%d: %d\n", cas , ans);
      continue;
    }
    if(P == 3) {
      int c[3];
      rep(i, 0, 3) c[i] = 0;
      rep(i, 1, N+1) {
        c[g[i]%3] ++;
      }
      int ans = c[0];
      int tt = min(c[1] , c[2]);
      ans += tt;
      c[1] -= tt; c[2] -= tt;
      tt = c[1] / 3;
      ans+= tt; c[1] -= tt*3;
      tt = c[2] / 3;
      ans+= tt; c[2] -= tt*3;
      if(c[1] + c[2] > 0) ans++;
      printf("Case #%d: %d\n", cas , ans);
      continue;
    }
    if(P == 4) {
      int c[4];
      rep(i, 0, 4) c[i] = 0;
      rep(i, 1, N+1) {
        c[g[i]%4] ++;
      }
      int ans = c[0];
      int tt = min(c[1] , c[3]); //1+3
      ans += tt;
      c[1] -= tt; c[3] -= tt;

      tt = c[2]/2; // 2+2
      ans += tt;
      c[2] -= tt; c[2] -= tt;

      tt = min(c[1]/2, c[2]);//1+1+2
      ans+= tt; 
      c[1] -= tt*2; c[2] -= tt;

      tt = min(c[3]/2, c[2]);//3+3+2
      ans+= tt; 
      c[3] -= tt*2; c[2] -= tt;

      tt = c[1] /4;
      ans+=tt;
      c[1] -= tt*4;

      tt = c[3] /4;
      ans+=tt;
      c[3] -= tt*4;

      if(c[1] + c[2] +c[3] > 0) ans++;
      int ans1 = ans;

      rep(i, 0, 4) c[i] = 0;
      rep(i, 1, N+1) {
        c[g[i]%4] ++;
      }
      ans = c[0];
      tt = min(c[1] , c[3]); //1+3
      ans += tt;
      c[1] -= tt; c[3] -= tt;

      tt = min(c[1]/2, c[2]);//1+1+2
      ans+= tt; 
      c[1] -= tt*2; c[2] -= tt;

      tt = min(c[3]/2, c[2]);//3+3+2
      ans+= tt; 
      c[3] -= tt*2; c[2] -= tt;

      tt = c[2]/2; // 2+2
      ans += tt;
      c[2] -= tt; c[2] -= tt;

      tt = c[1] /4;
      ans+=tt;
      c[1] -= tt*4;

      tt = c[3] /4;
      ans+=tt;
      c[3] -= tt*4;

      if(c[1] + c[2] +c[3] > 0) ans++;
      if(ans1 < ans) ans1 = ans;

      rep(i, 0, 4) c[i] = 0;
      rep(i, 1, N+1) {
        c[g[i]%4] ++;
      }
      ans = c[0];
      tt = min(c[1] , c[3]); //1+3
      ans += tt;
      c[1] -= tt; c[3] -= tt;

      tt = min(c[1]/2, c[2]);//1+1+2
      ans+= tt; 
      c[1] -= tt*2; c[2] -= tt;

      tt = c[2]/2; // 2+2
      ans += tt;
      c[2] -= tt; c[2] -= tt;

      tt = min(c[3]/2, c[2]);//3+3+2
      ans+= tt; 
      c[3] -= tt*2; c[2] -= tt;


      tt = c[1] /4;
      ans+=tt;
      c[1] -= tt*4;

      tt = c[3] /4;
      ans+=tt;
      c[3] -= tt*4;
      if(ans1 > ans) ans = ans1;
      printf("Case #%d: %d\n", cas , ans);
      continue;

    }
  }
  //cout<<"time: "<<(ll)clock()*1000/CLOCKS_PER_SEC<<" ms"<<endl;

  return 0;
}

