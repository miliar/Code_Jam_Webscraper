#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

int main() {
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("B-small-attempt1.out", "w", stdout);
//    freopen("A-large.in", "r", stdin);
//    freopen("A-large.out", "w", stdout);

    int T;
    int N, R, O, Y, G, B, V;

    scanf("%d", &T);

    for (int t = 1; t <= T; t++) {
        scanf("%d %d %d %d %d %d %d", &N, &R, &O, &Y, &G, &B, &V);
        vector<pair<int, char>> arr = {{R, 'R'}, {Y, 'Y'}, {B, 'B'}};
        sort(arr.begin(), arr.end());
        int d = arr[0].first + arr[1].first - arr[2].first;
        printf("Case #%d: ", t);
        if (d >= 0) {
            string res;
            for (int i = 0; i < d; i++) {
                res += arr[0].second;
                res += arr[1].second;
                res += arr[2].second;
            }
            d = arr[1].first - d;
            for (int i = 0; i < d; i++) {
                res += arr[1].second;
                res += arr[2].second;
            }
            d = arr[2].first - arr[1].first;
            for (int i = 0; i < d; i++) {
                res += arr[0].second;
                res += arr[2].second;
            }
            cout << res << endl;
        }
        else {
            cout << "IMPOSSIBLE" << endl;
        }
    }

    return 0;
}

