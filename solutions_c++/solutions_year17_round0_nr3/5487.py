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

struct Data {
  int Ls,Rs,p;
  bool operator < (const Data &data) const {
    int mini  = min(Ls,Rs);
    int dmini = min(data.Ls,data.Rs);
    if( mini != dmini ) return mini < dmini;
    int maxi  = max(Ls,Rs);
    int dmaxi = max(data.Ls,data.Rs);
    if( maxi != dmaxi ) return maxi < dmaxi;
    return p > data.p;
  }
};

ll N,K;

void bf() {
  //puts("---");
  vector<int> vec(N,-1);
  Data last;
  rep(_,K) {
    Data ans = (Data){-1,-1,-1};
    rep(i,N) {
      if( vec[i] != -1 ) continue;
      int Ls = 0, Rs = 0, p = i;
      int cur = i-1;
      while( cur >= 0 && vec[cur] == -1 ) {
	--cur;
	++Ls;
      }
      cur = i + 1;
      while( cur < N && vec[cur] == -1 ) {
	++cur;
	++Rs;
      }
      Data tmp = (Data){Ls,Rs,p};
      if( ans.Ls == -1 || ans < tmp ) ans = tmp;
    }
    //cout << _ << "-th : " << ans.Ls << " " << ans.Rs << " p = " << ans.p << endl;
    vec[ans.p] = _;
    last = ans;
  }

  //rep(i,N) cout << vec[i] << " "; puts("");
  cout << max(last.Ls,last.Rs) << " " << min(last.Ls,last.Rs) << endl;
}

void compute() {
  bf();

}

int main() {
  int T,CNT=1;
  cin >> T;
  while( T-- ) {
    cin >> N >> K;
    cout << "Case #" << CNT++ << ": ";
    compute();
  }
  return 0;
}
