#include <bits/stdc++.h>

using namespace std;

#define siz(x) ((int)(x).size())
#define all(x) (x).begin(),(x).end()
#define foreach(it,a) for(__typeof((a).begin()) it=(a).begin();it!=(a).end();it++)
#define rep(i,a,b) for (int i=(a),_ed=(b);i<_ed;i++)
#define per(i,a,b) for (int i=(b)-1,_ed=(a);i>=_ed;i--)

typedef long long ll;
typedef unsigned long long ull;

const int maxN = 100;

int T,N;
string s;
int tn[maxN];
ll num;

bool check(int n) {
  int last = 10;
  while(n) {
    int tn = n%10;
    if(tn > last) return false;
    last = tn;
    n /=10;
  }
  return true;
}

int main()
{
#ifndef ONLINE_JUDGE
  freopen("B-large.in","r",stdin);
  freopen("B.out","w",stdout);
#endif
  cin >> T;
  rep(cas, 1, 1+T) {
    cout << "Case #" << cas << ": ";
    cin >> s;
    N = s.length();
    if(N == 1) {
      cout << s << endl;
      continue;
    }
    int ans = 0;
    rep(i, 0, N) tn[i+1] = s[i] - '0';
    tn[0] = 0;
    rep(i, 1, N) {
      if(tn[i] > tn[i+1]) {
        ans = i;
        break;
      }
    }
    if(ans == 0) {
      cout << s << endl;
      continue;
    }
    //cout << ans << endl;
    for(int i = ans-1; i>=1; i--) {
      if(tn[i] == tn[ans]) ans--;
    }
    if(tn[ans] == 1) {
      rep(i, 1, N) {
        cout << "9";
      }
      cout << endl;
    } else {
      rep(i, 1, ans) {
        cout << tn[i];
      }
      cout << tn[ans] - 1;
      rep(i, ans+1, N+1) {
        cout << 9;
      }
      cout << endl;
    }

  }

  //cout<<"time: "<<(ll)clock()*1000/CLOCKS_PER_SEC<<" ms"<<endl;

  return 0;
}

