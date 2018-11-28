#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
char s[20];int k;
int dis[(1<<10)+10];
int Q[(1<<10)+10];
int dir[20],ndir;
void bfs()
{
    memset(dis,0x3f,sizeof(dis));
    int front=0,rear=0;
    Q[rear++]=0;
    dis[0]=0;
    while(front<rear)
    {
        int p=Q[front++];
        for(int i=0;i<ndir;i++)
        {
            int now=p^dir[i];
            if(dis[now]==0x3f3f3f3f)
            {
                dis[now]=dis[p]+1;
                Q[rear++]=now;
            }
        }
    }
}
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int t;
    scanf("%d",&t);
    int ca=1;
    while(t--)
    {
        scanf("%s%d",s,&k);
        int len=strlen(s);
        int d=(1<<k)-1;ndir=0;
        dir[ndir++]=d;
        for(int i=k;i<len;i++)
        {
            d=d^(1<<i)^(1<<i-k);
            dir[ndir++]=d;
        }
        bfs();
        d=0;
        for(int i=0;i<len;i++)
        {
            d^=(s[i]=='-')<<i;
        }
        if(dis[d]==0x3f3f3f3f)
            printf("Case #%d: IMPOSSIBLE\n",ca++);
        else
            printf("Case #%d: %d\n",ca++,dis[d]);
    }
    return 0;
}
