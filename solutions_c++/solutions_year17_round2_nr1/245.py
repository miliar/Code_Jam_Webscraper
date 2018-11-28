#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>


#pragma warning(disable:4996)

using namespace std;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("test.out", "w", stdout);

    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        int D, N;
        scanf("%d %d", &D, &N);
        vector<pair<int, int>> horses(N);
        vector<int> S(N);

        for (int i = 0; i < N; i++) {
            scanf("%d %d", &horses[i].first, &horses[i].second);
        }
        sort(horses.begin(), horses.end());

        double endtime = (double)(D - horses.back().first) / (double)horses.back().second;
        for (int i = N - 2; i >= 0; i--) {
            double e2 = (double)(D - horses[i].first) / (double)horses[i].second;
            endtime = max(endtime, e2);
        }

        printf("Case #%d: %.8lf\n", t, (double)D / (double)endtime);

    
    }

    return 0;
}
