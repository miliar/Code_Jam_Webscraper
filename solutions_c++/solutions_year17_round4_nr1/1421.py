#include<bits/stdc++.h>
using namespace std;
int n,p;
int mem[105][105][105][5];
int f(int a,int b,int c,int left)
{
    if(mem[a][b][c][left]==-1)
    {
        mem[a][b][c][left] = 0;
        if(left==0)
        {
            if(a) mem[a][b][c][left] = max(mem[a][b][c][left],1 + f(a-1,b,c,(left-1+p)%p));
            if(b) mem[a][b][c][left] = max(mem[a][b][c][left],1 + f(a,b-1,c,(left-2+p)%p));
            if(c) mem[a][b][c][left] = max(mem[a][b][c][left],1 + f(a,b,c-1,(left-3+p)%p));
        }
        else
        {
            if(a) mem[a][b][c][left] = max(mem[a][b][c][left],f(a-1,b,c,(left-1+p)%p));
            if(b) mem[a][b][c][left] = max(mem[a][b][c][left],f(a,b-1,c,(left-2+p)%p));
            if(c) mem[a][b][c][left] = max(mem[a][b][c][left],f(a,b,c-1,(left-3+p)%p));
        }
    }
    return mem[a][b][c][left];
}
main()
{
    int T,cnum=1;
    int i,x,a,b,c,ans;
    freopen("A-large.in","r",stdin);
    freopen("A_out.txt","w",stdout);
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d%d",&n,&p);
        ans = a = b = c = 0;
        for(i=1;i<=n;i++)
        {
            scanf("%d",&x);
            if(x%p==0) ans++;
            if(x%p==1) a++;
            if(x%p==2) b++;
            if(x%p==3) c++;
        }
        memset(mem,-1,sizeof(mem));
        printf("Case #%d: %d\n",cnum++,f(a,b,c,0) + ans);
    }
}
