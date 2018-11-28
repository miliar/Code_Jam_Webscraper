#include <bits/stdc++.h>

using namespace std;

#define siz(x) ((int)(x).size())
#define all(x) (x).begin(),(x).end()
#define foreach(it,a) for(__typeof((a).begin()) it=(a).begin();it!=(a).end();it++)
#define rep(i,a,b) for (int i=(a),_ed=(b);i<_ed;i++)
#define per(i,a,b) for (int i=(b)-1,_ed=(a);i>=_ed;i--)

typedef long long ll;
typedef unsigned long long ull;

const int maxN = 1000+13;
int T,K;
int tn[maxN];

int main()
{
#ifndef ONLINE_JUDGE
  freopen("A-small-attempt0.in","r",stdin);
  freopen("A.out","w",stdout);
#endif
  cin >> T;
  rep(cas, 1, T+1) {
    cout << "Case #" << cas << ": ";
    string s;
    cin >> s;
    cin >> K;
    //cout << s<< ' '<< K << endl;
    int N = s.length();
    bool ok = true;
    int ans = 0;
    for(int i = 0; i < N-K+1; i++) {
      if(s[i] == '-') {
        ans ++ ;
        for(int j = 0; j < K; j++) {
          if(s[i+j] == '-') s[i+j] = '+';
          else s[i+j] = '-';
        }
      }
    }
    for(int i = N-K; i < N; i++) {
      if(s[i] == '-') ok = false;
    }
    if(ok) cout << ans << endl;
    else 
      cout << "IMPOSSIBLE" << endl;
  }

  //cout<<"time: "<<(ll)clock()*1000/CLOCKS_PER_SEC<<" ms"<<endl;

  return 0;
}

