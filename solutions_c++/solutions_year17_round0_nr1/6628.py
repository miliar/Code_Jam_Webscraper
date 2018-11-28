#include <bits/stdc++.h>
#include<string.h>
#define MOD 1000000009
#define MAXA 10000000000000ll
#define PI 3.14159265358979323846264338327950
//#define INF 0x3f3f3f3f
typedef long long int ll;
using namespace std;
//const int MAXA= 1e15;
const  int maxn=5e5+5;
const int N=1e6+5;
int dp[1005];
int main()
{
    freopen("AA!.in","r+",stdin);
    freopen("out.txt","w+",stdout);
    int t,k,i,j,t1=1;
    string a;
    cin>>t;
    while(t--)
    {
        cin>>a>>k;
        int ans=0,f=0;
        memset(dp,0,sizeof(dp));
        int n=a.length();
        for(i=0;i<n;i++)
        {
            if(a[i]=='+')
                dp[i]=1;
        }
        for(i=0;i<=n-k;i++)
        {
            if(dp[i]==1)
                continue;
            ans++;
            for(j=i;j<i+k;j++)
                dp[j]=dp[j]^1;
        }
        for(i=0;i<n;i++)
        {
            if(dp[i]==0)
            {
                f=1;
                break;
            }
        }
        printf("Case #%d: ",t1);
        t1++;
        if(f)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n",ans);
    }
    return 0;

}
