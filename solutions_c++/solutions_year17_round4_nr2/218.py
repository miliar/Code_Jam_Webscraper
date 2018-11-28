#include <bits/stdc++.h>

using namespace std;

const int INF = (int)1e9;

struct Solver {
    vector<int> cnt;
    
    int get_min(int rides) {
        int n = cnt.size();
        vector<int> dp(n + 1, INF);
        int ans = 0;
        int was = 0;
        for (int i = 1; i <= n; i++) {
            was += cnt[i - 1];
            if (was > i * rides)
                return INF;
            ans += max(0, cnt[i - 1] - rides); 
        }
        return ans;
    }

    void solve() {
        int n, c, m;
        cin >> n >> c >> m;
        cnt.resize(n);
        vector<int> customer(c);
        for (int i = 0; i < m; i++) {
            int pos, b;
            cin >> pos >> b;
            --pos;
            --b;
            customer[b]++;
            cnt[pos]++;
        }
        int low = *max_element(customer.begin(), customer.end()) - 1;
        int high = m;
        while (high - low > 1) {
            int mid = (low + high) / 2;
            if (get_min(mid) != INF)
                high = mid;
            else
                low = mid;
        }
        cout << high << " " << get_min(high) << endl;
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
