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
int T;
ll n;
ll divnum[20];
ll solve(ll n){
    memset(divnum,0,sizeof(divnum));
    for (int i=0;i<=18;++i){
        divnum[i]=n%10;
        n/=10;
    }
    int max9=-1;
    for (int i=0;i<18;++i){
        if(divnum[i]<divnum[i+1]){
            max9=max(max9,i);
            divnum[i+1]--;
        }
    }
    for (int i=0;i<=max9;++i){
        divnum[i]=9;
    }
    ll ans=0;
    for (int i=18;i>=0;--i){
        ans*=10;
        ans+=divnum[i];
    }
    return ans;
}
int main()
{
#ifndef ONLINE_JUDGE
	freopen("B-large.in","r",stdin);
	freopen("data.out","w",stdout);
#endif
    scanf("%d",&T);
    for (int ti=1;ti<=T;++ti){
        scanf("%lld",&n);
        printf("Case #%d: ",ti);
        printf("%lld\n",solve(n));;
    }
	return 0;
}


