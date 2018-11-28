#include <bits/stdc++.h>

using namespace std;

#define FILE_IO

typedef pair<int, int> pii;

int cx[] = {-1, 1, 0, 0};
int cy[] = {0, 0, -1, 1};
int nxtfs[] = {3, 2, 1, 0};
int nxtbs[] = {2, 3, 0, 1};

int N, M, K, ok;
int tid;
char s[55][55];
int a[55][55];
int c[55][55];
int id[55][55];
int val[105];
int viz[55][55];
vector <pii> lsr;

bool go(int x, int y, int d)
{
    if(x < 1 || y < 1 || x > N || y > M || a[x][y] == -1)    return true;
    if(a[x][y] == -2)   return false;

    if(a[x][y] == 1)    d = nxtfs[d];
    if(a[x][y] == 2)    d = nxtbs[d];
    if(a[x][y] == 0)    viz[x][y]++;

    return go(x + cx[d], y + cy[d], d);
}

void complete(int x, int y, int d, int add)
{
    if(x < 1 || y < 1 || x > N || y > M || a[x][y] == -1)    return;
    if(a[x][y] == 0)    c[x][y] += add;

    if(a[x][y] == 1)    d = nxtfs[d];
    if(a[x][y] == 2)    d = nxtbs[d];

    complete(x + cx[d], y + cy[d], d, add);
}

bool verif()
{
    int cc[55][55];
    memset(cc, 0, sizeof(cc));

    for(int i = 1; i <= N; i++)
        for(int j = 1; j <= M; j++)
            if(s[i][j] == '-')
            {
                int y = j - 1;
                while(s[i][y] == '.')   cc[i][y]++, y--;
                if(s[i][y] == '-' || s[i][y] == '|')    return false;
                y = j + 1;
                while(s[i][y] == '.')   cc[i][y]++, y++;
                if(s[i][y] == '-' || s[i][y] == '|')    return false;
            }
            else if(s[i][j] == '|')
            {
                int x = i - 1;
                while(s[x][j] =='.')    cc[x][j]++, x--;
                if(s[x][j] == '-' || s[x][j] == '|')    return false;
                x = i + 1;
                while(s[x][j] == '.')   cc[x][j]++, x++;
                if(s[x][j] == '-' || s[x][j] == '|')    return false;
            }

    for(int i = 1; i <= N; i++)
        for(int j = 1; j <= M; j++)
            if(s[i][j] == '.' && cc[i][j] == 0)
                return false;
    return true;
}

void bck(int pas)
{
    if(pas >= K)
    {
        for(int i = 1; i <= N; i++)
            for(int j = 1; j <= M; j++)
                if(a[i][j] == 0 && c[i][j] == 0)    return;

        printf("POSSIBLE\n");
        for(int i = 1; i <= N; i++)
            printf("%s\n", s[i] + 1);

        assert( verif() );

        ok = 1;
        return;
    }

    int i = pas;
    val[i] = 0;
    int x = lsr[i].first;
    int y = lsr[i].second;
    s[x][y] = '-';
    if( go(x, y - 1, 2) && go(x, y + 1, 3) )
    {
        complete(x, y - 1, 2, +1);
        complete(x, y + 1, 3, +1);

        bck(pas + 1);
        if(ok)  return;

        complete(x, y - 1, 2, -1);
        complete(x, y + 1, 3, -1);
    }

    val[i] = 1;
    s[x][y] = '|';
    if( go(x - 1, y, 0) && go(x + 1, y, 1) )
    {
        complete(x - 1, y, 0, +1);
        complete(x + 1, y, 1, +1);

        bck(pas + 1);
        if(ok)  return;

        complete(x - 1, y, 0, -1);
        complete(x + 1, y, 1, -1);
    }
}

void solve_test(int testId)
{
    tid = testId;
    printf("Case #%d: ", testId);

    memset(s, 0, sizeof(s));
    memset(a, 0, sizeof(a));
    memset(c, 0, sizeof(c));
    memset(viz, 0, sizeof(viz));
    memset(id, 0, sizeof(id));
    memset(val, 0, sizeof(val));
    lsr.clear();

    scanf("%d%d\n", &N, &M);
    for(int i = 1; i <= N; i++)
        gets(s[i] + 1);

    for(int i = 1; i <= N; i++)
        for(int j = 1; j <= M; j++)
        {
            if(s[i][j] == '.')  a[i][j] = 0;
            else if(s[i][j] == '#') a[i][j] = -1;
            else if(s[i][j] == '/') a[i][j] = 1;
            else if(s[i][j] == '\\') a[i][j] = 2;
            else if(s[i][j] == '-' || s[i][j] == '|')   { a[i][j] = -2; lsr.push_back({i, j}); id[i][j] = lsr.size() - 1; val[ id[i][j] ] = -1;  }
        }

    for(int i = 0; i < lsr.size(); i++)
    {
        int x = lsr[i].first;
        int y = lsr[i].second;
        bool hrz = go(x, y - 1, 2) && go(x, y + 1, 3);
        bool vrt = go(x - 1, y, 0) && go(x + 1, y, 1);
        if(!hrz && !vrt)
        {
            printf("IMPOSSIBLE\n");
            return;
        }
        if(!hrz)
        {
            complete(x - 1, y, 0, 1);
            complete(x + 1, y, 1, 1);
            lsr.erase(lsr.begin() + i);
            i--;
            id[x][y] = -1;
            s[x][y] = '|';
            continue;
        }
        if(!vrt)
        {
            lsr.erase(lsr.begin() + i);
            i--;
            id[x][y] = -1;
            s[x][y] = '-';
            continue;
        }
    }

    for(int i = 1; i <= N; i++)
        for(int j = 1; j <= M; j++)
            if(a[i][j] == 0 && viz[i][j] == 0)
            {
                printf("IMPOSSIBLE\n");
                return;
            }

    ok = 0; K = lsr.size();
    bck(0);

    if(ok == 0) printf("IMPOSSIBLE\n");
}

int main()
{
    #ifdef FILE_IO
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);
    #endif

    int T;
    cin >> T;
    for(int t = 1; t <= T; t++)
        solve_test(t);

    return 0;
}
