//// ngmq

#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <sstream>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <cstdlib>
// #include <climits>
// #include <functional>
// #include <ctime>
#include <cmath>
#include <bitset>
// #include <utility>
#include <complex>
#include<fstream>

using namespace std;
typedef long long ll;
typedef unsigned long long ull;
#define inf (1e9 + 1e9)
#define linf 1e18
#define BASE 1000000
#define EPS 1e-10
#define PI acos(-1)
#define pii pair<int,int>
#define vi vector<int>
#define fi first
#define se second
#define ALL(x) (x).begin(), (x).end()
#define ms(x,val) memset(x, val, sizeof(x))
#define pb(x) push_back(x)
#define make_unique(x) sort(ALL(x)) ; x.erase( unique(ALL(x)), x.end()) ;
#define dbg(x) do { cout << #x << " = " << x << endl; } while(0)
#define mp(x, y) make_pair(x, y)

/*** IMPLEMENTATION ***/
bool exitInput = false;
int ntest = 1, itest = 1 ;

const int dx[4] =
{
    1, 0, -1, 0
};
const int dy[4] =
{
    0, 1, 0, -1
};
// const int dx[8] = {-2, -1, -1, +0, +0, +1, +1, +2};
// const int dy[8] = {+0, -1, +1, -2, +2, -1, +1, +0};

/** Knight Move **/
// const int dx[8] = {+1, +2, +2, +1, -1, -2, -2, -1};
// const int dy[8] = {+2, +1, -1, -2, -2, -1, +1, +2};

const char * directions[4] =
{
    "NE", "SE", "Sw", "Nw"
};

const ll Mod = 1000000007LL;
const int maxn = 200000 + 5;
const int maxv = 100000 + 5;
const int maxe = 1000011 + 5;

const int GRASS = -1;

int n, m;
char avail[111][111][3], grid[111][111], original[111][111];

struct Candidate
{
    int nkill;
    int model, value;
    int r, c;
    Candidate()
    {

    }
    Candidate(int _nkill, int _model, int _value, int _r, int _c)
    {
        model = _model;
        nkill = _nkill;
        value = _value;
        r = _r;
        c = _c;
    }
    bool operator <(const Candidate& other) const
    {
        if(nkill != other.nkill)
            return nkill > other.nkill;
        if(value != other.value)
            return value < other.value;
        if(model != other.model)
            return model > other.model;
        if(r != other.r)
            return r > other.r;
        return c > other.c;
    }
};

void setAll(int r, int c, int x)
{
    avail[r][c][0] = avail[r][c][1] = avail[r][c][2] = x;
}

void setEach(int r, int c, int d, int x)
{
    avail[r][c][d] = x;
}

int model2num(char x)
{
    if(x == '+') return 0;
    if(x == 'x') return 1;
    if(x == 'o') return 2;
    return -1;
}
int num2model(int x)
{
    if(x == 0) return '+';
    if(x == 1) return 'x';
    if(x == 2) return 'o';
    return '.';
}

void setKill0(int r, int c, int& cnt, bool isCounting = false)
{
    int i, j, k;
    if(!isCounting)
    {
        setEach(r, c, 0, 0);
        setEach(r, c, 1, 0);
        grid[r][c] = 0;
    }


    i = r; j = c;
    for(--i, --j; i >= 1 && j >= 1; --i, --j)
    {
        if(avail[i][j][0] == 1)
        {
            if(!isCounting)
            {
                setEach(i, j, 0, 0);
            }
            ++cnt;
        }
        if(avail[i][j][2] == 1)
        {
            if(!isCounting)
            {
                setEach(i, j, 2, 0);
            }
            cnt += 2;
        }
    }

    i = r; j = c;
    for(++i, ++j; i <= n && j <= n; ++i, ++j)
    {
        if(avail[i][j][0] == 1)
        {
            if(!isCounting)
            {
                setEach(i, j, 0, 0);
            }
            ++cnt;
        }
        if(avail[i][j][2] == 1)
        {
            if(!isCounting)
            {
                setEach(i, j, 2, 0);
            }
            cnt += 2;
        }
    }

    i = r; j = c;
    for(--i, ++j; i >= 1 && j <= n; --i, ++j)
    {
        if(avail[i][j][0] == 1)
        {
            if(!isCounting)
            {
                setEach(i, j, 0, 0);
            }
            ++cnt;
        }
        if(avail[i][j][2] == 1)
        {
            if(!isCounting)
            {
                setEach(i, j, 2, 0);
            }
            cnt += 2;
        }
    }

    i = r; j = c;
    for(++i, --j; i <= n && j >= 1; ++i, --j)
    {
        if(avail[i][j][0] == 1)
        {
            if(!isCounting)
            {
                setEach(i, j, 0, 0);
            }
            ++cnt;
        }
        if(avail[i][j][2] == 1)
        {
            if(!isCounting)
            {
                setEach(i, j, 2, 0);
            }
            cnt += 2;
        }
    }
}

