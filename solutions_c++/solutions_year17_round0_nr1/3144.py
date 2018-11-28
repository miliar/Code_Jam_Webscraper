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
char s[1003];
int ar[1003]={0};
int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("out1l.txt","w",stdout);
    int t;
    sd(t);
    for(int tc=1;tc<=t;tc++)
    {
        ss(s);
        int k;
        sd(k);
        int l=strlen(s);
        int ans=0;
        int i;
        for(i=0;i+k<=l;i++)
        {
            int cr=0;
            if(i)
                cr=ar[i-1];
            if(i>=k)
                cr=cr^ar[i-k];
            int x=(s[i]=='+')?0:1;
            int fl=cr^x;
            ans+=fl;
            ar[i]=fl^ar[i-1];
        }
        bool pos=1;
        while(i<l)
        {
            int cr=ar[i-1];
            if(i>=k)
                cr=cr^ar[i-k];
            int x=(s[i]=='+')?0:1;
            int fl=cr^x;
            if(fl)
            {
                pos=0;break;
            }
            ar[i]=ar[i-1];
            i++;
        }
        if(pos)
            printf("Case #%d: %d\n",tc,ans);
        else
            printf("Case #%d: IMPOSSIBLE\n",tc);
    }
    return 0;
}


