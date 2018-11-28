#include<bits/stdc++.h>
using namespace std;


vector<pair<int, int> > NRook;
vector<pair<int, int> > NBishop;

int N, M;
char T[10101];
int R[10101];
int C[10101];
bool usedx[1010];
bool usedy[1010];
vector<int> conn[4040];
int from[101010];
int to[101010];
int flow[101010];
int weight[101010];
int ENo = 0;
int pmapV[1010][1010];
int mapV[1010][1010];
bool noc[1010][1010];
bool usedipj[10101];
void init()
{
    memset(usedipj, false, sizeof(usedipj));
    memset(noc, true, sizeof(noc));
    memset(mapV, 0, sizeof(mapV));
    memset(pmapV, 0, sizeof(pmapV));
    NRook.clear();
    NBishop.clear();
    memset(usedx, false, sizeof(usedx));
    memset(usedy, false, sizeof(usedy));
    for(int i=0; i<4040; ++i) conn[i].clear();
    ENo = 0;
}

bool visit[4040];
bool dfs(int a, int b)
{
    if(visit[a]) return false;
    visit[a] = true;
    if(a==b)
    {
        return true;
    }
    for(int E: conn[a])
    {
        if(from[E] == a && flow[E] == 0)
        {
            if(dfs(to[E], b))
            {
                flow[E] = 1;
                return true;
            }
        }
        if(to[E] == a && flow[E] == 1)
        {
            if(dfs(from[E], b))
            {
                flow[E] = 0;
                return true;
            }
        }
    }
    return false;
}
int doFlow(int a, int b)
{
    for(int i=1; i<=4*N; ++i) visit[i] = false;
    int ans = 0;
    while(dfs(a, b))
    {
        ans++;
        for(int i=1; i<=4*N; ++i) visit[i] = false;
    }
    return ans;
}
int value;
void connect(int a, int b, int c)
{
    conn[a].push_back(ENo);
    conn[b].push_back(ENo);
    from[ENo] = a;
    to[ENo] = b;
    flow[ENo] = 0;
    weight[ENo] = c;
    ENo++;
}
void Bishop()
{
    for(int i = 2; i <= 2*N; ++i)
        if(!usedipj[i])
            connect(1, i, 1);
    for(int i = 2*N+1; i <= 4*N-1; ++i)
        if(!usedipj[i])
            connect(i, 4*N, 1);
    for(int i=1; i<=N; ++i)
        for(int j=1; j<=N; ++j)
            if(noc[i][j])
                connect(i+j, i-j+3*N, 1);
    value = doFlow(1, 4 * N) + N;
    for(int i=0; i<ENo; ++i)
    {
        if(from[i]!=1 && to[i] != 4*N && flow[i] != 0) 
        {
            int xpy = from[i];
            int xmy = to[i] - 3*N;
            int x = (xpy+xmy)/2;
            int y = (xpy-xmy)/2;
            NBishop.emplace_back(x, y);
        }
    }
}
void Rook()
{
    int pti = 1, ptj = 1;
    while(pti<=N && ptj<=N)
    {
        if(usedx[pti])
        {
            ++pti; continue;
        }
        if(usedy[ptj])
        {
            ++ptj; continue;
        }
        NRook.emplace_back(pti++, ptj++);
    }
}
void tmain(int tc)
{
    init();
    scanf("%d%d",&N,&M);
    for(int i=0; i<M; ++i)
    {
        scanf(" %c %d %d", T+i, R+i, C+i);
        if(T[i] != '+')
        {
            usedx[R[i]] = usedy[C[i]] = true;
            NRook.emplace_back(R[i], C[i]);
        }
        if(T[i] != 'x')
        {
            NBishop.emplace_back(R[i], C[i]);
            noc[R[i]][C[i]] = false;
            usedipj[R[i]+C[i]]= true;
            usedipj[R[i]-C[i]+3*N] = true;
        }
        if(T[i]=='o') pmapV[R[i]][C[i]] = 3;
        if(T[i]=='x') pmapV[R[i]][C[i]] = 1;
        if(T[i]=='+') pmapV[R[i]][C[i]] = 2;
    }
    Rook();
    fprintf(stderr,"%d %d %dOK\n", tc, N, M);
    Bishop();
    for(auto x: NRook)
    {
        mapV[x.first][x.second]++;
        fprintf(stderr,"R%d %d\n",x.first, x.second);
    }
    for(auto x: NBishop)
    {
        mapV[x.first][x.second] += 2;
        fprintf(stderr,"B%d %d\n",x.first, x.second);
    }
    int cnt = 0;
    int ans = 0;
    for(int i=1; i<=N; ++i)
        for(int j=1; j<=N; ++j)
        {
            ans += __builtin_popcount(mapV[i][j]);
            if(mapV[i][j]!=pmapV[i][j]) cnt++;
        }
        
    printf("Case #%d: ",tc);
    printf("%d %d\n", ans, cnt);
    for(int i=1; i<=N; ++i)
    {
        for(int j=1; j<=N; ++j)
        {
            if(mapV[i][j] == pmapV[i][j]) continue;
            if(mapV[i][j] == 1) printf("x %d %d\n", i, j);
            if(mapV[i][j] == 2) printf("+ %d %d\n", i, j);
            if(mapV[i][j] == 3) printf("o %d %d\n", i, j);
        }
    }
    return;
}

int main()
{
    int T;
    scanf("%d",&T);
    for(int i=1; i<=T; ++i)
    {
        tmain(i);
    }
}