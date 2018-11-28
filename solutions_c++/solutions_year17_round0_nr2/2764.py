/**
 * http://code.google.com/codejam/contest/3264486/dashboard#s=p1
 */

#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll solve(ll N)
{
    stack<ll> s;
    while (N)
    {
        s.push(N % 10);
        N /= 10;
    }

    ll res = 0;
    bool add_nine = false;
    while (!s.empty())
    {
        auto d = s.top();

        if (add_nine) d = 9; // add nine

        if (res % 10 <= d)
        {
            res = res * 10 + d; // add current digit
            s.pop();
        }
        else
        {
            while (res % 10 > d)
            {
                d = res % 10;
                res /= 10;

                assert(d != 0);

                --d;
                s.push(d);
            }

            s.pop();
            res = res * 10 + d; // add adjusted digit

            add_nine = true;
        }
    }

    return res;
}

int main()
{
    int T;
    cin >> T;

    for (int t = 1; t <= T; ++t)
    {
        ll N;
        cin >> N;

        cout << "Case #" << t << ": " << solve(N) << '\n';
    }

    return 0;
}
