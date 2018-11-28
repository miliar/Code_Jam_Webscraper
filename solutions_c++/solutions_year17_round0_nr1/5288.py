#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cassert>
#include<cstring>
#include<climits>
#include<sstream>
#include<deque>
#include<queue>
#include<sstream>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<bitset>

#define REP(i,s,n) for(int i=s;i<n;++i)
#define rep(i,n) REP(i,0,n)

using namespace std;

typedef long long ll;

const string NO = "IMPOSSIBLE";

bool check(string s) {
  rep(i,(int)s.size()) if(s[i] == '-') return false;
  return true;
}

void compute(string s,int K) {
  int n = s.size();
  int flip = 0;
  rep(i,n) {
    if( s[i] == '-' && i + K - 1 < n ) {
      ++flip;
      rep(j,K) {
	s[i+j] = ( ( s[i+j] == '-' ) ? '+' : '-' );
      }
    }
  }
  if( check(s) ) cout << flip << endl;
  else cout << NO << endl;
}

int main() {
  int T,CNT=1;
  cin >> T;
  while( T-- ) {
    string s;
    cin >> s;
    int K;
    cin >> K;
    cout << "Case #" << CNT++ << ": ";
    compute(s,K);
  }
  return 0;
}
