#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <map>

#define PROBLEM "C-large"

using namespace std;

void solve(long long n, long long k) {
    map<long long, long long> m;
    m[n] = 1;
    long long v, c;
    while (k > 0) {
        auto it = m.end();
        --it;
        v = it->first;
        c = it->second;
        if (k <= c) {
            cout << v/2 << " " << (v-1)/2;
            return;
        } else {
            m.erase(it);
            k -= c;
            m[v/2] += c;
            m[(v-1)/2] += c;
        }
    }
}

int main()
{
    freopen(PROBLEM ".in", "rt", stdin);
    freopen(PROBLEM ".out", "wt", stdout);

    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        long long n, k;
        cin >> n >> k;
         cout << "Case #" << t << ": ";
         solve(n, k);
         cout << endl;
    }
    return 0;
}
