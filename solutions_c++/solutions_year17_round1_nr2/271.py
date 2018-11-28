#include<iostream>
#include<vector>
#include<sstream>
#include<set>
#include<map>
#include<algorithm>

using namespace std;

int n, p;
vector<int> r;
vector<vector<int> > q;

int min_quan(int a, int b)
{
    a *= 11;
    b *= 10;
    return (b + a - 1)/ a;
}

int max_quan(int a, int b)
{
    a *= 9;
    b *= 10;
    return b / a;
}

int solve1()
{
    int ans = 0;
    for (int i = 0; i < p; ++i)
    {
        int m1 = min_quan(r[0], q[0][i]);
        int m2 = max_quan(r[0], q[0][i]);
        if (m1 <= m2)
            ++ans;
    }
    return ans;
}

int solve2()
{
    int ans = 0;
    vector<int> perm(p);
    for (int i = 0; i < p; ++i)
        perm[i] = i;
    do
    {
        int curr_ans = 0;
        for (int i = 0; i < p; ++i)
        {
            int m1 = max(min_quan(r[0], q[0][i]), min_quan(r[1], q[1][perm[i]]));
            int m2 = min(max_quan(r[0], q[0][i]), max_quan(r[1], q[1][perm[i]]));
            if (m1 <= m2)
                ++curr_ans;
        }
        ans = max(ans, curr_ans);
    }
    while (next_permutation(perm.begin(), perm.end()));
    return ans;
}

int solven()
{
    int ans = 0;
    for (int i = 0; i < n; ++i)
    {
        sort(q[i].begin(), q[i].end());
    }
    vector<int> point(n);
    while (true)
    {
        int m1 = 0;
        int m2 = 1000000000;
        for (int i = 0; i < n; ++i)
        {
            m1 = max(m1, min_quan(r[i], q[i][point[i]]));
            m2 = min(m2, max_quan(r[i], q[i][point[i]]));
        }
        if (m1 <= m2 && m2 > 0)
        {
            ++ans;
            for (int j = 0; j < n; ++j)
            {
                ++point[j];
                if (point[j] >= p)
                    return ans;
            }
        }
        else
        {
            double m = 1e9;
            double pos = -1;
            for (int j = 0; j < n; ++j)
            {
                if ((double)q[j][point[j]] / r[j] < m)
                {
                    m = (double)q[j][point[j]] / r[j];
                    pos = j;
                }
            }
            ++point[pos];
            if (point[pos] >= p)
                return ans;
        }
    }
}

int solve()
{
    cin >> n >> p;
    r.resize(n);
    for (int i = 0; i < n; ++i)
        cin >> r[i];
    q.resize(0);
    q.resize(n, vector<int>(p));
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < p; ++j)
            cin >> q[i][j];
    return solven();
}

int main()
{
    int T, t;
    cin >> T;
    for (t = 1; t <= T; ++t)
    {
        cout << "Case #" << t << ": " << solve() << endl;
    }
    return 0;
}

