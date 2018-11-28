#include<bits/stdc++.h>
using namespace std;
inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}
typedef long long ll;
typedef pair<ll,ll> P;
const int INF=INT_MAX / 3;
const ll LINF=LLONG_MAX / 3LL;
#define CONST 1000000007
#define EPS (1e-8)
#define PB push_back
#define MP make_pair
#define sz(a) ((int)(a).size())
#define reps(i,n,m) for(int i=(n);i<int(m);i++)
#define rep(i,n) reps(i,0,n)
#define SORT(a) sort((a).begin(),(a).end())
ll mod(ll a,ll m){return (a%m+m)%m;}
int dx[9]={0,1,0,-1,1,1,-1,-1,0},dy[9]={1,0,-1,0,1,-1,1,-1,0};

int solve() {
  const int DAY = 1440;
  int ans = DAY;
  vector<int> cs(1440, 0), js(1440, 0);
  int n, m;
  int csum = 0, jsum = 0;
  cin >> n >> m;
  rep(i, n) {
    int x, y;
    cin >> x >> y;
    cs[x] = y;
    csum += y - x;
  }
  rep(i, m) {
    int x, y;
    cin >> x >> y;
    js[x] = y;
    jsum += y - x;
  }

  rep(s, DAY) {
    if(cs[s] == 0 && js[s] == 0) continue;

    bool flag = true;
    int ct = DAY/2, jt = DAY/2;
    bool c_baby = cs[s] == 0;

    int i = 0;
    int change = 0;
    cerr<<s<<endl;
    int crest = csum;
    int jrest = jsum;
    while(i < DAY) {
      int t = (s + i) % DAY;
      if(cs[t] != 0) { // James
        if (cs[t] - t > jt) {
          flag = false;
          break;
        }
        jt -= (cs[t] - t);
        crest -= (cs[t] - t);
        i += (cs[t] - t);

        if(c_baby) {
          c_baby = false;
          change += 1;
        }

      } else if(js[t] != 0) { // Cameron

        if (js[t] - t > ct) {
          flag = false;
          break;
        }

        ct -= (js[t] - t);
        jrest -= (js[t] - t);
        i += (js[t] - t);

        if(!c_baby) {
          c_baby = true;
          change += 1;
        }

      } else {
        if ((c_baby && ct - jrest == 0) || (!c_baby && jt - crest == 0)) {
          c_baby = !c_baby;
          change += 1;
        }

        if(c_baby) {
          ct -= 1;
        } else {
          jt -= 1;
        }

        if(ct - jrest < 0 || jt - crest < 0) {
          flag = false; break;
        }
        i++;
      }
    }
    if(c_baby != (cs[s] == 0)) {
      change += 1;
    }
    if(flag) {
      ans = min(ans, change);
    }
  }
  return ans;
}

int main(){
  ll T;
  cin >> T;
  for(int i = 1; i <= T; ++i) {
    int ans = solve();
    printf("Case #%d: %d\n", i, ans);
  }

  return 0;
}
