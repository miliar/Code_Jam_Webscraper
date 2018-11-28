#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

vector<int> MaximumMatching(const vector<vector<int> > &N, int n)
{
    vector<int> m(N.size(), -1);

    for (int i = 0; i < n; i++)
        if (!~m[i])
        {
            vector<int> p(N.size(), -1);
            vector<int> q(1, i);

            for (int qs = 0; qs < q.size(); qs++)
            {
                int v = q[qs];

                for (int j = 0; j < N[v].size(); j++)
                    if (!~p[N[v][j]])
                    {
                        int u = N[v][j];
                        p[u] = v;
                        if (~m[u])
                            q.push_back(m[u]);
                    }
            }

            for (int j = n; j < N.size(); j++)
                if (!~m[j] && ~p[j])
                {
                    for (int u = j; ~u; )
                    {
                        int v = p[u];
                        int w = m[v];
                        m[v] = u;
                        m[u] = v;
                        u = w;
                    }

                    break;
                }
        }

    return m;
}

int main()
{
    int t;
    cin >> t;

    for (int tt = 1; tt <= t; tt++)
    {
        int n;
        cin >> n;
        vector<string> a(n, string(n, '.'));

        int k;
        cin >> k;
        for (int i = 0; i < k; i++)
        {
            string s;
            int u, v;
            cin >> s >> u >> v;
            a[u - 1][v - 1] = s[0];
        }

        k = 0;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
            {
                k += a[i][j] != '.';
                k += a[i][j] == 'o';
            }

        vector<vector<int> > N(4 * n);
        for (int i = 0; i < 2 * n - 1; i++)
        {
            bool ok = true;
            for (int t = max(0, i - n + 1); t < n && t <= i; t++)
                ok &= a[i - t][t] == '.' || a[i - t][t] == 'x';

            if (!ok)
                continue;

            for (int j = 0; j < 2 * n - 1; j++)
            {
                int t = i + j - n + 1;
                if (t % 2 == 1 || t < 0 || t >= 2 * n || t > 2 * i || 2 * i - t >= 2 * n)
                    continue;

                t /= 2;
                ok = a[i - t][t] == '.' || a[i - t][t] == 'x';

                for (int t = max(0, j - n + 1); t < n && t <= j; t++)
                    ok &= a[n - 1 - j + t][t] == '.' || a[n - 1 - j + t][t]== 'x';

                if (!ok)
                    continue;

                N[i].push_back(2 * n + j);
                N[2 * n + j].push_back(i);
            }
        }
/*
        for (int i = 0; i < N.size(); i++)
        {
            for (int j = 0; j < N[i].size(); j++)
                cout << N[i][j] << " ";
            cout << endl;
        }
*/
        vector<int> matching = MaximumMatching(N, 2 * n);
        vector<pair<int, int> > m;
        for (int i = 0; i < 2 * n; i++)
            if (~matching[i])
            {
                int j = matching[i] - 2 * n;
                int t = (i + j - n + 1) / 2;
                a[i - t][t] = a[i - t][t] == '.' ? '+' : 'o';
                m.push_back(make_pair(i - t, t));
                k++;
            }

        for (int i = 0, j = 0; i < n && j < n; )
        {
            bool ok = true;
            for (int t = 0; t < n; t++)
                ok &= a[i][t] == '.' || a[i][t] == '+';

            if (!ok)
            {
                i++;
                continue;
            }

            for (int t = 0; t < n; t++)
                ok &= a[t][j] == '.' || a[t][j] == '+';

            if (!ok)
            {
                j++;
                continue;
            }

            m.push_back(make_pair(i, j));
            a[i][j] = a[i][j] == '.' ? 'x' : 'o';
            k++;
        }

        sort(m.begin(), m.end());
        m.resize(unique(m.begin(), m.end()) - m.begin());

        cout << "Case #" << tt << ": " << k << " " << m.size() << endl;
        for (int i = 0; i < m.size(); i++)
            cout << a[m[i].first][m[i].second] << " " << m[i].first + 1 << " " << m[i].second + 1 << endl;
    }

    return 0;
}
