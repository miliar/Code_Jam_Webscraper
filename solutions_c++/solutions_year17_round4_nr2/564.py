#include <bits/stdc++.h>
using namespace std;

int main() {
    ifstream cin("B.in");
    ofstream cout("B.out");

    int t; cin >> t;

    for(int t_case = 1; t_case <= t; ++t_case) {
        cout << "Case #" << t_case << ": ";
        cerr << t_case << "\n";

        int n, c, m; cin >> n >> c >> m;
        
        vector<int> cnt(n, 0);
        vector<int> people(c, 0);

        for(int i = 0; i < m; ++i) {
            int p, b; cin >> p >> b;
            p--;b--;
            cnt[p]++;
            people[b]++;
        }
        
        auto getTry = [&] (int value) {
            vector<int> temp = cnt;
            int cost = 0;

            for(int i = 0; i < n; ++i) {
                while(temp[i] > value) {
                    bool found = false;
                    for(int j = i - 1; j >= 0; --j)
                        if(temp[j] < value) {
                            cost++;
                            found = true;
                            temp[i]--;
                            temp[j]++;
                            break;
                        }
                    if(not found)
                        return make_pair(false, -1);
                }
            }

            return make_pair(true, cost);
        };

        int ans = 0;
        for(int i = 0; i < c; ++i)
            ans = max(people[i], ans);

        int cost = -1;

        for(int lf = ans, rt = m; lf <= rt;) {
            int mid = (lf + rt) / 2;

            auto sol = getTry(mid);
            if(sol.first) {
                ans = mid;
                cost = sol.second;
                rt = mid - 1;
            } else {
                lf = mid + 1;
            }
        }
        
        cout << ans << " " << cost << "\n";
    }   
}
