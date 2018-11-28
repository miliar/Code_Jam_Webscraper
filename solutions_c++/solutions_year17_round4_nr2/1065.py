#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int, int> PI;
const double eps=1e-8;
const int mod=1e9+7;
const double pi=acos(-1.0);
const int N=1e5+5;
const int M=100;
#define INF 0x3f3f3f3f

int n;
map<char,int>Mp1,Mp2;
char boy[1005],girl[1005];
int B_g[1005][1005],G_b_score[1005][1005];
bool mark[1005][1005];
int bg[1005],gb[1005];
struct node
{
    char b,g;
} res[N];
bool cmp(node c,node d)
{
    return c.b<d.b;
}
void stable_marry()
{
    memset(bg,-1,sizeof(bg));
    memset(gb,-1,sizeof(gb));
    memset(mark,false,sizeof(mark));
    queue<int>q;
    while(!q.empty()) q.pop();
    for(int i=1; i<=n; i++)
        q.push(i);
    int head,nxt;
    while(!q.empty())
    {
        head=q.front();
        q.pop();
        for(int i=1; i<=n; i++)
        {
            nxt=B_g[head][i];
            if(mark[head][nxt]) continue;
            mark[head][nxt]=1;
            if(gb[nxt]==-1)
            {
                gb[nxt]=head;
                bg[head]=nxt;
                break;
            }
            else if(G_b_score[nxt][gb[nxt]]<G_b_score[nxt][head])
            {
                q.push(gb[nxt]);
                gb[nxt]=head;
                bg[head]=nxt;
                break;
            }
        }
    }
    return;
}

vector<int> a[1005];
int mmap[1100][1100],vis[550],pre[550];
int dfs(int x)
{
    for(int i=1; i<=n; i++)
    {
        if(!vis[i] && mmap[x][i])
        {
            vis[i]=1;
            if(pre[i]==-1 || dfs(pre[i]))
            {
                pre[i]=x;
                return 1;
            }
        }
    }
    return 0;
}
int x[105], y[105];
int v[1005],per[1005];
vector<int> g[1005];
int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    int t,ca=1;
    scanf("%d", &t);
    while(t--)
    {
        int n, c, m;
        scanf("%d%d%d", &n, &c, &m);
        printf("Case #%d: ", ca++);
        int mx=0;
        memset(v,0,sizeof v);
        memset(per,0,sizeof per);
        for(int i=0;i<m;i++)
        {
            int x, y;
            scanf("%d%d", &x, &y);
            per[y]++;
            v[x]++;
            mx=max(per[y],mx);
        }
        int ans=0;
        for(int i=n;i>=1;i--)
        {
            if(v[i]>mx)
            {
                int g=v[i]-mx;
                ans+=g;
                v[i-1]+=g;
            }
        }
        if(v[0])
            mx++, ans=0;
        printf("%d %d\n",mx,ans);
    }
    return 0;
}
/*
*/
