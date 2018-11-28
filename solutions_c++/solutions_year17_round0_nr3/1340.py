#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <string.h>
#include <string>
#include <vector>
#include <queue>

#define MEM(a,x) memset(a,x,sizeof a)
#define eps 1e-8
#define MOD 10009
#define MAXN 10010
#define MAXM 100010
#define INF 99999999
#define ll long long
#define bug cout<<"here"<<endl
#define fread freopen("C-large.in","r",stdin)
#define fwrite freopen("out.txt","w",stdout)

using namespace std;

int main()
{
//    fread;
//    fwrite;
    int tc;
    scanf("%d",&tc);
    int cs=1;
    while(tc--)
    {
        ll n,k;
        cin>>n>>k;
        ll step=1;
        while(k>step)
        {
            k-=step;
            step*=2;
            n-=step/2;
        }
        ll ans=n/step;
        if(k<=n%step)
            ans++;
        printf("Case #%d: %lld %lld\n",cs++,ans/2,(ans-1)/2);
    }
    return 0;
}
