#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<ll, char> P;
typedef pair<ll, P> PPI;

#define fi first
#define se second
#define repl(i,a,b) for(ll i=(ll)(a);i<(ll)(b);i++)
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

#define INF INT_MAX/3

int main(){
	cin.sync_with_stdio(false);
  int cases;
  cin>>cases;
  rep(hoge,cases){
    ll n,r,o,y,g,b,v;
    cin>>n>>r>>o>>y>>g>>b>>v;
    bool ok=true;
    if(r==g&&n==r+g){
      string res;
      rep(i,n){
        if(i%2==0)res+='R';
        else res+='G';
      }
      printf("Case #%lld: %s\n", hoge+1,res.c_str());
      continue;
    }
    if(y==v&&n==y+v){
      string res;
      rep(i,n){
        if(i%2==0)res+='Y';
        else res+='V';
      }
      printf("Case #%lld: %s\n", hoge+1,res.c_str());
      continue;
    }
    if(b==o&&n==b+o){
      string res;
      rep(i,n){
        if(i%2==0)res+='B';
        else res+='O';
      }
      printf("Case #%lld: %s\n", hoge+1,res.c_str());
      continue;
    }
    if(r>=g+1){
      r-=g;
    }else if(g>0) ok=false;

    if(y>=v+1){
      y-=v;
    }else if(v>0)ok=false;

    if(b>=o+1){
      b-=o;
    }else if(o>0)ok=false;

    if(!ok){
      printf("Case #%lld: IMPOSSIBLE\n", hoge+1);
    }else{
      string res;
      P ns[]={P(r,'R'),P(y,'Y'),P(b,'B')};
      sort(ns,ns+3,greater<P>());
      if(ns[2].fi+ns[1].fi<ns[0].fi)ok=false;
      if(!ok){
        printf("Case #%lld: IMPOSSIBLE\n", hoge+1);
      }else{
        string res[3];
        rep(i,ns[0].fi)res[0]+=ns[0].se;
        int rest=ns[2].fi;
        rep(i,ns[0].fi){
          if(i<ns[1].fi){
            res[1]+=res[0][i];
            res[1]+=ns[1].se;
          }else if(i<ns[1].fi+ns[2].fi){
            res[1]+=res[0][i];
            res[1]+=ns[2].se;
            rest--;
          }
        }
        rep(i,res[1].length()){
          if(rest>0){
            res[2]+=res[1][i];
            res[2]+=ns[2].se;
            rest--;
          }else res[2]+=res[1][i];
        }
        string ress;
        rep(i,res[2].length()){
          if(res[2][i]=='R'&&g>0){
            while(g>0){
              ress+="RG";g--;
            }
            ress+="R";
          }else if(res[2][i]=='Y'&&v>0){
            while(v>0){
              ress+="YV";v--;
            }
            ress+="Y";
          }else if(res[2][i]=='B'&&o>0){
            while(o>0){
              ress+="BO";o--;
            }
            ress+="B";
          }else ress+=res[2][i];
        }
        printf("Case #%lld: %s\n", hoge+1,ress.c_str());
      }
    }
  }
	return 0;
}
