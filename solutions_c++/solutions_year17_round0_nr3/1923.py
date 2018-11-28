#include<bits/stdc++.h>
using namespace std;
#define Enter putchar(10)
#define Space putchar(32)
#define MAX(x,y) (((x)>(y))?(x):(y))
#define MIN(x,y) (((x)<(y))?(x):(y))
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define sqr(x) ((x)*(x))
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<pii> vpii;
typedef long long ll;
typedef unsigned long long ull;
template<typename N>N gcd(N a,N b){return b?gcd(b,a%b):a;}
template<typename N>inline int sgn(N a){return a>0?1:(a<0?-1:0);}
const int dx[5]={1,0,-1,0,0},dy[5]={0,1,0,-1,0};
const double pi=acos(-1);
const double eps=1e-8;
const int maxn=1e5+7;
void getre(){int x=0;printf("%d\n",1/x);}
void gettle(){int res=1;while(1)res<<=1;printf("%d\n",res);}
void getole(){char ole[1<<16];for(int i=0;i<1<<16;++i){ole[i]='o';}while(1)puts(ole);}
void getwa(){printf("wawawawawawawawaawa\n");}

map<ll,ll> seg;
map<ll,ll>::iterator iter;
ll n,k,T;
ll maxl,minl;
void solve(){
    seg.clear();
    seg[n]=1;
    while(k>0){
        iter=seg.end();iter--;
        ll l=iter->fi-1,r=l>>1;l-=r;
        if(iter->fi==1){
            maxl=minl=0;break;
        }
        if(iter->se<k){
            k-=iter->se;
            seg[l]+=iter->se;
            iter=seg.end();iter--;
            seg[r]+=iter->se;
            iter=seg.end();iter--;
            seg.erase(iter);
        }else{
            maxl=l;minl=r;break;
        }
    }
}
int main()
{
#ifndef ONLINE_JUDGE
	freopen("C-large.in","r",stdin);
	freopen("data.out","w",stdout);
#endif
    scanf("%lld",&T);
    for (int ti=1;ti<=T;++ti){
        scanf("%lld%lld",&n,&k);
        printf("Case #%d: ",ti);
        solve();
        printf("%lld %lld\n",maxl,minl);
    }
	return 0;
}


