#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;
const int MAXN = 222;
int uN,vN;
int g[MAXN][MAXN];
int linker[MAXN];
bool used[MAXN];
int tot;

void show()
{
    printf("\ngraph:\n");
    for (int u=0;u<uN;u++) {
        for (int v=0;v<vN;v++) printf("%d ",g[u][v]);
        puts("");
    }
    printf("-----\n");
}
bool dfs(int u)
{
    for (int v=0;v<vN;v++) {
        if (g[u][v] && !used[v]) {
            used[v] = true;
            if (linker[v] == -1 || dfs(linker[v])) {
                linker[v] = u;
                return true;
            }
        }
    }
    return false;
}
int hungary()
{
    int res = 0;
    memset(linker,-1,sizeof(linker));
    for (int u=0;u<uN;u++) {
        memset(used,false,sizeof(used));
        if (dfs(u)) res++;
    }
    return res;
}
int T_T,n,m;
char op[11111][3];
int r[11111],c[11111];
char s[111][111],t[111][111];
int main(void)
{
//    freopen("D-large.in","r",stdin);
//    freopen("out-large.txt","w",stdout);
    scanf("%d",&T_T);
    for (int cas=1;cas<=T_T;cas++)
    {

        memset(s,0,sizeof(s));
        memset(t,0,sizeof(t));
        printf("Case #%d: ",cas);
        scanf("%d%d",&n,&m);
        for (int i=0;i<m;i++) {
            scanf("%s%d%d",op[i],&r[i],&c[i]);
            s[r[i]][c[i]] = t[r[i]][c[i]] = op[i][0];
        }
        //x
        uN = vN = n;
        for (int u=0;u<uN;u++) for (int v=0;v<vN;v++) g[u][v] = 1;
        for (int i=0;i<m;i++) {
            if (op[i][0] == 'x' || op[i][0] == 'o') {
                int uu = r[i]-1, vv = c[i]-1;
                for (int u=0;u<uN;u++) g[u][vv] = 0;
                for (int v=0;v<vN;v++) g[uu][v] = 0;
            }
        }
//        show();
        hungary();
//        for (int i=0;i<vN;i++) if (linker[i] != -1) printf("%d - %d\n",i,linker[i]);
        for (int i=0;i<vN;i++) if (linker[i] != -1)
        {
            int x = linker[i] + 1, y = i+1;
            if (s[x][y] == '+') s[x][y] = 'o';
            else s[x][y] = 'x';
        }

        //+
        uN = vN = 2*n-1;
        memset(g,0,sizeof(g));

        for (int i=1;i<=n;i++) for (int j=1;j<=n;j++) {
            g[i+j-2][i-j-(-n+1)] = 1;
        }
        for (int i=0;i<m;i++) {
            if (op[i][0] == '+' || op[i][0] == 'o') {
                int uu = r[i]+c[i] - 2, vv = r[i]-c[i] - (-n+1);
                for (int u=0;u<uN;u++) g[u][vv] = 0;
                for (int v=0;v<vN;v++) g[uu][v] = 0;
            }
        }
        hungary();
        for (int i=0;i<vN;i++) if (linker[i] != -1)
        {
            int x = (linker[i]+i-n+3)/2, y = (linker[i]-i+1+n)/2;
            if (s[x][y] == 'x') s[x][y] = 'o';
            else s[x][y] = '+';
        }
        int sum = 0, ans = 0;
        for (int i=1;i<=n;i++) for (int j=1;j<=n;j++)
        {
            if (s[i][j] == '+' || s[i][j] == 'x') sum++;
            else if (s[i][j] == 'o') sum += 2;
            if (s[i][j] != t[i][j]) {
                op[ans][0] = s[i][j];
                r[ans] = i;
                c[ans] = j;
                ans++;
            }
        }
        printf("%d %d\n",sum,ans);
        for (int i=0;i<ans;i++) {
            printf("%c %d %d\n",op[i][0],r[i],c[i]);
        }
    }
    return 0;
}
