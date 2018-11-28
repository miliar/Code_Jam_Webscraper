#include <bits/stdc++.h>

using namespace std;

int R, C;
char grid[100][100];
int id[100][100];
const int UP=0;
const int DOWN=1;
const int LEFT=2;
const int RIGHT=3;
int dx[4]={-1, 1, 0, 0};
int dy[4]={0, 0, -1, 1};
int t1[4]; // /
int t2[4]; // backslash
vector<int> OR[100][100];
int last[100][100];
#define FALSE(x) ((x)*2)
#define TRUE(x) ((x)*2+1)
// FALSE = -
// TRUE = |
vector<int> adj[50*50*2];
vector<int> adj2[50*50*2];
int idx[50*50*2];
int low[50*50*2];
int now;
vector<int> stk;
int onstk[50*50*2];
int comp[50*50*2];
int ncomp;

void scc(int u)
{
    idx[u]=low[u]=now++;
    stk.push_back(u);
    onstk[u]=1;
    for(auto& v: adj[u])
    {
        if(idx[v]==-1)
        {
            scc(v);
            low[u]=min(low[u], low[v]);
        }
        else if(onstk[v])
            low[u]=min(low[u], idx[v]);
    }
    if(idx[u]==low[u])
    {
        comp[u]=ncomp++;
        while(stk.back()!=u)
        {
            comp[stk.back()]=comp[u];
            onstk[stk.back()]=0;
            stk.pop_back();
        }
        onstk[u]=0;
        stk.pop_back();
    }
}

int go(int x, int y, int dir, int mark=-1, int lst=0)
{
    if(x<0 || x>=R || y<0 || y>=C || grid[x][y]=='#')
        return 0;
    if(grid[x][y]=='-' || grid[x][y]=='|')
        return 1;
    if(grid[x][y]=='.')
    {
        if(mark!=-1)
        {
            OR[x][y].push_back(mark);
            last[x][y]=lst;
        }
    }
    else if(grid[x][y]=='/')
        dir=t1[dir];
    else if(grid[x][y]=='\\')
        dir=t2[dir];
    else
        assert(0);
    return go(x+dx[dir], y+dy[dir], dir, mark, lst);
}

vector<int> order;
int lookup[50*50*2];

void top(int u)
{
    if(lookup[u]!=-1)
        return;
    lookup[u]=0;
    for(auto& v: adj2[u])
        top(v);
    lookup[u]=order.size();
    order.push_back(u);
}

void _main(int TEST)
{
    scanf("%d%d", &R, &C);
    for(int i=0; i<R*C*2; i++)
        adj[i].clear();
    for(int i=0; i<R; i++)
        scanf("%s", grid[i]);
    int N=0;
    for(int i=0; i<R; i++)
        for(int j=0; j<C; j++)
            OR[i][j].clear();
    for(int i=0; i<R; i++)
        for(int j=0; j<C; j++) if(grid[i][j]=='-' || grid[i][j]=='|')
            id[i][j]=N++;
    for(int i=0; i<R; i++)
        for(int j=0; j<C; j++) if(grid[i][j]=='-' || grid[i][j]=='|')
        {
            if(!(go(i-1, j, UP, -1) || go(i+1, j, DOWN, -1)))
            {
                go(i-1, j, UP, id[i][j], 1);
                go(i+1, j, DOWN, id[i][j], 1);
            }
            else
                adj[TRUE(id[i][j])].push_back(FALSE(id[i][j]));
        }
    for(int i=0; i<R; i++)
        for(int j=0; j<C; j++) if(grid[i][j]=='-' || grid[i][j]=='|')
        {
            if(!(go(i, j-1, LEFT, -1) || go(i, j+1, RIGHT, -1)))
            {
                go(i, j-1, LEFT, id[i][j], 0);
                go(i, j+1, RIGHT, id[i][j], 0);
            }
            else
                adj[FALSE(id[i][j])].push_back(TRUE(id[i][j]));
        }
    for(int i=0; i<R; i++)
        for(int j=0; j<C; j++) if(grid[i][j]=='.')
        {
            if(OR[i][j].empty())
            {
                printf("IMPOSSIBLE\n");
                return;
            }
            assert(OR[i][j].size()<=2);
            if(OR[i][j].size()==1)
            {
                int x=OR[i][j][0];
                if(last[i][j]==0)
                    adj[TRUE(x)].push_back(FALSE(x));
                else
                    adj[FALSE(x)].push_back(TRUE(x));
            }
            else
            {
                int x=OR[i][j][0];
                int y=OR[i][j][1];
                adj[FALSE(x)].push_back(FALSE(y));
                adj[TRUE(y)].push_back(TRUE(x));
            }
        }
    for(int i=0; i<N*2; i++)
        idx[i]=low[i]=-1, onstk[i]=0, adj2[i].clear(), lookup[i]=-1;
    order.clear();
    now=0;
    ncomp=0;
    stk.clear();
    for(int i=0; i<N*2; i++) if(idx[i]==-1)
        scc(i);
    for(int i=0; i<N; i++) if(comp[FALSE(i)]==comp[TRUE(i)])
    {
        printf("IMPOSSIBLE\n");
        return;
    }
    for(int i=0; i<N*2; i++)
        for(int j: adj[i])
            adj2[comp[i]].push_back(comp[j]);
    for(int i=0; i<ncomp; i++)
    {
        sort(adj2[i].begin(), adj2[i].end());
        adj2[i].erase(unique(adj2[i].begin(), adj2[i].end()), adj2[i].end());
    }
    for(int i=0; i<ncomp; i++)
        top(i);
    for(int i=0; i<R; i++)
        for(int j=0; j<C; j++) if(grid[i][j]=='-' || grid[i][j]=='|')
        {
            int x=id[i][j];
            if(lookup[comp[FALSE(x)]]>lookup[comp[TRUE(x)]])
                grid[i][j]='|';
            else
                grid[i][j]='-';
        }
    printf("POSSIBLE\n");
    for(int i=0; i<R; i++)
        printf("%s\n", grid[i]);
}

int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    t1[RIGHT]=UP;
    t1[UP]=RIGHT;
    t1[LEFT]=DOWN;
    t1[DOWN]=LEFT;
    t2[LEFT]=UP;
    t2[UP]=LEFT;
    t2[RIGHT]=DOWN;
    t2[DOWN]=RIGHT;
    int TEST;
    scanf("%d", &TEST);
    for(int i=1; i<=TEST; i++)
    {
        //cerr << i << endl;
        printf("Case #%d: ", i);
        _main(i);
    }
    return 0;
}
