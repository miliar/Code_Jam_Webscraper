#include <bits/stdc++.h>

using namespace std;

#define int int64_t
#define endl '\n'
#define fi first
#define se second
#define mp make_pair
#define pb push_back

template <typename T1, typename T2>
istream & operator >> (istream & in, pair <T1, T2> & p)
{
    in >> p.fi >> p.se;
    return in;
}

template <typename T1, typename T2>
ostream & operator << (ostream & out, pair <T1, T2> & p)
{
    out << "{" << p.fi << ", " << p.se << "}";
    return out;
}

template <typename T>
istream & operator >> (istream & in, vector <T> & arr)
{
    for (auto & i: arr)
    {
        in >> i;
    }
    return in;
}

template <typename T>
ostream & operator << (ostream & out, vector <T> & arr)
{
    for (int i = 0; i < (int)arr.size() - 1; ++i)
        out << arr[i] << " ";
    if (arr.size())
        out << arr.back();
    return out;
}

ifstream in("B-small-attempt222.in");
ofstream out("output.txt");

#define cin in
#define cout out

void solve()
{
    int n;
    cin >> n;
    int c, m;
    cin >> c >> m;
    printf("lol");
    vector <pair <int, int> > arr(m);
    cin >> arr;
    printf("kek");
    vector <vector <int> > pos(c);
    if (c != 2)
        return;
    printf("kek");
    for (int i = 0; i < m; ++i)
    {
        if (arr[i].se < 0 || arr[i].se > 3)
        {
            cout << arr[i].se;
            exit(0);
        }
        pos[arr[i].se - 1].push_back(arr[i].fi);
    }
    printf("kek");
    printf("kek");
    sort(pos[0].begin(), pos[0].end());
    sort(pos[1].begin(), pos[1].end());
    int j = 0;
    int ans = 0;
    int cnt = 0;
    bool flag = true;
    if (pos[1].size() < pos[0].size())
        swap(pos[0], pos[1]);
    printf("kek");
    for (int i = 0; i < pos[0].size(); ++i)
    {
        while (j < pos[1].size() && pos[1][j] <= pos[0][i])
        {
            ++j;
        }
        if (j >= pos[1].size())
        {
            flag = false;
            j = 0;
        }
        if (pos[0][i] == pos[1][j] && pos[0][i] == 1)
            ans += 2;
        else if (pos[0][i] == pos[1][j])
        {
            ans++;
            cnt++;
        }
        else
        {
            ans++;
        }
        pos[1].erase(pos[1].begin() + j);
    }
    cout << ans + pos[1].size() << " " << cnt << endl;
}

signed main()
{
    //ios::sync_with_stdio(false);
    //cin.tie(0);
    //cout.tie(0);

    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        printf("1");
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
    system("pause");
    return 0;
}
