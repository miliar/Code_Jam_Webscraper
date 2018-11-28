#include <iostream>
#include <vector>
#include <limits>
#include <cassert>
#include <set>
#include <queue>

using namespace std;

struct status
{
    long long hd, ad, hk, ak;
    long long turns;
};

bool operator < (const status& a, const status& b)
{
    if (a.hd != b.hd)
        return a.hd < b.hd;
    if (a.ad != b.ad)
        return a.ad < b.ad;
    if (a.hk != b.hk)
        return a.hk < b.hk;
    if (a.ak != b.ak)
        return a.ak < b.ak;
    return false;
}

void add(queue<status>& q, set<status>& s, status n)
{
    if (n.ak < 0)
    {
        n.ak = 0;
    }
    if (n.hd < 0)
    {
        n.hd = 0;
    }
    if (n.hk < 0)
    {
        n.hk = 0;
    }
    if (s.find(n) != s.end())
    {
        return;
    }
    s.insert(n);
    q.push(n);
}

int main()
{
    int T;

    cin >> T;
    for (int ct = 0; ct < T; ++ct)
    {
        long long hd, ad, hk, ak, b, d, turns = numeric_limits<long long>::max();

        cin >> hd >> ad >> hk >> ak >> b >> d;

        set<status> s;
        queue<status> q;

        status initial{hd, ad, hk, ak, 0};
        q.push(initial);
        s.insert(initial);
        while (!q.empty())
        {
            status cur = q.front();
            q.pop();
            if (cur.hk <= 0)
            {
                turns = cur.turns;
                break;
            }
            if (cur.hd <= 0)
            {
                continue;
            }
            // attack
            add(q, s, status{cur.hd - cur.ak, cur.ad, cur.hk - cur.ad, cur.ak, cur.turns + 1});
            // buff
            add(q, s, status{cur.hd - cur.ak, cur.ad + b, cur.hk, cur.ak, cur.turns + 1});
            // cure
            add(q, s, status{hd - cur.ak, cur.ad, cur.hk, cur.ak, cur.turns + 1});
            // debuff
            add(q, s, status{cur.hd - max(cur.ak - d, 0ll), cur.ad, cur.hk, cur.ak - d, cur.turns + 1});
        }

        if (turns == numeric_limits<long long>::max())
        {
            cout << "Case #" << (ct + 1) << ": IMPOSSIBLE" << endl;
        }
        else
        {
            cout << "Case #" << (ct + 1) << ": " << turns << endl;
        }
    }
    return 0;
}
