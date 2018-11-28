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

char s[100];

int main(){
	cin.sync_with_stdio(false);
  int cases;
  cin>>cases;
  repl(hoge,1,cases+1){
    cin>>s;
    int n=strlen(s);
    int l=0;
    rep(i,n-1){
      if(s[i]>s[i+1]){
        s[l]--;
        repl(j,l+1,n)s[j]='9';
      }else if(s[i]<s[i+1])l=i+1;
    }
    printf("Case #%d: %lld\n", hoge,stoll(s));
  }
	return 0;
}
