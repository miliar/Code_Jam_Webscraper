#include <bits/stdc++.h>

using namespace std;

int get_low(int amt, int req) {
    int low = 1.0 * amt / req / 1.1;
    if (1.0 * amt / (low * req) > 1.1)
        low++;
    return low;
}

int get_high(int amt, int req) {
    int high = 1.0 * amt / req / 0.9;
    if (1.0 * amt / (high * req) < 0.9)
        high--;
    return high;
}

int main() {
    int T;
    scanf("%d", &T);
    
    for (int tc = 1; tc <= T; tc++) {
        int N, P;
        scanf("%d %d", &N, &P);
        vector<vector<int>> packs(N, vector<int>(P));
        vector<int> ingred(N);
        for (int i = 0; i < N; i++)
            scanf("%d", &ingred[i]);

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < P; j++) 
                scanf("%d", &packs[i][j]);
            sort(packs[i].rbegin(), packs[i].rend());
        }

        int kit = 0;

        bool done = false;
        while (!done) {
            for (int i = 0; i < N; i++)
                if (packs[i].empty()) {
                    done = true;
                    break;
                }
            if (done)
                break;

            int low = get_low(packs[0].back(), ingred[0]);
            int high = get_high(packs[0].back(), ingred[0]);

            for (int k = low; k <= high; k++) {
                int cnt = 1;
                for (int i = 1; i < N; i++) {
                    while (!packs[i].empty() && get_high(packs[i].back(), ingred[i]) < k)
                        packs[i].pop_back();

                    if (!packs[i].empty()) {
                        int lo = get_low(packs[i].back(), ingred[i]);
                        int hi = get_high(packs[i].back(), ingred[i]);

                        if (lo <= k && hi >= k)
                            cnt++;
                    }
                }
                if (cnt == N) {
                    for (int i = 1; i < N; i++)
                        packs[i].pop_back();
                    kit++;
                    break;
                }
            }
            packs[0].pop_back();
        }
        printf("Case #%d: %d\n", tc, kit);
    }

    return 0;
}
