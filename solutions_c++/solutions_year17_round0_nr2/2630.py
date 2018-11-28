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

char mn[Sz];

string s;

int n;
                              
int main() 
{
  Read_rap ();
  files ("B-large");
  cin >> t;
             
  for (int c = 1;c <= t;c ++) {
    cin >> s;
    n = sz(s);
                       
    bool big = 0;
    string res = "";
    for (int i = 0;i < n;i ++) {
      if (big) {    
        res.pb ('9');
        continue;
      }
      if (i == n - 1)
      {
        res.pb (s[i]);
        continue;
      }
      int j = i;
      while (j + 1 < n && s[j] == s[i])
        j ++;        
      if (s[i] > s[j]) {
        res.pb (s[i] - 1);
        big = 1;
      }
      else    
      {
        res.pb (s[i]);
      }
    }            
    int l = 0;
    while (l + 1 < sz(res) && res[l] == '0')
      l ++;

    cout << "Case #" << c << ": " << res.substr (l, sz(res) - l) << endl;
  }

  return 0;
} 










// Coded by Z...