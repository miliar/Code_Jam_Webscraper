#include<bits/stdc++.h>
#define PB(u)  push_back(u)
#define AA   first
#define BB   second
#define inf 0x3f3f3f3f
using namespace std ;
#define MAX 100005
#define sz size()
typedef long long ll ;
typedef pair<int,int> PII ;
const double eps=1e-8;
const double pi=acos(-1.0);
const int mod=1e9+7;

pair<int,char>  a[10];
char  ans[1005];
bool vis[1005];

int main()
{
    freopen("data.in","r",stdin);
    freopen("data.out","w",stdout);
    int T,cas=1;
    cin>>T;
    while(T--)
    {
        int u,n;
        scanf("%d",&n);
        scanf("%d %d",&a[0].AA,&u);
        scanf("%d %d",&a[1].AA,&u);
        scanf("%d %d",&a[2].AA,&u);
        a[0].BB='R';
        a[1].BB='Y';
        a[2].BB='B';
        sort(a,a+3);
        if(n&1)
        {
            int id=0;
            for(int i=0;i<a[2].AA;i++)
            {
                ans[id]=a[2].BB;
                id=(id+2)%n;
            }
            for(int i=0;i<a[1].AA;i++)
            {
                ans[id]=a[1].BB;
                id=(id+2)%n;
            }
            for(int i=0;i<a[0].AA;i++)
            {
                ans[id]=a[0].BB;
                id=(id+2)%n;
            }
        }
        else
        {
            memset(vis,0,sizeof(vis));
            int id=0;
            for(int i=0;i<a[2].AA;i++)
            {
                if(id==0&&vis[id]) id++;
                ans[id]=a[2].BB;
                vis[id]=1;
                id=(id+2)%n;
            }
            for(int i=0;i<a[1].AA;i++)
            {
                if(id==0&&vis[id]) id++;
                ans[id]=a[1].BB;
                vis[id]=1;
                id=(id+2)%n;
            }
            for(int i=0;i<a[0].AA;i++)
            {
                if(id==0&&vis[id]) id++;
                ans[id]=a[0].BB;
                vis[id]=1;
                id=(id+2)%n;
            }
        }
        if(a[2].AA*2>n)
            printf("Case #%d: IMPOSSIBLE\n",cas++);
        else
        {
            printf("Case #%d: ",cas++);
            for(int i=0;i<n;i++)
                printf("%c",ans[i]);
            printf("\n");
        }
    }
    return 0 ;
}

