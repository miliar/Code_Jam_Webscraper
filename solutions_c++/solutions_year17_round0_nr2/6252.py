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

char s[30],s2[30];

int main()
{
    freopen ("B-large.in","r",stdin);
    freopen ("B-large.txt","w",stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t,i,n,j;
    scanf("%d",&t);
    for(j=1;j<=t;j++)
    {
        scanf("%s",s);
        printf("Case #%d: ",j);
        n=strlen(s);
        s2[0]=s[0];
        for(i=1;i<n;i++)
        {
            if(s[i]>=s[i-1])
                s2[i]=s[i];
            else
                break;
        }
        if(i==n)
        {
            s2[n]='\0';
            printf("%s\n",s2);
            continue;
        }
        for(;i>0;i--)
        {
            if(s[i]>s[i-1])
            {
                s2[i]--;
                i++;
                for(;i<n;i++)
                    s2[i]='9';
                s2[n]='\0';
                break;
            }
        }
        if(!i)
        {
            if(s[0]=='1')
            {
                for(i=0;i<n-1;i++)
                    s2[i]='9';
                s2[n-1]='\0';
            }
            else
            {
                s2[0]=s[0]-1;
                for(i=1;i<n;i++)
                    s2[i]='9';
                s2[n]='\0';
            }
        }
        printf("%s\n",s2);
    }
    return 0;
}
