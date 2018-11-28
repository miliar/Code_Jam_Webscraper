#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<ll, ll> P;

#define fi first
#define se second
#define repl(i,a,b) for(ll i=(ll)(a);i<(ll)(b);i++)
#define rep(i,n) repl(i,0,n)
#define each(itr,v) for(auto itr:v)
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define dbg(x) cout<<#x"="<<x<<endl
#define mmax(x,y) (x>y?x:y)
#define mmin(x,y) (x<y?x:y)
#define maxch(x,y) x=mmax(x,y)
#define minch(x,y) x=mmin(x,y)
#define uni(x) x.erase(unique(all(x)),x.end())
#define exist(x,y) (find(all(x),y)!=x.end())
#define bcnt __builtin_popcount

#define INF INT_MAX/3

int n;
int g[111];
int p;
int cnt[111];

int main(){
	cin.sync_with_stdio(false);
  int cases;
  cin>>cases;
  repl(hoge,1,cases+1){
    ll res=0;
    cin>>n>>p;
    rep(i,n)cin>>g[i];
    memset(cnt,0,sizeof(cnt));
    rep(i,n){
      cnt[g[i]%p]++;
    }
    if(p==2){
      res=cnt[0]+(cnt[1]+1)/2;
    }else if(p==3){
      ll k=min(cnt[1],cnt[2]);
      cnt[1]-=k;
      cnt[2]-=k;
      res=cnt[0]+k+(cnt[1]+2)/3+(cnt[2]+2)/3;
    }else{
      ll k=min(cnt[1],cnt[3]);
      cnt[1]-=k;
      cnt[3]-=k;
      if(cnt[2]%2==0){
        res=cnt[0]+k+cnt[2]/2+(cnt[1]+3)/4+(cnt[3]+3)/4;
      }else{
        if(max(cnt[1],cnt[3])>=2){
          ll rest=max(cnt[1],cnt[3])-2;
          res=cnt[0]+k+cnt[2]/2+(rest+3)/4+1;
        }else{
          res=cnt[0]+k+cnt[2]/2+1;
        }
      }
    }
    printf("Case #%lld: %lld\n", hoge,res);
  }
	return 0;
}
