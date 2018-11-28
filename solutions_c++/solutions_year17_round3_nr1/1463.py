#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

double DP[1055][1055];

void solve(int Case) {
    memset(DP, 0, sizeof DP);
    int N, K;
    double r, h;
    cin >> N >> K;
    vector<pair<double, double> > P;
    for (int i=0;i<N;i++) {
        cin >> r >> h;
        P.push_back(make_pair(r, h));
    }
    sort(P.begin(), P.end(), greater<pair<double, double> >());
    for (int j=1;j<=K;j++) {
        for (int i=1;i<=N;i++) {
            DP[j][i] = max(
                DP[j-1][i-1] + 2 * M_PI * P[i-1].first * P[i-1].second +
                    (j == 1 ? P[i-1].first * P[i-1].first * M_PI : 0),
                max(DP[j-1][i-1], DP[j][i-1]));

            // printf("%lf ", 2 * M_PI * P[i-1].first * P[i-1].second + (j == 1 ? P[i-1].first * P[i-1].first * M_PI : 0));
        }
        // printf("\n");
    }
    printf("Case #%d: %lf\n", Case, DP[K][N]);
}

int main () {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    cin >> T;
    for (int i=0;i<T;i++) solve(i+1);
}