#include <bits/stdc++.h>

#define forn(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;
typedef long long ll;

int main()
{
    int T;
    cin >> T;
    cout.precision(8);
    for (int casenum = 1; casenum <= T; ++casenum) {
        priority_queue<ll> q;
        ll N, K;
        cin >> N >> K;
        q.push(N);
        ll l, r;
        map<ll, ll> counts;
        counts[N] = 1;

        while (K > 0) {
            ll s = q.top(); q.pop();
            l = (s-1)/2;
            r = s/2;
            ll count = counts[s];
            if (l > 0) {
                if (counts.count(l) == 0) q.push(l);
                counts[l] += count;
            }
            if (r > 0) {
                if (counts.count(r) == 0) q.push(r);
                counts[r] += count;
            }
            //cout << i << ": " << l << ',' << r << endl;
            K -= count;
        }

        cout << "Case #" << casenum << ": " << r << ' ' << l << endl;
    }
    return 0;
}

