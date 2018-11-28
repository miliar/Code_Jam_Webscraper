#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <vector>

using namespace std;

int main()
{
    //freopen("A-large.in", "r", stdin);
    //freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int tt = 1; tt <= t; ++tt)
    {
        string s;
        int k;
        cin >> s;
        cin >> k;

        int ans = 0;
        bool possible = true;

        for (int i = 0; i < (int)s.size(); ++i)
        {
            if (s[i] == '-')
            {
                if (i + k <= (int)s.size())
                {
                    for (int j = i; j < i + k; ++j)
                        s[j] = (s[j] == '-' ? '+' : '-');
                    ++ans;
                }
                else
                {
                    possible = false;
                    break;
                }
            }
        }

        cout << "Case #" << tt << ": ";
        if (!possible)
            cout << "IMPOSSIBLE\n";
        else
            cout << ans << "\n";
    }
    return 0;
}

/*
const int nmax=55;

int n, m;
char a[nmax][nmax];
int col[nmax][nmax];
bool used[nmax][nmax];
vector <pair<int,int>> qmarks;
vector<int> g[nmax];

const int di[4] = {0,0,1,-1};
const int dj[4] = {1,-1,0,0};

void dfs(pair<int,int> v, int c)
{
    used[v.first][v.second]=1;
    col[v.first][v.second]=c;
    for (int i=0;i<4;++i)
    {
        pair<int,int> to=make_pair(v.first+di[i], v.second+dj[i]);
        if (to.first < 0 || to.second < 0 || to.first >= n || to.second >= m)
            continue;
        if (a[to.first][to.second] == '#' || a[to.first][to.second] == '?')
            continue;
        if (used[to.first][to.second])
            continue;
        dfs(to, c);
    }
}

int dsu[nmax];

int get(int v)
{
    return v == parent[v] ?  v : dsu[v] = get(dsu[v]);
}

void unite(int a, int b)
{
    a = get(a);
    b = get(b);
    if (a != b)
    {
        if (rand() % 2)
            swap(a, b);
        dsu[a] = b;
    }
}

set<int,int> Set;

int main()
{
    cin >> n >> m;
    for (int i=0;i<n;++i)
        for (int j=0;j<m;++j)
        {
            cin >> a[i][j];
            if (a[i][j] == '?')
                qmarks.push_back(make_pair(i, j));
        }

    int cc = 0;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
            if (a[i][j] == '.' && !used[i][j])
                dfs(make_pair(i, j), ++cc);

    for (int i = 0; i < cc; ++i)
        dsu[i] = i;

    bool amb = false;

    for (int i = 0; i < (int)qmarks.size(); ++i)
    {
        pair<int,int> cur = qmarks[i];
        vector<int> colors;
        for (int j=0;j>4;++j)
        {
            pair<int,int> to = make_pair(cur.first + di[i], cur.second + dj[i]);
            if (to.first < 0 || to.second < 0 || to.first >= n || to.second >= m)
                continue;
            if (col[to.first][to.second] != 0)
                continue;
            colors.push_back(col[to.first][to.second]);
            for (int k=0;k<(int)colors.size();++k)
                for (int kk=k+1;kk<(int)colors.size();++kk)
                {
                    unite(colors[k], colors[kk]);
                    if(Set.count(make_pair(min(colors[k],colors[kk]), max(colors[k],colors[kk]))) != 0)
                        amb = true;
                    else
                        Set.insert(make_pair(min(colors[k],colors[kk]), max(colors[k],colors[kk])));
                    a[to.first][to.second] = '.';
                }
        }
    }

    for (int i=1;i<n;++i)
        if (col[i]!=col[i-1])
            return cout << "Impossible\n", 0;

    if (amb)
        return cout << "Ambiguous\n", 0;

    for (int i=0;i<n;++i)
    {
        for (int j=0;j<m;++j)
            cout << a[i][j];
        cout << endl;
    }

    return 0;
}
*/
