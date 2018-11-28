#include<bits/stdc++.h>
using namespace std;
#define f first
#define s second
#define ll long long
#define mp make_pair
#define MAX 100005
#define mod 1000000007
#define pb push_back
#define INF 1000005
#define pii pair<int,int>

char s[1005];
int b[1005];

int main()
{
    freopen ("A-large.in","r",stdin);
    freopen ("A-large.txt","w",stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t,i,k,p,n,j,q=0;
    scanf("%d",&t);
    for(int a=1;a<=t;a++)
    {
        scanf("%s%d",s,&k);
        q=0;
        n=strlen(s);
        printf("Case #%d: ",a);
        for(i=0;i<n;i++)
        {
            if(s[i]=='+')
                b[i]=1;
            else
                b[i]=-1;
        }
        p=0;
        for(i=0;i<=n-k;i++)
        {
            if(b[i]==-1)
            {
                for(j=i;j<i+k;j++)
                    b[j]*=-1;
                p++;
            }
        }
        for(;i<n;i++)
            if(b[i]==-1)
            {
                printf("IMPOSSIBLE\n");
                q++;
                break;
            }
        if(q)
            continue;
        printf("%d\n",p);
    }
    return 0;
}
