#include <cstdio>
#include <algorithm>

using namespace std;

int d[101][101][101][101],v[5];

int main()
{
    freopen("file.in", "r", stdin);
    freopen("file.out", "w", stdout);
    int test;
    scanf("%d",&test);
    for(int t=1;t<=test;t++)
    {
        int n,p,x;
        scanf("%d%d",&n,&p);
        for(int i=0;i<4;i++) v[i]=0;
        for(int i=1;i<=n;i++)
        {
            scanf("%d",&x);
            v[x%p]++;
        }
        for(int i=0;i<=v[0];i++)
            for(int j=0;j<=v[1];j++)
                for(int k=0;k<=v[2];k++)
                    for(int q=0;q<=v[3];q++)
                    {
                        d[i][j][k][q]=0;
                        if(i>0) d[i][j][k][q]=max(d[i][j][k][q],d[i-1][j][k][q]+(((j+2*k+3*q)%p)==0));
                        if(j>0) d[i][j][k][q]=max(d[i][j][k][q],d[i][j-1][k][q]+(((j-1+2*k+3*q)%p)==0));
                        if(k>0) d[i][j][k][q]=max(d[i][j][k][q],d[i][j][k-1][q]+(((j+2*(k-1)+3*q)%p)==0));
                        if(q>0) d[i][j][k][q]=max(d[i][j][k][q],d[i][j][k][q-1]+(((j+2*k+3*(q-1))%p)==0));
                    }
        printf("Case #%d: %d\n",t,d[v[0]][v[1]][v[2]][v[3]]);
    }
    return 0;
}
