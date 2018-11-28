#include <cstdio>
#include <algorithm>
#include <utility>
using namespace std;

pair<long long, long long> a[1000];
int N, K;
long long R[1000], H[1000];

double solve() {
    scanf("%d%d", &N, &K);
    for (int i = 0; i < N; i++) {
        scanf("%lld%lld", R + i, H + i);
        a[i] = make_pair(2 * R[i] * H[i], R[i] * R[i]);
    }
    sort(a, a + N);
    long long mx = a[N - 1].second, mn = a[N - 1].first;
    long long ans = 0;
    for (int i = 0; i < K; i++) {
        ans += a[N - i - 1].first;
        mx = max(mx, a[N - i - 1].second);
        mn = min(mn, a[N - i - 1].first);
    }
    ans += mx;
    long long wer = 0;
    for (int i = 0; i < N - K; i++)
        if (mx < a[i].second && a[i].second - mx + a[i].first - mn > wer) {
            wer = a[i].second - mx + a[i].first - mn;
        }
    return 3.14159265358979323846 * (ans + wer);
}

int main() {
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; i++)
        printf("Case #%d: %.9lf\n", i, solve());
}
