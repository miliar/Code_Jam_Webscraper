#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <ctime>
#include <string>
#include <cstring>
#include <complex>
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
#define mp make_pair

const ll INF_LL = (ll)1e16;
const int INF = (int)1e9;
const int N = 102;
int W, H;
int M;
char s[N][N];
const int DX[] = {1, 0, -1, 0};
const int DY[] = {0, 1, 0, -1};
bool visibleTurr[N][N][N];
int countTurr[N][N];
int sId[N][N], tId[N][N];
int posS[N][2];
int n, m;

int dist[N][N];
int q[N * N][2];
int topQ;

ll a[N][N];
int mt[N];
int way[N];
ll minDist[N];
ll V[N], U[N];
bool used[N];

bool checkCell(int x, int y)
{
    if (x < 0 || x >= W || y < 0 || y >= H) return false;
    return s[x][y] != '#';
}

void read()
{
    scanf("%d%d%d", &H, &W, &M);
    for (int i = 0; i < W; i++)
        scanf("%s", s[i]);
    n = 0;
    m = 0;
    for (int x = 0; x < W; x++)
        for (int y = 0; y < H; y++)
        {
            if (s[x][y] != 'S')
                sId[x][y] = -1;
            else
            {
                posS[n][0] = x;
                posS[n][1] = y;
                sId[x][y] = n++;
            }
            if (s[x][y] != 'T')
                tId[x][y] = -1;
            else
                tId[x][y] = m++;
        }
    for (int x = 0; x < W; x++)
        for (int y = 0; y < H; y++)
            for (int i = 0; i < m; i++)
                visibleTurr[x][y][i] = 0;
    for (int x = 0; x < W; x++)
        for (int y = 0; y < H; y++)
        {
            if (tId[x][y] == -1) continue;
            int id = tId[x][y];
            for (int dir = 0; dir < 4; dir++)
            {
                int nx = x, ny = y;
                while(checkCell(nx, ny))
                {
                    visibleTurr[nx][ny][id] = 1;
                    nx += DX[dir];
                    ny += DY[dir];
                }
            }
        }
    cerr << H << " " << W << "   " << n << " " << m << endl;
    return;
}

void addQ(int x, int y)
{
    q[topQ][0] = x;
    q[topQ][1] = y;
    topQ++;
}

void BFSHung(int x, int y, int id)
{
    topQ = 0;
    for (int i = 0; i < W; i++)
        for (int j = 0; j < H; j++)
            dist[i][j] = INF;
    dist[x][y] = 0;
    addQ(x, y);
    for (int k = 0; k < topQ; k++)
    {
        x = q[k][0];
        y = q[k][1];
        for (int i = 0; i < m; i++)
            if (visibleTurr[x][y][i])
                a[id + 1][i + 1] = min(a[id + 1][i + 1], (ll)dist[x][y]);
        if (dist[x][y] == M) continue;
        for (int dir = 0; dir < 4; dir++)
        {
            int nx = x + DX[dir], ny = y + DY[dir];
            if (!checkCell(nx, ny)) continue;
            if (dist[nx][ny] <= dist[x][y] + 1) continue;
            dist[nx][ny] = dist[x][y] + 1;
            addQ(nx, ny);
        }
    }
    return;
}

void buildHungarian()
{
    for (int i = 0; i <= n; i++)
        for (int j = 0; j <= m; j++)
            a[i][j] = (j == 0 ? 0 : INF);
    for (int x = 0; x < W; x++)
        for (int y = 0; y < H; y++)
        {
            if (sId[x][y] == -1) continue;
            BFSHung(x, y, sId[x][y]);
        }
    return;
}

