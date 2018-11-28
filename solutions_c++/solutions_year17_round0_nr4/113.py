#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#define LL long long

using namespace std;

const int Maxn=210;
int ans,sum,n,M,g[Maxn][Maxn],Used[Maxn],linker[Maxn],x[Maxn*Maxn],y[Maxn*Maxn];
char Map[Maxn][Maxn],Mapnew[Maxn][Maxn],s[Maxn*Maxn][5];
bool p[Maxn],q[Maxn];

bool dfs(int u)
{
    for (int v=1; v<=2*n; v++) if (g[u][v] && !Used[v])
    {
        Used[v]=true;
        if (linker[v]==-1 || dfs(linker[v]))
        {
            linker[v]=u;
            return true;
        }
    }
    return false;
}

void hungary()
{
    for (int i=1; i<=2*n; i++) linker[i]=-1;
    for (int i=1; i<=2*n; i++)
    {
        for (int j=1; j<=2*n; j++) Used[j]=false;
        dfs(i);
    }
}

int main()
{
    freopen("d.in","r",stdin);
    freopen("d.out","w",stdout);
    int T,w=0;
    for (scanf("%d",&T); T--; )
    {
        scanf("%d%d",&n,&M);
        for (int i=1; i<=n; i++)
        for (int j=1; j<=n; j++) Map[i][j]=Mapnew[i][j]='.';
        for (int i=1; i<=M; i++)
        {
            scanf("%s%d%d",s[i],&x[i],&y[i]);
            Map[x[i]][y[i]]=s[i][0];
            Mapnew[x[i]][y[i]]=s[i][0];
        }
        printf("Case #%d: ",++w);

        for (int i=1; i<=2*n; i++)
        for (int j=1; j<=2*n; j++) g[i][j]=false,p[i]=false,q[i]=false;
        for (int i=1; i<=M; i++) if (s[i][0]=='x' || s[i][0]=='o')
        {
            p[x[i]]=true,q[y[i]]=true;
        }
        for (int i=1; i<=n; i++) if (!p[i])
        for (int j=1; j<=n; j++) if (!q[j]) g[i][j]=true;
        hungary();
        for (int i=1; i<=n; i++)
        {
            //printf("%d %d\n",linker[i],i);
            if (linker[i]!=-1) if (Mapnew[linker[i]][i]=='.') Mapnew[linker[i]][i]='x'; else Mapnew[linker[i]][i]='o';
        }

        for (int i=1; i<=2*n; i++)
        for (int j=1; j<=2*n; j++) g[i][j]=false,p[i]=false,q[i]=false;
        for (int i=1; i<=M; i++) if (s[i][0]=='+' || s[i][0]=='o')
        {
            p[x[i]+y[i]]=true,q[x[i]-y[i]+n]=true;
        }
        for (int i=1; i<=n; i++)
        for (int j=1; j<=n; j++) if (!p[i+j] && !q[i-j+n]) g[i+j][i-j+n]=true;
        hungary();
        for (int i=1; i<=2*n; i++) if (linker[i]!=-1)
        {
            int xx=(linker[i]+i-n)/2,yy=linker[i]-xx;
            //printf("%d %d %d %d\n",linker[i],i,xx,yy);
            if (Mapnew[xx][yy]=='.') Mapnew[xx][yy]='+'; else Mapnew[xx][yy]='o';
        }

        ans=0,sum=0;
        for (int i=1; i<=n; i++)
        for (int j=1; j<=n; j++)
        {
            if (Mapnew[i][j]=='+' || Mapnew[i][j]=='x') ans++; else
                if (Mapnew[i][j]=='o') ans+=2;
            if (Mapnew[i][j]!=Map[i][j]) sum++;
        }
        printf("%d %d\n",ans,sum);
        for (int i=1; i<=n; i++)
        for (int j=1; j<=n; j++) if (Mapnew[i][j]!=Map[i][j]) printf("%c %d %d\n",Mapnew[i][j],i,j);
    }
    return 0;
}
