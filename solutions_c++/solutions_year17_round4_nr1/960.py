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

ifstream in("A-large222.in");
ofstream out("output.txt");

#define cin in
#define cout out

void solve()
{
    int n, p;
    cin >> n >> p;
    vector <int> arr(n);
    cin >> arr;
    vector <int> cnt(p, 0);
    for (int i = 0; i < n; ++i)
    {
        cnt[arr[i] % p]++;
    }
    int ans = cnt[0];
    if (p == 2)
    {
        ans += cnt[1] / 2;
        if (cnt[1] % 2 == 1)
            ans += 1;
    }
    else if (p == 3)
    {
        ans += min(cnt[1], cnt[2]);
        ans += abs(cnt[2] - cnt[1]) / 3;
        if (abs(cnt[2] - cnt[1]) % 3 != 0)
            ans++;
    }
    else
    {
        map <vector <int>, int> mapa;
        mapa[vector <int> (4, 0)] = 0;
        for (int p0 = 0; p0 <= cnt[0]; ++p0)
        {
            for (int p1 = 0; p1 <= cnt[1]; ++p1)
            {
                for (int p2 = 0; p2 <= cnt[2]; ++p2)
                {
                    for (int p3 = 0; p3 <= cnt[3]; ++p3)
                    {
                        int sum = p1 * 1 + p2 * 2 + p3 * 3;
                        int now = 0;
                        if (p0 > 0)
                        {
                            now = max(now, mapa[{p0 - 1, p1, p2, p3}] + (sum % 4 == 0));
                        }
                        if (p1 > 0)
                        {
                            now = max(now, mapa[{p0, p1 - 1, p2, p3}] + ((sum - 1) % 4 == 0));
                        }
                        if (p2 > 0)
                        {
                            now = max(now, mapa[{p0, p1, p2 - 1, p3}] + ((sum - 2) % 4 == 0));
                        }
                        if (p3 > 0)
                        {
                            now = max(now, mapa[{p0, p1, p2, p3 - 1}] + ((sum - 3) % 4 == 0));
                        }
                        mapa[{p0, p1, p2, p3}] = now;
                    }
                }
            }
        }
        ans = mapa[cnt];
        /*cout << mapa[{2, 0, 0, 0}] << endl;
        cout << mapa[{2, 1, 0, 0}] << endl;
        cout << mapa[{2, 1, 1, 0}] << endl;*/
    }
    cout << ans << endl;
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
    return 0;
}