void hungarian()
{
    
    while(m < n)
    {
        m++;
        for (int i = 0; i <= n; i++)
            a[i][m] = INF;
    }
    while(n < m)
    {
        n++;
        for (int i = 0; i <= m; i++)
            a[n][i] = INF;
    }
    
    for (int i = 0; i <= n; i++)
        V[i] = 0;
    for (int i = 0; i <= m; i++)
        U[i] = 0;
    for (int i = 0; i <= m; i++)
        mt[i] = 0;
    for (int it = 1; it <= n; it++)
    {
        for (int i = 0; i <= m; i++)
        {
            used[i] = 0;
            minDist[i] = INF_LL;
            way[i] = 0;
        }
        int col = 0;
        mt[0] = it;
        while(mt[col])
        {
            int row = mt[col];
            used[col] = 1;
            int ncol = -1;
            ll delta = INF_LL;
            for (int c = 0; c <= m; c++)
            {
                if (used[c]) continue;
                ll newDist = a[row][c] + V[row] + U[c];
                if (newDist < minDist[c])
                {
                    minDist[c] = newDist;
                    way[c] = col;
                }
                if (minDist[c] < delta)
                {
                    delta = minDist[c];
                    ncol = c;
                }
            }
            if (ncol == -1) break;
            for (int c = 0; c <= m; c++)
            {
                if (used[c])
                {
                    V[mt[c]] -= delta;
                    U[c] += delta;
                }
                else
                    minDist[c] -= delta;
            }
            col = ncol;
        }
        if (mt[col]) continue;
        while(col)
        {
            int ncol = way[col];
            mt[col] = mt[ncol];
            col = ncol;
        }
    }
    return;
}

bool BFSRestore(int x, int y, int id)
{
    for (int i = 0; i < W; i++)
        for (int j = 0; j < H; j++)
            dist[i][j] = INF;
    topQ = 0;
    dist[x][y] = 0;
    addQ(x, y);
    for (int k = 0; k < topQ; k++)
    {
        x = q[k][0];
        y = q[k][1];
        if (visibleTurr[x][y][id]) return true;
        if (dist[x][y] == M || countTurr[x][y] > 0) continue;
        for (int dir = 0; dir < 4; dir++)
        {
            int nx = x + DX[dir], ny = y + DY[dir];
            if (!checkCell(nx, ny)) continue;
            if (dist[nx][ny] <= dist[x][y] + 1) continue;
            dist[nx][ny] = dist[x][y] + 1;
            addQ(nx, ny);
        }
    }
    return false;
}

void restoreAns()
{
    
    for (int i = 1; i <= m; i++)
        if (mt[i] && a[mt[i]][i] == INF)
            mt[i] = 0;
            
    for (int x = 0; x < W; x++)
        for (int y = 0; y < H; y++)
        {
            countTurr[x][y] = 0;
            for (int i = 0; i < m; i++)
                if (visibleTurr[x][y][i])
                    countTurr[x][y]++;
        }
    int cnt = 0;
    for (int i = 1; i <= m; i++)
        if (mt[i])
            cnt++;
    printf("%d\n", cnt);
    for (int i = 1; cnt > 0; i = 1 + (i % m))
    {
        if (mt[i] == 0) continue;
        if (!BFSRestore(posS[mt[i] - 1][0], posS[mt[i] - 1][1], i - 1)) continue;
        printf("%d %d\n", mt[i], i);
        cnt--;
        mt[i] = 0;
        for (int x = 0; x < W; x++)
            for (int y = 0; y < H; y++)
            {
                if (visibleTurr[x][y][i - 1])
                {
                    countTurr[x][y]--;
                }
            }
    }
    return;
}

void solve()
{
    read();
    cerr << "READED" << endl;
    buildHungarian();
    cerr << "BUILDED" << endl;
    /*
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= m; j++)
            printf("%d ", a[i][j]);
        printf("\n");
    }
    */
    int oldm = m, oldn = n;
    hungarian();
    m = oldm;
    n = oldn;
    //printf("cost = %d\n", U[0]);
    cerr << "SOLVED" << endl;
    restoreAns();
    cerr << "RESTORED" << endl;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; i++)
    {
        printf("Case #%d: ", i);
        cerr << "Test " << i << endl;
        solve();
    }

    return 0;
}
