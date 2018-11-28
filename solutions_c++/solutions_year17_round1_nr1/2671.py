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
int sum[25][25][25][25], C[25][25][25][25];

char a[25][25];

int t;

int n, m;
     
pii pos[300];
                              
int main() 
{
  Read_rap ();
  files ("A-small-attempt0");
  int T;  cin >> T;

  for (int t = 1;t <= T;t ++) {
    cin >> n >> m;
    for (int i = 1;i <= n;i ++) {
      for (int j = 1;j <= m;j ++) {
        cin >> a[i][j];
        if (a[i][j] != '?') {
          pos[a[i][j]] =  (mp (i, j));
        }
      }
    }
    for (char c = 'A';c <= 'Z';c ++) {
      int x = pos[c].F, y = pos[c].S;
      if (x + y == 0) continue;      
      pos[c] = {0, 0};

      for (int i = 1;i <= n;i ++) {
        for (int j = 1;j <= m;j ++) {

          for (int fi = i;fi <= n;fi ++) {
            for (int fj = j;fj <= m;fj ++) {
              sum[i][j][fi][fj] = sum[i][j][fi][fj - 1] + sum[i][j][fi - 1][fj] - sum[i][j][fi - 1][fj - 1];
              if (a[fi][fj] != '?') {
                C[i][j][fi][fj] = a[fi][fj];
                sum[i][j][fi][fj] ++;
              }
              else
              {
                C[i][j][fi][fj] = (C[i][j][fi - 1][fj] | C[i][j][fi][fj - 1]);
              }
            }
          }
        }
      }

      int sx = x, sy = y, fx = x, fy = y;
      int P = 0;

      for (int i = 1;i <= n;i ++) {
        for (int j = 1;j <= m;j ++) {
          for (int fi = 1;fi <= n;fi ++) {
            for (int fj = 1;fj <= m;fj ++) {
              if (sum[i][j][fi][fj] == 1 && i <= x && x <= fi && j <= y && y <= fj) {
                int pl = (fi - i + 1) * (fj - j + 1);
                if (pl > P) {
                  P = pl;
                  sx = i, sy = j, fx = fi, fy = fj;
                }
              }
            }
          }
        }
      }
      for (int i = sx;i <= fx;i ++) 
        for (int j = sy;j <= fy;j ++)
          a[i][j] = c;
    }
    cout << "Case #" << t << ":" << endl;
    for (int i = 1;i <= n;i ++, cout << endl)
      for (int j = 1;j <= m;j ++)
        cout << a[i][j];   
  }
    


  return 0;
} 










// Coded by Z...