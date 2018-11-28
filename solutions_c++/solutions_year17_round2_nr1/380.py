#include <bits/stdc++.h>
using namespace std;
using i64 = int64_t;

struct Tp {
    int x, s;

    bool operator<(const Tp& other) const {
        return x < other.x || (x == other.x && s > other.s);
    }
};

int main() {
    freopen(".in", "r", stdin);
    freopen(".out", "w", stdout);
    ios::sync_with_stdio(false);

    int T;
    cin >> T;
    for (int __ =1; __ <= T; ++__) {
        int D, N;
        cin >> D >> N;

        vector<Tp> A(N);
        for (int i = 0; i < N; ++i) {
            cin >> A[i].x >> A[i].s;
        }
        sort(A.begin(), A.end());

        double t = 0;
        for (int i = N - 1; i >= 0; --i) {
            double newt = double(D - A[i].x) / A[i].s;
            t = max(newt, t);
        }

        cout.precision(12);
        cout << "Case #" << __ << ": " << fixed << D / t << endl;
    }

    return 0;
}
