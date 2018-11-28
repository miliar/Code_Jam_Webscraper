#include <bits/stdc++.h>

using namespace std;

#define int int64_t
#define mp make_pair
#define fi first
#define se second

ifstream in("B-small-attempt3.in");
ofstream out("B_small_ans.txt");

#define cin in
#define cout out

string solve()
{
    int n, r, o, y, g, bbb, v;
    cin >> n >> r >> o >> y >> g >> bbb >> v;
    if (r > n / 2 || y > n / 2 || bbb > n / 2)
    {
        return "IMPOSSIBLE";
    }
    set <pair <int, char> > s;
    if (r > 0)
        s.insert(mp(r, 'R'));
    if (y > 0)
        s.insert(mp(y, 'Y'));
    if (bbb > 0)
        s.insert(mp(bbb, 'B'));
    string ans = "";
    while (s.size() > 0)
    {
        if (s.size() == 1)
        {
            assert(s.begin()->fi == 1);
            ans.push_back(s.begin()->se);
            if (s.begin()->se == ans[0])
                swap(ans[ans.size() - 1], ans[ans.size() - 2]);
            break;
        }
        if (s.size() == 2)
        {
            int a = s.begin()->fi, b = (++s.begin())->fi;
            char aa = s.begin()->se, bb = (++s.begin())->se;
            assert(b == a);
            for (int i = 0; i < a; ++i)
            {
                if (bb != ans.back() && aa != ans[0])
                {
                    ans.push_back(bb);
                    ans.push_back(aa);
                }
                else
                {
                    ans.push_back(aa);
                    ans.push_back(bb);
                }
            }
            break;
        }
        int a = s.begin()->fi, b = (++s.begin())->fi, c = (++++s.begin())->fi;
        char aa = s.begin()->se, bb = (++s.begin())->se, cc = (++++s.begin())->se;
        for (int i = 0; i < max(b - a, 1ll); ++i)
        {
            b--;
            c--;
            if (cc != ans.back())
            {
                ans.push_back(cc);
                ans.push_back(bb);
            }
            else
            {
                ans.push_back(bb);
                ans.push_back(cc);
            }
        }
        s.erase(--s.end());
        s.erase(--s.end());
        if (b > 0)
        {
            s.insert(mp(b, bb));
        }
        if (c > 0)
        {
            s.insert(mp(c, cc));
        }
    }
    //cout << ans << endl;
    for (int i = 0; i < ans.size(); ++i)
    {
        assert(ans[i] != ans[(i + 1) % n]);
    }
    assert(ans.size() == n);
    return ans;
}

signed main()
{
    int t;
    cin >> t;
    cout.precision(12);
    for (int itt = 0; itt < t; ++itt)
    {
        cout << "Case #" << itt + 1 << ": " << solve() << endl;
    }
    return 0;
}

