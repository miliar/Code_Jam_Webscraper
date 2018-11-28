#include <bits/stdc++.h>

using namespace std;
int cnt[1005];
int main() {
    ios_base::sync_with_stdio(0);
    int t;
    cin >> t;
    for (int test = 1; test <= t; test++) {
        for (int i = 0; i <= 1000; i++) cnt[i] = 0;
        string line;
        cout << "Case #" << test << ": ";
        int k;
        cin >> line >> k;
        int cost = 0;
        bool good = true;
        int sum = 0;
        for (int i = 0; i < line.size(); i++) {
            sum -= cnt[i];
            line[i] = line[i] == '+';
            line[i] = (line[i] + sum) % 2;
            if (line[i] % 2 == 0 && i + k <= line.size()) {
                cnt[i + k]++;
                cost++;
                sum++;
            }
            if (line[i] % 2 == 0 && i + k > line.size()) {
                good = false;
            }
        }
        if (good) cout << cost << endl;
            else cout << "IMPOSSIBLE" << endl;
    }
    
    return 0;
}