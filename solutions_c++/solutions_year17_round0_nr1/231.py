#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define rep(i, from, to) for (int i = from; i < (to); ++i)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
#define FOR(i, to) for (int i = 0; i < (to); ++i)


typedef vector<string> vs;
typedef vector<long long> vll;
typedef vector<vector<int> > vvi;
typedef vector<vll> vvll;
typedef vector<pair<int, int> > vpi;
typedef pair<double,double> pdd;
typedef pair<ll,ll> pll;


int N, tt, T;
string S;
int main() {
  cin >> T;
  while(T--) {
    ++tt;
    cin >> S >> N;
    int ret = 0;
    for(int i=0;i<sz(S) - N+1;++i) {
      if(S[i] == '-') {
        ++ret;
        for(int j=0;j<N;++j) {
          if(S[i+j] == '-') S[i+j] = '+';
          else S[i+j] = '-';
        }
      }
      //cout << S << endl;
    }
    cout << "Case #" << tt <<": ";
    int ok = 1;
    for(auto x : S) {
      if(x == '-') ok = 0;
    }
    if(!ok) {
      cout << "IMPOSSIBLE\n";
    } else {
      cout << ret << "\n";
    }
  }
}
