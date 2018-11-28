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

char s[25],ans[25];

int main()
{
   freopen ("B-large.in","r",stdin);
    freopen ("A-larg.txt","w",stdout);
    int t,i,n,a;
    scanf("%d",&t);
    for(a=1;a<=t;a++)
    {
        cin>>s;

        n=strlen(s);
        ans[0]=s[0];
        for(i=1;i<n;i++)
        {
            if(s[i]>=s[i-1])
                ans[i]=s[i];
            else
                break;
        }
         printf("Case #%d: ",a);
        if(i==n)
        {
            ans[n]='\0';
            printf("%s\n",ans);
            continue;
        }
        for(;i>0;i--)
        {
            if(s[i]>s[i-1])
            {
                ans[i]--;
                i++;
                for(;i<n;i++)
                    ans[i]='9';
                ans[n]='\0';
                break;
            }
        }
        if(i==0)
        {
            if(s[0]=='1')
            {
                for(i=0;i<n-1;i++)
                    ans[i]='9';
                ans[n-1]='\0';
            }
            else
            {
                ans[0]=s[0]-1;
                for(i=1;i<n;i++)
                    ans[i]='9';
                ans[n]='\0';
            }
        }

        printf("%s\n",ans);
    }
    return 0;
}
