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
int t;

string s;

int k;

bool b[Sz];
                              
int main() 
{
  Read_rap ();
  files ("A-large");
  cin >> t;
  for (int c = 1;c <= t;c ++) {
    cin >> s >> k;
    for (int i = 0;i < sz(s);i ++)
      b[i] = (s[i] == '-');                  

    int ans = 0;  
    for (int i = 0;i + k - 1 < sz(s);i ++) {
      if (b[i]) {        
        for (int j = i;j <= i + k - 1;j ++)
          b[j] ^= 1;
        ans ++;
      }
    }
    cout << "Case #" << c << ": ";

    bool ok = 1;
    for (int i = 0;i < sz(s);i ++)
      if (b[i]) {
        cout << "IMPOSSIBLE";
        ok = 0;
        break;
      }  
    if (ok) cout << ans;

    cout << endl;
  }  

  return 0;
} 










// Coded by Z...