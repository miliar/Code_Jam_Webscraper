
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

constexpr static int MAXN = 2000;
int N, C, M;
int p[MAXN], b[MAXN];

void solve() {
    cin >> N >> C >> M;
    vector <vector <int>> pos(C);
    vector <int> cnt(N);
    for (int i = 0; i < M; i++) {
        cin >> p[i] >> b[i];
        p[i]--;
        b[i]--;
        pos[b[i]].push_back(p[i]);
        cnt[p[i]]++;
    }

    int rides = 0;
    for (int j = 0; j < C; j++)
        rides = max(rides, (int) pos[j].size());

    int sum = 0;
    for (int i = 0; i < N; i++) {
        sum += cnt[i];
        rides = max(rides, (sum + i) / (i + 1));
    }
    // rides = max(rides, (M + N - 1) / N);

    vector <int> left(N);
    for (int i = 0; i < N; i++)
        left[i] = rides;

    int prom = 0;
    for (int i = 0; i < M; i++) {
        if (left[p[i]] > 0)
            left[p[i]]--;
        else
            prom++;
    }
    cout << rides << " " << prom << endl;
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": ";
        solve();
    }
}
