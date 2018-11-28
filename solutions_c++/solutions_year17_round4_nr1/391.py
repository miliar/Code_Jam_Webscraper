#include <bits/stdc++.h>
using namespace std;
#pragma GCC diagnostic ignored "-Wmissing-declarations"

#define FINAL_OUT(x) {cout << (x) << '\n'; exit(0);}

#define SHOW(x) std::cout << #x << " = " << x << std::endl;

inline int safe_mul(int x, int y) __attribute__ ((warn_unused_result));

int const maxn = 101;
int dp4[maxn][maxn][maxn];
int dp3[maxn][maxn];
int dp2[maxn];


inline void maxs(int& x, int y)
{
    x = max(x, y);
}


void solve(int numtest)
{
    int n,p;
    cin >> n >> p;
    vector<int> mask(p, 0);

    for(int i = 0; i < n; ++i)
    {
        int cur;
        cin >> cur;
        ++mask[cur % p];
    }

    int ans = 0;

    if (p == 2)
        for(int i = 0; i <= mask[1]; ++i)
            maxs(ans, dp2[i]);

    if (p == 3)
        for(int x = 0; x <= mask[1]; ++x)
        for(int y = 0; y <= mask[2]; ++y)
            maxs(ans, dp3[x][y]);

    if (p == 4)
        for(int x = 0; x <= mask[1]; ++x)
        for(int y = 0; y <= mask[2]; ++y)
        for(int z = 0; z <= mask[3]; ++z)
            maxs(ans, dp4[x][y][z]);

    cout << "Case #" << numtest << ": " << ans + mask[0] << endl;
}

void precalc()
{
    dp2[1] = 1;
    for(int i = 0; i < 500; ++i)
    {
        for(int x = 0; x < maxn; ++x)
            if (x + 2 < maxn)
                maxs(dp2[x + 2], dp2[x] + 1);
    }

    dp3[1][0] = dp3[0][1] = 1;

    for(int i = 0; i < 500; ++i)
    {
        for(int nx = 0; nx <= 4; ++nx)
        for(int ny = 0; ny <= 4; ++ny)
            if((nx + ny > 0) &&  (nx + 2 * ny) % 3 == 0)
        for(int x = 0; x < maxn; ++x)
        for(int y = 0; y < maxn; ++y)
        {
            if (x + nx < maxn && y + ny < maxn)
                maxs(dp3[x + nx][y + ny], dp3[x][y] + 1);
        }
    }

    dp4[1][0][0] = dp4[0][1][0] = dp4[0][0][1] = 1;
    for(int i = 0; i < 150; ++i)
    {
        if (i % 10 == 0)
            cerr << "step " << i << endl;
        for(int nx = 0; nx <= 4; ++nx)
        for(int ny = 0; ny <= 4; ++ny)
        for(int nz = 0; nz <= 4; ++nz)
        if ( (nx + ny + nz > 0) &&  (nx + 2 * ny + 3 * nz) % 4 == 0)
        for(int x = 0; x < maxn; ++x)
        for(int y = 0; y < maxn; ++y)
        for(int z = 0; z < maxn; ++z)
        {
            if (x + nx < maxn && y + ny < maxn && z + nz < maxn)
                maxs(dp4[x + nx][y + ny][z + nz], dp4[x][y][z] + 1);
        }
    }
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    //freopen("out.txt", "w", stdout);
    ios_base::sync_with_stdio(false);

    precalc();

    int T;
    cin >> T;
    for(int i = 1; i <= T; ++i)
        solve(i);
}
