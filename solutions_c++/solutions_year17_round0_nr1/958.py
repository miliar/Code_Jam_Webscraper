#include <bits/stdc++.h>
using namespace std;

#define fi first
#define se second
#define repl(i,a,b) for(int i=(int)(a);i<(int)(b);i++)
#define rep(i,n) repl(i,0,n)
#define each(itr,v) for(auto itr:v)
#define pb(s) push_back(s)
#define mp(a,b) make_pair(a,b)
#define all(x) (x).begin(),(x).end()
#define dbg(x) cout<<#x"="<<x<<endl
#define maxch(x,y) x=max(x,y)
#define minch(x,y) x=min(x,y)
#define uni(x) x.erase(unique(all(x)),x.end())
#define exist(x,y) (find(all(x),y)!=x.end())
#define bcnt(x) bitset<32>(x).count()

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> P;
typedef pair<P, int> PPI;
typedef pair<ll, ll> PL;
typedef pair<P, ll> PPL;

#define INF INT_MAX/3

#define MAX_N 1000

char s[1111];

int main(){
	cin.sync_with_stdio(false);
  int cases;
  cin>>cases;
  repl(hoge,1,cases+1){
    int k;
    cin>>s>>k;
    int n=strlen(s);
    int cnt=0;
    rep(i,n-k+1){
      if(s[i]=='-'){
        cnt++;
        repl(j,i,i+k)s[j]=s[j]=='+'?'-':'+';
      }
    }
    bool ok=true;
    rep(i,n){
      if(s[i]!='+')ok=false;
    }
    if(ok)printf("Case #%d: %d\n", hoge,cnt);
    else printf("Case #%d: IMPOSSIBLE\n", hoge);
  }
	return 0;
}
