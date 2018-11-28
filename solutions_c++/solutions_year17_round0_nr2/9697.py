#include<set>
#include<map>
#include<list>
#include<stack>
#include<queue>
#include<ctime>
#include<cmath>
#include<vector>
#include<cstdio>
#include<string>
#include<cstring>
#include<iostream>
#include<algorithm>
#define X first
#define Y second
#define sc scanf
#define pr printf
#define MP make_pair
#define PB push_back
#define lson l,m,i<<1
#define rson m+1,r,i<<1|1
#define mem(a,b) memset(a,b,sizeof(a))
using namespace std;

typedef double db;
typedef long long ll;

const int N=22;

ll p10[N];
char s[N];

bool judge(ll n)
{
    char s[N];
    sprintf(s,"%lld",n);
    int l=strlen(s);

    for(int i=0;i<l;i++)
    {
        if(i+1<l && s[i]>s[i+1]) break;
        if(i+1==l) return 1;
    }
    return 0;
}

int main()
{
    #ifdef Jove
    freopen("B-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    #endif // Jove

    p10[0]=1;
    for(int i=1;i<18;i++)
        p10[i]=p10[i-1]*(ll)10;

    int T;
    sc("%d",&T);
    for(int TT=1;TT<=T;TT++)
    {
        pr("Case #%d: ",TT);

        ll n;
        sc("%lld",&n);
        sprintf(s,"%lld",n);

        int l=strlen(s);

        ll ans=0;

        if(judge(n)) ans=n;

        ll now=0;
        for(int i=0;i<l;i++)
        {
            if(s[i]!='0')
            {
                ll tmp=now*p10[l-i]+(s[i]-'0')*p10[l-i-1]-1;

                if(judge(tmp)) ans=max(ans,tmp);
            }

            now=now*10+s[i]-'0';
        }
        pr("%lld\n",ans);
    }

    return 0;
}

