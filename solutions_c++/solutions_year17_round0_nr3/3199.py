#include<stdio.h>
#include<iostream>
#include<vector>
#include<stack>
#include<utility>//pair
#include<functional>//greater
#include<queue>
#include<set>
#include<string.h>
#include<algorithm>
#include<math.h>
#define F first
#define S second
#define sd(n) scanf("%d",&n)
#define sdd(m,n) scanf("%d %d",&m,&n)
#define sl(n) scanf("%lld",&n)
#define sll(m,n) scanf("%lld %lld",&m,&n)
#define sc(n) scanf("%c",&n)
#define ss(n) scanf("%s",n)
#define pd(n) printf("%d\n",n)
#define pl(n) printf("%lld\n",n)
#define pc(n) printf("%c ",n)
#define ps(n) printf("%s ",n)
#define NL printf("\n")
#define pb(n) push_back(n)
#define sz size()
#define clr(v,a,b) for(int i=a;i<=b;i++)v[i].clear()
#define all(v) v.begin(),v.end()
#define mod 1000000007//10^9+7
#define pp(a,b) make_pair(a,b)
#include<fstream>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
const int MXN=100005;
int dx[4]={-1,0,0,1};
int dy[4]={0,-1,1,0};
int dxx[8]={0,1,1,1,0,-1,-1,-1};
int dyy[8]={1,1,0,-1,-1,-1,0,1};
int main()
{
    //freopen("C-large.in","r",stdin);
    //freopen("out3l.txt","w",stdout);

    int t;
    sd(t);
    for(int tc=1;tc<=t;tc++)
    {
        ll n,k;
        sll(n,k);
        ll mn=0,mx=0;
        if(n>=k)
        {
            ll x=n-k;
            ll y=0;
            while(k)
            {
                y=k;
                k=k&(k-1);
            }
            ll s=x/y;
            ll two=(ll)2;
            if(s%2)
            {
                mn=(s/two);
                mx=(s/two)+1;
            }
            else
            {
                mn=(s/two);
                mx=(s/two);
            }
        }
        printf("Case #%d: %lld %lld\n",tc,mx,mn);
    }
    return 0;
}




