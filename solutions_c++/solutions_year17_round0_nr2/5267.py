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

bool check(ll i) {
  stringstream ss;
  ss << i;
  string s;
  ss >> s;
  rep(i,(int)s.size()-1) {
    if( s[i] > s[i+1] ) return false;
  }
  return true;
}

ll bf(string s) {
  ll v = atoll(s.c_str());
  for(ll i=v;i>=0;--i) {
    if( check(i) ) {
      return i;
    }
  }
  return -1;
}

bool dp[20][10][2];
int pre[20][10][2];
string ans;

bool dfs(int cur,int digit,bool free,string &s) {
  if( cur >= (int)s.size() ) {
    return true;
  }
  for(int ndigit=9;ndigit>=0;--ndigit) {
    if( digit > ndigit ) continue;
    if( free ) {
      if( dfs(cur+1,ndigit,free,s) ) {
	ans += string(1,'0'+ndigit);
	return true;
      }
    } else {
      if( s[cur]-'0' < ndigit ) continue;
      bool nfree;
      if( s[cur]-'0' == ndigit ) nfree = false;
      else                       nfree = true;
      if( dfs(cur+1,ndigit,nfree,s) ) {
	ans += string(1,'0'+ndigit);
	return true;
      }
    }
  }
  return false;
}

void compute(string s) {
  //cout << bf(s) << endl;
  memset(dp,false,sizeof dp);
  memset(pre,-1,sizeof pre);
  ans = "";

  assert(dfs(0,0,false,s));
  reverse(ans.begin(),ans.end());
  cout << atoll(ans.c_str()) << endl;
  return;

  int n = s.size();
  dp[n][9][0] = true;
  for(int i=n;i>=1;--i) {
    rep(j,10) {
      rep(k,2) {
	if( !dp[i][j][k] ) continue;
	rep(l,10) {
	  if( k == 0 ) { // まだ N と一致している : 使えるのはs[i-1]

	  } else { // 一致していない : 自由に使える

	  }
	}
      }
    }
  }
  
}

int main() {
  int T,CNT = 1;
  cin >> T;
  while( T-- ) {
    string s;
    cin >> s;
    cout << "Case #" << CNT++ << ": ";
    compute(s);
  }
  return 0;
}
