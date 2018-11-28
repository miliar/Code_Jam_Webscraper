#include <bits/stdc++.h>
using namespace std;

int main(void) {
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++ t) {
        long long n, k;
        cin >> n >> k;

        map<long long, long long> vis, tmp;
        vis[-n] = 1;

        long long maxAns = 0, minAns = 0;

        while (k > 0) {
            tmp.clear();
            for (auto p: vis) {
                long long len = -p.first, cnt = p.second;
                len -= 1;

                if (k <= cnt) {
                    k -= cnt;
                    minAns = len / 2;
                    maxAns = minAns + (len % 2);
                    break;
                } else {
                    if (len % 2 == 0) {
                        tmp[-len / 2] += cnt * 2;
                    } else {
                        tmp[-len / 2] += cnt;
                        tmp[-(len / 2 + 1)] += cnt;
                    }
                    k -= cnt;
                }
            }
            vis = tmp;
        }
        cout << "Case #" << t << ": " << maxAns << ' ' << minAns << endl;
    }

    return 0;
}
