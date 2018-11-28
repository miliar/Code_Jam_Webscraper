#include <bits/stdc++.h>

using namespace std;

const int maxn = 110;
const int maxp = 4;

int n,p;
int g[maxn];
int m[maxp];

int main(){
  ios::sync_with_stdio(false);
//   cin.tie(0);
  int t; cin >> t;
  for(int cass = 1; cass <= t; ++cass){
    cin >> n >> p;
    for(int i = 0; i < n; ++i) cin >> g[i];
    memset(m,0,sizeof(m));
    for(int i = 0; i < n; ++i) m[g[i]%p]++;
    int sol = 0;
    if(p == 2){
      sol = n-m[1]/2;
    }
    else if(p == 3){
      sol = m[0] + min(m[1],m[2]);
      int x = max(m[1],m[2])-min(m[1],m[2]);
      sol += x/3;
      if(x%3) ++sol;
    }
    else if(p == 4){
      sol = m[0] + m[2]/2;
      int x = m[2]%2;
//       cerr << sol << '\n';
      sol += min(m[1],m[3]);
      int y = max(m[1],m[3])-min(m[1],m[3]);
//       cerr << sol << '\n';
      if(x == 0){
        sol += y/4;
        if(y%4) ++sol;
      }
      else{
        if(y >= 3){
          sol++;
          y -= 2;
          --x;
        }
        sol += y/4;
        if(y%4 or x) ++sol;
      }
    }
    cout << "Case #" << cass << ": " << sol << '\n';
  }
}