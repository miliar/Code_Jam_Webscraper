#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

int N, C, M;

void solve() {
    cin >> N >> C >> M;
    vector<int> A(N + 1, 0);
    vector<int> B(C, 0);
    vector<int> D(N + 1, 0);
    for(int m = 0; m < M; ++m) {
        int p, b;
        cin >> p >> b;
        for(int i = p; i<= N; ++i) ++A[i];
        ++B[b - 1];
        ++D[p];
    }
    int ans1 = 0;
    for(int n = 1; n <= N; ++n)
        ans1 = max(ans1, (A[n] - 1) / n + 1);
    for(int c = 0; c < C; ++c)
        ans1 = max(ans1, B[c]);
    int ans2 = 0;
    for(int n = 1; n <= N; ++n)
        ans2 += max(0, D[n] - ans1);
    cout << ans1 << ' ' << ans2;
}

int main() {
    int T;
    cin >> T;
    for(int t = 1; t <= T; ++t) {
        printf("Case #%d: ", t);
        solve();
        printf("\n");
    }
}
 
