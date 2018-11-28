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

char b[33][33];

int main(){
	cin.sync_with_stdio(false);
  int cases;
  cin>>cases;
  rep(hoge,cases){
    int h,w;
    cin>>h>>w;
    rep(i,h)cin>>b[i];
    rep(i,h)rep(j,w){
      if(b[i][j]!='?'){
        int k=j-1;
        while(k>=0&&b[i][k]=='?'){
          b[i][k]=b[i][j];
          k--;
        }
        k=j+1;
        while(k<w&&b[i][k]=='?'){
          b[i][k]=b[i][j];
          k++;
        }
      }
    }
    rep(i,h)rep(j,w){
      if(b[i][j]!='?'){
        int k=i-1;
        while(k>=0&&b[k][j]=='?'){
          b[k][j]=b[i][j];
          k--;
        }
        k=i+1;
        while(k<h&&b[k][j]=='?'){
          b[k][j]=b[i][j];
          k++;
        }
      }
    }
    printf("Case #%d:\n", hoge+1);
    rep(i,h)printf("%s\n", b[i]);
  }
	return 0;
}
