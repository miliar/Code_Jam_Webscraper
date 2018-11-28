#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int, int>;

int N, K;
pii cake[1100];

double memo[1010][1010];
int seen[1010][1010];
double dp(int idx, int k, int id) {
    if (seen[idx][k] == id)  return memo[idx][k];
    double ans = 0;
    double h = cake[idx].second;
    double r = cake[idx].first;
    ans += (2*h*M_PI*r);

    double best = 0;
    if (k > 1) {
        best = -1e40;
        for (int i = idx+1; i < N; i++) {
            best = std::max(best, dp(i, k-1, id));
        }
    }
    ans += best;

    seen[idx][k] = id;
    memo[idx][k] = ans;
    return ans;
}

int main() {
    int T;
    scanf("%i", &T);
    for (int t = 0; t < T; t++) {
        scanf("%i %i", &N, &K);
        for (int i = 0; i < N; i++) {
            int x, y;
            scanf("%i %i", &x, &y);
            cake[i].first = x;
            cake[i].second = y;
        }
        std::sort(cake, cake+N, std::greater<pii>());

        double best = -1e40;

        for (int i = 0; i < N; i++) {
            double r = cake[i].first;
            double ans = r * r * M_PI;
            best = std::max(best, ans + dp(i, K, t+1));
        }
        printf("Case #%i: %.9lf\n", t+1, best);
    }
}
