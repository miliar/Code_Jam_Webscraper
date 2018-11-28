#include <bits/stdc++.h>

using namespace std;

map<vector<int>, int> mem;

struct Solver {

    int calc(vector<int> v) {
        if (accumulate(v.begin(), v.end(), 0) == 0)
            return 0;
        if (mem.count(v))
            return mem[v];
        mem[v] = 0;
        int P = v.size();
        int tot = 0;
        for (int i = 0; i < P; i++)
            tot += i * v[i];
        for (int i = 0; i < P; i++) {
            if (!v[i])
                continue;
            v[i]--;
            int ans = calc(v);
            v[i]++;
            int cur = tot - i;
            if (cur % P == 0)
                ans++;
            mem[v] = max(mem[v], ans);
        }
        return mem[v];
    }

    void solve() {
        int n;
        cin >> n;
        int P;
        cin >> P;
        vector<int> cnt(P);
        for (int i = 0; i < n; i++) {
            int x;
            cin >> x;
            cnt[x % P]++;
        }
        cout << calc(cnt) << endl;
    }
};

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(nullptr);
    cout.setf(ios::fixed);
    cout.precision(20);
    int ts;
    cin >> ts;
    for (int t = 1; t <= ts; t++) {
        cout << "Case #" << t << ": ";
        Solver solver;
        solver.solve();
    }
}
