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
const int Sz = 1110111;

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

int T;

double k[Sz], s[Sz], d;

int n;
                              
int main() 
{
  Read_rap ();
  files ("A-large");
  cin >> T;
  for (int t = 1;t <= T;t ++) {
    cin >> d >> n;
    for (int i = 1;i <= n;i ++) cin >> k[i] >> s[i];
    for (int i = 1;i <= n;i ++) {
      for (int j = i + 1;j <= n;j ++) {
        if (k[i] > k[j]) {
          swap (k[i], k[j]);
          swap (s[i], s[j]);
        }
      }
    }
    k[n + 1] = d;
    s[n + 1] = 0;
    double ans = MXLL;
    for (int i = 1;i <= n;i ++) {
      double h = (s[i] > s[i + 1] ? min ((d - k[i]) / s[i], (k[i + 1] - k[i]) / (s[i] - s[i + 1])) : (d - k[i]) / s[i]);
      ans = min (ans, (k[i] + s[i] * h) / h);
    }
    cout << fixed << setprecision (6) << "Case #" << t << ": " << ans << endl;
  }


  return 0;
} 










// Coded by Z...