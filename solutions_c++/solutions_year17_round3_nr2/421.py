#include<iostream>
#include<queue>
#include<vector>
#include<cstdio>
#include <set>
#include <algorithm>
#include <cmath>
#include <iomanip>
using namespace std;

void init(vector<int>& ca, int cnt)
{
    for (int i = 0; i < cnt; ++i)
    {
        int c, d;
        cin >> c >> d;
        for (int j = c; j < d; j++)
        {
            ca[j] = 1;
        }
    }
}

int f[1500][740][2];

int inf = 1500;
void init_f()
{
    for (int i = 0; i < 1500; ++i)
        for (int j = 0; j < 730; ++j)
        {
            f[i][j][0] = f[i][j][1] = inf;
        }
}

double solution()
{
    int ca, ja;
    cin >> ca >> ja;
    vector<int> ca_, ja_;
    ca_.resize(24*60);
    ja_ = ca_;
    init(ca_, ca);
    init(ja_, ja);
    init_f();
    if (ca_[0] == 0)
    {
        f[0][1][0] = 0;
    }
    if (ja_[0] == 0)
    {
        f[0][0][1] = 0;
    }
    for (int i = 0; i < 24 * 60; ++i)
    {
        for (int j = 0; j <= 720; ++j)
        {
            if (f[i][j][0] != inf)
            {
                if (ca_[i + 1] == 0)
                {
                    f[i + 1][j + 1][0] = min(f[i + 1][j + 1][0], f[i][j][0]);
                }
                if (ja_[i + 1] == 0)
                {
                    f[i + 1][j][1] = min(f[i + 1][j][1], f[i][j][0] + 1);
                }
            }
            if (f[i][j][1] != inf)
            {
                if (ca_[i + 1] == 0)
                {
                    f[i + 1][j + 1][0] = min(f[i + 1][j + 1][0], f[i][j][1] + 1);
                }
                if (ja_[i + 1] == 0)
                {
                    f[i + 1][j][1] = min(f[i + 1][j][1], f[i][j][1]);
                }
            }
        }
    }

    int res = min(f[1440-1][720][0], f[1440-1][720][1]);
    if (res % 2 == 1)
    {
        res += 1;
    }
    return res;
}

int main()
{
    freopen("input.txtb2", "r", stdin);
    freopen("output.txtb2", "w", stdout);
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i)
    {
        cout << "Case #" << i << ": " << solution() << endl;
    }
    return 0;
}
