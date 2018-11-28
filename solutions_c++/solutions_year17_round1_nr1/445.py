#include<bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define rep(i,from,to) for(int i = from; i < (to); ++i)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
#define FOR(i,to) for(int i=0;i<(to);++i)
#define Nmax 101010
string s[55];
int N,M,tt,T;
int get(int x,int y) {
  for(int i=y;i<M;++i) if(s[x][i] != '?') return i;
  for(int i=y;i>=0;--i) if(s[x][i] != '?') return i;
  return -1;
}

int main() {
  cin >> T;
  while(T--) {
    ++tt;
    cin >> N >> M;
    FOR(i,N) {
      cin >> s[i];
    }
    int ok = 0;
    FOR(i,N) {
      int pos = get(i,0);
      if(pos!=-1) {
        FOR(j,M) {
          pos = get(i,j);
          ok = 1;
          s[i][j] = s[i][pos];
          
        }
      } else {
        if(ok) {
          FOR(j,M) {
            s[i][j] = s[i-1][j];
          }
        }
      }
    }
    for(int i=N-1;i>=0;--i) {
      int pos = get(i,0);
      if(pos!=-1) {
        FOR(j,M) {
          pos = get(i,j);
          s[i][j] = s[i][pos];
        }
      } else {
        if(ok)
        FOR(j,M) {
          s[i][j] = s[i+1][j];
        }
      }
    }
    cout << "Case #" << tt << ":\n";
    FOR(i,N) cout << s[i] << "\n";
    
  } 
}
