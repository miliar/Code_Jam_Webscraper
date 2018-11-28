#include <iostream>
#include <vector>

using namespace std;

void dfs(vector<vector<char>>& v, int n0, int n1, int m0, int m1)
{
    int cnt = 0;
    char last = '?';
    for (int i = n0; i <= n1; ++i)
    {
        for (int j = m0; j <= m1; ++j)
        {
            if (v[i][j] != '?')
            {
                cnt ++;
                last = v[i][j];
            }
        }
    }
    if (cnt == (n1 - n0 + 1) * (m1 - m0 + 1))
    {
        return;
    }

    if (cnt == 1)
    {
        for (int i = n0; i <= n1; ++i)
        {
            for (int j = m0; j <= m1; ++j)
            {
                v[i][j] = last;
            }
        }
        return;
    }

    int new_cnt = 0;
    for (int i = n0; i <= n1; ++i)
    {
        for (int j = m0; j <= m1; ++j)
        {
            if (v[i][j] != '?')
            {
                new_cnt ++;
            }
        }
        if (new_cnt > 0 && new_cnt < cnt)
        {
            dfs(v, n0, i, m0, m1);
            dfs(v, i + 1, n1, m0, m1);
            return;
        }
    }

    new_cnt = 0;
    for (int j = m0; j <= m1; ++j)
    {
        for (int i = n0; i <= n1; ++i)
        {
            if (v[i][j] != '?')
            {
                new_cnt ++;
            }
        }
        if (new_cnt > 0 && new_cnt < cnt)
        {
            dfs(v, n0, n1, m0, j);
            dfs(v, n0, n1, j + 1, m1);
            return;
        }
    }
}

int main()
{
    int T;

    cin >> T;
    for (int ct = 0; ct < T; ++ct)
    {
        int n, m;
        vector<vector<char>> v;
        cin >> n >> m;
        for (int i = 0; i < n; ++i)
        {
            vector<char> vv;
            for (int j = 0; j < m; ++j)
            {
                char c;
                cin >> c;
                vv.push_back(c);
            }
            v.push_back(vv);
        }

        dfs(v, 0, n - 1, 0, m - 1);

        cout << "Case #" << (ct + 1) << ":" << endl;
        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < m; ++j)
            {
                cout << v[i][j];
            }
            cout << endl;
        }
    }
    return 0;
}
