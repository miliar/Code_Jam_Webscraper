#include <bits/stdc++.h>

using namespace std;

const int MaxN = 102;

char a[102][102];

vector <pair<int, int> > pos;

void paint(int x, int y, int xx, int yy, char c)
{
    for(int i = x; i <= xx; ++i)
        for(int j = y; j <= yy; ++j)
            a[i][j] = c;
}

void solve(int CASE)
{
    pos.clear();
    cout << "CASE #" << CASE << ":\n";
    int n, m;
    cin >> n >> m;
    for(int i = 1; i <= n; ++i)
        for(int j = 1; j <= m; ++j)
        {
            cin >> a[i][j];
            if(a[i][j] != '?')
                pos.push_back(make_pair(i, j));
        }
    int l = 0;
    while(l < pos.size())
    {
        int r = l;
        while(r < pos.size() && pos[l].first == pos[r].first)
            ++r;
        int h1, h2, w1, w2;



        if(l + 1 != -1)
        {
            if(l == 0)
                h1 = 1;
            else
                h1 = pos[l - 1].first + 1;
            if(r == pos.size())
                h2 = n;
            else
                h2 = pos[r].first - 1;
//            cout << l << ' ' << r << ' ' << h1 << ' ' << h2 << '\n';
            for(int j = l; j < r; ++j)
            {
                if(j == l)
                    w1 = 1;
                else
                    w1 = pos[j - 1].second + 1;
                if(j + 1 == r)
                    w2 = m;
                else
                    w2 = pos[j + 1].second - 1;
                paint(h1, w1, h2, w2, a[pos[j].first][pos[j].second]);
            }
        }
        l = r;
    }
    for(int i = 1; i <= n; ++i)
    {
        for(int j = 1; j <= m; ++j)
            cout << a[i][j];
        cout << '\n';
    }
}

int main()
{
    freopen("ALARGE.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    for(int t1 = 1; t1 <= t; ++t1)
        solve(t1);
    return 0;
}
