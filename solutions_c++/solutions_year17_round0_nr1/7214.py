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

string s;
int b[1005];
int main()
{
   freopen ("A-large.in","r",stdin);
    freopen ("A-large1.txt","w",stdout);
    int t,i,k,p,n,j,a;
    scanf("%d",&t);
    for(a=1;a<=t;a++)
    {
        cin>>s>>k;
        n=s.size();
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
        bool flag=0;
        for(;i<n;i++)
            if(b[i]==-1)
            {
                printf("IMPOSSIBLE\n");
                flag=1;
                break;
            }

        if(flag==0)
        printf("%d\n",p);
    }
    return 0;
}
