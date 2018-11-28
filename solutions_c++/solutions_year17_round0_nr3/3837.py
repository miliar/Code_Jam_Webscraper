
#include <bits/stdc++.h>
using namespace std;
#define MOD 1000000007
#define pii pair<int, int>
#define pll pair<long long, long long>
#define V  vector
#define pb  push_back
#define mp  make_pair
#define pq priority_queue
#define FIN(x) freopen(x,"r",stdin)
#define FOUT(x) freopen(x,"w",stdout)
#define ALL(x) x.begin(),x.end()
#define M(a,x) memset(a,x,sizeof(a))
#define S(x) scanf("%d",&x)
#define Sl(x) scanf("%lld",&x)
#define scs(x) scanf("%s",x);
#define SZ(x) (int)x.size()
#define print(x) printf("%d",x);
#define nl printf("\n")
#define fr first
#define se second
#define printl(x) printf("%lld",x)
#define F(i,a,n) for(int i=a;i<n;i++)
#define INF 4000000000000000000LL
#define LL long long

const int N = 1e5+5;

int cs = 0;
struct cmp {
  bool operator() ( const pii &a, const pii &b) {
    if(a.se-a.fr+1 == b.se-b.fr+1) return a.fr < b.fr;
    return (a.se-a.fr+1 > b.se-b.fr+1);
  }
};
set < pii , cmp > s;
int main() {
  FIN("sm32.in");
  FOUT("sm32.out");
  int t;
  S(t);
  while(t--) {
    s.clear();
    int n,k;
    cin >> n >> k;
    int loc;
    pair<int,int> T;
    s.insert(make_pair(1,n+2));
    for(int i = 1 ; i <= k ; i++) {
      int ans = -1;
      int ans2 = -1;
	pii temp = *(s.begin());
	loc = (temp.fr+temp.se)/2;
	T = temp;
//	cout << temp.fr <<" "<<temp.se << " " << loc << endl;
	/*int mx1 = min(i-temp.fr-1,temp.se-i-1);
	int mx2 = max(i-temp.fr-1,temp.se-i-1);
	if(mx1 > ans) {
	  ans = mx1;
	  T = temp;
	  ans2 = mx2;
	  loc = i;
	}
	else if(mx1 == ans && mx2 > ans2) {
	  ans2 = mx2;
	  T = temp;
	  loc = i;
	}*/
      s.erase(s.find(T));
      s.insert(make_pair(T.fr,loc));
      s.insert(make_pair(loc,T.se));
    }
    printf("Case #%d: ",++cs);
    cout << max(loc-T.fr-1,T.se-loc-1) <<" "<<min(loc-T.fr-1,T.se-loc-1) << endl;
  }
}
