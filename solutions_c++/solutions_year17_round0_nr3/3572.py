#include <bits/stdc++.h>

using namespace std;

int main() {
//    freopen("C-small-2-attempt0.in", "r", stdin);
//    freopen("C-small-2-attempt0.out", "w", stdout);
    int t, n, k;
    scanf("%d", &t);
    for (int tc = 1; tc <= t; tc++) {
        priority_queue<int> pq;
        scanf("%d%d", &n, &k);
        pq.push(n);
        int ansMax = 0, ansMin = 0;
        while (k--) {
            int space = pq.top();
            pq.pop();
            int div = space / 2;
            if (div != 0) {
                if (space & 1) {
                    pq.push(div);
                    ansMin = div;
                } else {
                    if (div - 1 != 0) {
                        pq.push(div - 1);
                    }
                    ansMin = div - 1;
                }
                pq.push(div);
                ansMax = div;
            } else {
                ansMax = ansMin = 0;
            }
        }
        cout << "Case #" << tc << ": " << ansMax << " " << ansMin << endl;
    }
    return 0;
}
