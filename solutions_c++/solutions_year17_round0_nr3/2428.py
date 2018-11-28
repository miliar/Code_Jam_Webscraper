#include <iostream>
#include <bits/stdc++.h>

using namespace std;

using ll = long long;

int main(int argc, char *argv[])
{
    freopen("c1.in", "r", stdin);
    freopen("c.out", "w", stdout);
    cin.sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin >> t;
    for (int qq = 1; qq <= t; qq++)
    {
        cout << "Case #" << qq << ": ";
        ll n, k;
        cin >> n >> k;
        map<ll, ll> m[2];
        m[0][n] = 1;
        int i = 0;
        //ll prev = 0;
        ll next = 0;
        ll resLen = -1;
        while (resLen == -1)
        {
            //prev = next;
            for (auto it = m[i & 1].rbegin(); it != m[i & 1].rend(); it++)
            {
                map<ll, ll> &nextm = m[(i + 1) & 1];
                ll len = it->first;
                ll num = it->second;
                assert(num > 0);
                assert(len > 0);
                next += num;
                if (k <= next)
                {
                    resLen = len;
                    break;
                }
                if (len == 1)
                {
                    continue;
                }
                if (len == 2)
                {
                    nextm[1] += num;
                    continue;
                }
                nextm[len / 2] += num;
                nextm[len - len / 2 - 1] += num;
            }
            m[i & 1].clear();
            i++;
        }
        cout << (resLen / 2) << ' ' << (resLen - resLen / 2 - 1) << '\n';
    }
    return 0;
}
