#include<stdio.h>
#include<string.h>
using namespace std;
typedef long long ll;
#define INF 0x3f3f3f3f
int K;
char str[1005];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t,tt=0;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%s %d",str,&K);
        printf("Case #%d: ",++tt);
        int n=strlen(str);
        if(K>n)
        {
            int f=1;
            for(int i=0;i<n;i++)
                if(str[i]=='-') f=0;
            if(f) puts("0");
            else puts("IMPOSSIBLE");
        }
        else
        {
            int ans=0;
            for(int i=0;i<n-K+1;i++)
            {
                if(str[i]=='-')
                {
                    ans++;
                    for(int j=0;j<K;j++)
                    {
                        if(str[i+j]=='-') str[i+j]='+';
                        else str[i+j]='-';
                    }
                }
            }
            int f=1;
            for(int i=n-K+1;i<n;i++)
                if(str[i]=='-') f=0;
            if(f) printf("%d\n",ans);
            else puts("IMPOSSIBLE");
        }
    }
    return 0;
}
