#pragma GCC optimize("O3")
#include <bits/stdc++.h>
#define rep(i,n) for(__typeof(n) i=0;i<n;++i)
#define reu(i,s,e) for(__typeof(e) i=s;i<e;++i)
#define each(it,o) for(auto it= (o).begin(); it != (o).end(); ++ it)
#define all(o) (o).begin(), (o).end()
#define F first
#define S second
#define mp make_pair
#define pb push_back
#define mset(m,v) memset(m,v,sizeof(m))
#define INF 0x7fffffff
#define INFL 0x7fffffffffffffffLL
#define inrep int t;cin>>t; while(t--)
using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef vector<pii> vpii;
typedef vector<pll> vpll;
typedef vector<string> vs;
typedef map<int,int> mii;
typedef map<ll,ll> mll;

int t;
ll n,k;
mll r1,r2;
int main(){
      ios_base::sync_with_stdio ( false );
      freopen("C-small-2-attempt0.in","r",stdin);
      freopen("C-small-2.out","w",stdout);
      cin>>t;
      rep(testcase,t){
        cin>>n>>k;
        r2.insert(pll(n,1));
        int level=log2(k);
        rep(i,level){
          r1=r2;
          r2.clear();
          each(it,r1){
            if(it->F & 1) r2.insert(pll((it->F)>>1,0));
            else{
              r2.insert(pll((it->F)>>1,0));
              r2.insert(pll((it->F - 1)>>1,0));
            }
          }
          each(it,r1){
            if(it->F & 1) r2[it->F >> 1]+=(it->S <<1);
            else{
              r2[it->F >> 1]+=(it->S);
              r2[it->F - 1 >> 1]+=(it->S);
            }
          }
        }
        int tmp=k%(1<<level);
        if(r2.size()==1) cout<<"Case #"<<testcase+1<<": "<<(r2.begin()->F >>1)<<" "<<(r2.begin()->F - 1 >>1)<<"\n";
        else{
          if(r2.rbegin()->S > tmp) cout<<"Case #"<<testcase+1<<": "<<(r2.rbegin()->F >>1)<<" "<<(r2.rbegin()->F - 1 >>1) <<"\n";
          else cout<<"Case #"<<testcase+1<<": "<<(r2.begin()->F >>1)<<" "<<(r2.begin()->F - 1 >>1)<<"\n";
        }
        r1.clear();r2.clear();
      }
      return 0;
}
