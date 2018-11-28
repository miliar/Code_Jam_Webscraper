#include<bits/stdc++.h>

# define F first    
# define S second
# define mp make_pair
# define pii pair<int,int>         

# define long long long  
# define pb push_back
# define sz(a) (int)(a.size())

# define y1      NOT
# define left   NEEDED
# define right  THINGS      

const int Mod = (int)1e9 + 7;
const int MX = 1073741822;
const long MXLL = 9223372036854775807;
const int Sz = 2e6 + 10;

using namespace std;

inline void Read_rap () {
  ios_base :: sync_with_stdio(0);
  cin.tie(0); cout.tie(0);
}      
inline void files (string problem) {   
  if (fopen ((problem + ".in").c_str(),"r")) {
    freopen ((problem + ".in").c_str(),"r",stdin);
    freopen ((problem + ".out").c_str(),"w",stdout);
  }
} 

int t;

int n, p;

int r[Sz];

vector <pii> a[Sz];

int cnt[Sz];

inline bool can (int x, int n, int i) {  
  double L = (r[i] * n * 0.9), R = (r[i] * n * 1.1);
  return (L <= x*1.0 && x * 1.0 <= R);
}
inline int get (int x, int i) {
  double val = (10 * x) / (r[i] * 9.0); 
  for (int n = (int)val + 1000;n >= max (int(val) - 1000, 1);n --) {
    if (can (x, n, i)) {
      return n;
    }
  }
  return 0;
}
 
int main() 
{
  Read_rap ();
  files ("B-small-attempt1");  
  cin >> t;      
  for (int c = 1;c <= t;c ++) {
    cin >> n >> p;
    for (int i = 1;i <= n;i ++) cin >> r[i];

    int R = 0;         
    for (int i = 1;i <= n;i ++) {
      for (int j = 1;j <= p;j ++) {
        int x;  cin >> x;      
        int id = get (x, i);
        a[id].pb ({x, i});
        R = max (R, id);
      }
    }        
    int ans = 0;
     
    for (int j = R;j >= 1;j --) { 
      memset (cnt, 0, (n + 1) * 4);
      for (auto x : a[j])
        cnt[x.S] ++;           

      int mn = MX;
      for (int i = 1;i <= n;i ++)
        mn = min (mn, cnt[i]);
      vector <pii> nw;
      for (auto x : a[j]) {
        if (can (x.F, j - 1, x.S))
          nw.pb (x);
      }
      sort (nw.begin(), nw.end());

      for (int i = 0;i < sz(nw);i ++) {
        for (int k = 0;i + k < sz(nw) && nw[i + k].S == nw[i].S;k ++) {
          if (k + 1 <= cnt[nw[i].S] - mn) {
            a[j - 1].pb (nw[i + k]);
          }
        }
        i = i + cnt[nw[i].S] - 1; 
      }
      ans += mn;
      a[j].clear();
    }
    a[0].clear();

    cout << "Case #" << c << ": " << ans << endl;
  }
                       
  return 0;
} 










// Coded by Z...