void setKill1(int r, int c, int& cnt, bool isCounting = false)
{
    int i, j, k;
    if(!isCounting)
    {
        setEach(r, c, 0, 0);
        setEach(r, c, 1, 0);
        grid[r][c] = 1;
    }


    i = r; j = c;
    for(--i; i >= 1 && j >= 1; --i)
    {
        if(avail[i][j][1] == 1)
        {
            if(!isCounting)
            {
                setEach(i, j, 1, 0);
            }
            cnt += 1;
        }
        if(avail[i][j][2] == 1)
        {
            if(!isCounting)
            {
                setEach(i, j, 2, 0);
            }
            cnt += 2;
        }
    }

    i = r; j = c;
    for(++i; i <= n && j <= n; ++i)
    {
        if(avail[i][j][1] == 1)
        {
            if(!isCounting)
            {
                setEach(i, j, 1, 0);
            }
            cnt += 1;
        }
        if(avail[i][j][2] == 1)
        {
            if(!isCounting)
            {
                setEach(i, j, 2, 0);
            }
            cnt += 2;
        }
    }

    i = r; j = c;
    for(++j; i >= 1 && j <= n; ++j)
    {
        if(avail[i][j][1] == 1)
        {
            if(!isCounting)
            {
                setEach(i, j, 1, 0);
            }
            cnt += 1;
        }
        if(avail[i][j][2] == 1)
        {
            if(!isCounting)
            {
                setEach(i, j, 2, 0);
            }
            cnt += 2;
        }
    }

    i = r; j = c;
    for(--j; i <= n && j >= 1; --j)
    {
        if(avail[i][j][1] == 1)
        {
            if(!isCounting)
            {
                setEach(i, j, 1, 0);
            }
            cnt += 1;
        }
        if(avail[i][j][2] == 1)
        {
            if(!isCounting)
            {
                setEach(i, j, 2, 0);
            }
            cnt += 2;
        }
    }
}

void setKill2(int r, int c, int &cnt, bool isCounting = false)
{
    int i, j, k;
    if(!isCounting)
    {
        setEach(r, c, 0, 0);
        setEach(r, c, 1, 0);
        setEach(r, c, 2, 0);
        grid[r][c] = 2;
    }
    setKill0(r, c, cnt, isCounting);
    setKill1(r, c, cnt, isCounting);
    if(!isCounting)
    {
        setEach(r, c, 0, 0);
        setEach(r, c, 1, 0);
        setEach(r, c, 2, 0);
        grid[r][c] = 2;
    }
}


void setKill(int r, int c, int model,  int& cnt, bool isCounting = false)
{
    if(model == 0) setKill0(r, c, cnt, isCounting);
    if(model == 1) setKill1(r, c, cnt, isCounting);
    if(model == 2) setKill2(r, c, cnt, isCounting);
}

void displayAvail()
{
    int i, j;
    for(i = 1; i <= n; ++i)
    {
        for(j = 1; j <= n; ++j)
        {
            printf("(i, j) = %d, %d, avail 0 1 2 = %d %d %d\n", i, j, avail[i][j][0], avail[i][j][1], avail[i][j][2]);
        }
    }
}

int main()
{
#ifdef HOME
    freopen("D.in", "r", stdin);
    freopen("D.out", "w", stdout);
#endif
    int i, j, k;

    scanf("%d", &ntest);

    for(itest = 1; itest <= ntest; ++itest)
    {
        scanf("%d %d", &n, &m);
        for(i = 1; i <= n; ++i)
        {
            for(j = 1; j <= n; ++j)
            {
                setAll(i, j, 1);
                grid[i][j] = GRASS;
                original[i][j] = GRASS;
            }
        }
        int r, c, t, cnt;
        char s[3];

        for(i = 0; i < m; ++i)
        {
            scanf("%s %d %d", &s, &r, &c);
            t = model2num(s[0]);
            //printf("%d %d %d\n", t, r, c);
            cnt = 0;
            setKill(r, c, t, cnt);
            original[r][c] = t;
        }
        //displayAvail();
        priority_queue<Candidate> heap;
        for(i = 1; i <= n; ++i)
        {
            for(j = 1; j <= n; ++j)
            {
                //if(grid[i][j] == GRASS)
                {
                    for(k = 0; k <= 2; ++k)
                    {
                        if(avail[i][j][k])
                        {
                            cnt = 0;
                            setKill(i, j, k, cnt, true);
                            heap.push(Candidate(cnt, k, k == 2 ? 2 : 1, i, j));
                        }
                    }
                }
            }
        }
        //displayAvail();
        while(!heap.empty())
        {
            Candidate u = heap.top(); heap.pop();
            r = u.r;
            c = u.c;
            t = u.model;
            //if(grid[r][c] == GRASS && avail[r][c][t] == 1)
            if(avail[r][c][t] == 1)
            {
                grid[r][c] = t;
                setKill(r, c, t, cnt);
                //printf("set (%d, %d) to %d, grid = %d\n", r, c, t, grid[r][c]);
            }
        }
        queue<Candidate> que;
        cnt = 0;
        for(i = 1; i <= n; ++i)
        {
            for(j = 1; j <= n; ++j)
            {
                k = 0;
                if(grid[i][j] == 2) k = 2;
                else if(grid[i][j] != GRASS) k = 1;

                if(grid[i][j] != original[i][j])
                {
                    que.push(Candidate(0, grid[i][j], k, i, j));
                }
                cnt += k;
                //printf("%d %d %d ", i, j, grid[i][j]);
                //printf("%c\n", num2model(grid[i][j]));
            }
            //printf("\n");
        }
        printf("Case #%d: %d %d\n", itest, cnt, que.size());
        while(!que.empty())
        {
            Candidate u = que.front(); que.pop();
            r = u.r;
            c = u.c;
            t = u.model;
            printf("%c %d %d\n", num2model(t), r, c);
        }
    }

    return 0;
}

