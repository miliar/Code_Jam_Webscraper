#include <bits/stdc++.h>
#define pi M_PI
using namespace std;


const int M = 1010;

int N, K;
long long radius[M], height[M];

double getSurfaceArea(int prev, int cur) {
    if (prev == -1) {
        return (2*pi*radius[cur]*height[cur] + pi*radius[cur]*radius[cur]);
    }
    return (pi*(radius[prev]*radius[prev] - radius[cur]*radius[cur]) + 2*pi*radius[cur]*height[cur] + pi*radius[cur]*radius[cur]);
}

double solve(int i, int j, int prev) {
    if (j == 0)
        return 0;
    if (i == N)
        return -1;
    double x = solve(i + 1,  j - 1, i) + getSurfaceArea(prev, i) - (prev != -1 ? pi*radius[prev]*radius[prev] : 0);
    double y = solve(i + 1, j, prev);
    return max(x, y);
}

int main() {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    freopen("a.err", "w", stderr);

    int T;
    cin >> T;
    for(int tnum = 1; tnum <= T; ++tnum) {
        cin >> N >> K;
        vector<pair<int, int> > v(N);
        for (int i = 0; i < N; i++)
            cin >> v[i].first >> v[i].second;
        sort(v.rbegin(), v.rend());
        for (int i = 0; i < N; i++) {
            radius[i] = v[i].first;
            height[i] = v[i].second;
        }
        cout << "Case #" << tnum << ": ";
        printf("%.9lf\n", solve(0, K, -1));
    }
    return 0;
}
