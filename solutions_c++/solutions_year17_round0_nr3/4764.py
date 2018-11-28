#include <bits/stdc++.h>

#define F first
#define S second
#define pb push_back
#define INF (1 << 30)
#define SQR(a) ((a) * (a))

using namespace std;

const int N = 1111;

map<pair<int64_t, int64_t>, int64_t> m;

void solve() {
    m.clear();
    int64_t n, k;
    cin >> n >> k;
    m[{(n - 1) / 2, n / 2}] = 1;
    pair<int64_t, int64_t> lp;
    while (k > 0) {
        auto it = m.end();
        advance(it, -1);
        lp = it->first;
        int64_t count = it->second;
        m.erase(it);
        //cerr << k << " map {" << lp.first << ", " << lp.second << "} = " << count << endl;
        k -= count; 
        if (k <= 0)
            break;
        m[{(lp.first - 1) / 2, lp.first / 2}] += count;
        m[{(lp.second - 1) / 2, lp.second / 2}] += count;
    }
    cout << lp.second << " " << lp.first << endl;
}

int main()
{
    //freopen("input.txt", "r", stdin);
    
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        cout << "Case #" << i << ": ";
        solve();
    }

    return 0;
}
