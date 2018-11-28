#include<bits/stdc++.h>    

# define F first
# define S second
# define mp make_pair
# define pii pair<int,int>

# define long long long
# define pb push_back
# define sz(a) (int)(a.size())

# define y1     tipa_y1
# define left   tipa_left
# define right  tipa_right

const int Mod = (int)1e9 + 7;
const int MX = 1073741822;
const long MXLL = 4611686018427387903;
const int Sz = 1110111;

using namespace std;

inline void Read_rap () {
  ios_base :: sync_with_stdio(0);
  cin.tie(0);
}
int t;

long n, k;

inline void solve () {  
  map <long, long> cnt;
  cnt[n] = 1;
  while (1) {    
    pair <long, long> x = *cnt.rbegin();
    long l = x.F / 2, r = (x.F - 1) / 2;
    if (k <= x.S) {
      cout << l << ' ' << r;
      return;
    }
    k -= x.S;
    cnt.erase (x.F);
    cnt[l] += x.S;
    cnt[r] += x.S;
  } 
}
      

int main()
{
  Read_rap ();
  freopen ("C-large.in","r",stdin);
  freopen ("C-large.out","w",stdout);           
  cin >> t;

  for (int c = 1;c <= t;c ++) {
    cin >> n >> k;
        
    cout << "Case #" << c << ": ";
    solve ();
    cout << endl;
  }


  return 0;
}









// Coded by Z...
