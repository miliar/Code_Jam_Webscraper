#include <bits/stdc++.h>

using namespace std;

const int MAXN = 100 + 10;
const int INF = (int)(1e9);

void run() {
    long long n, k;
    cin >> n >> k;

    map<long long, long long> mm_1, mm_2;
    mm_1[-n] += 1;
    while (k > 0) {
        mm_2.clear();
        for(auto it = mm_1.begin(); it != mm_1.end(); ++it) {
            long long v = -(it->first), cnt = it->second;
            long long l = (v - 1) / 2, r = v - l - 1;
            k -= cnt;
            if (k <= 0) {
                cout << max(l, r) << " " << min(l, r) << endl;
                return;
            }
            if (l > 0) mm_2[-l] = mm_2[-l] + cnt;
            if (r > 0) mm_2[-r] = mm_2[-r] + cnt;
        }
        mm_1 = mm_2;
    }
}

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C.out", "w", stdout);

    int ntests = 1;
    cin >> ntests;
    for(int tc = 1; tc <= ntests; ++tc) {
        cout << "Case #" << tc << ": ";
        run();
    }
}
