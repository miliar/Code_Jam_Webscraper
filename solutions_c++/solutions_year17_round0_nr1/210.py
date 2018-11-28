#include <bits/stdc++.h>
using namespace std;

int main() {
    ifstream cin("A.in");
    ofstream cout("A.out");

    int t; cin >> t;

    for(int t_case = 1; t_case <= t; ++t_case) {
        cout << "Case #" << t_case << ": ";

        string pancakes; cin >> pancakes;
        int k; cin >> k;
        int ans = 0;
        
        int n = pancakes.size();
        bool bad = false;

        for(int i = 0; i < n; ++i) {
            if(pancakes[i] == '-') {
                ans++;
                if(i + k - 1 >= n) {
                    bad = true;
                    break;
                } else {
                    for(int j = i; j <= i + k - 1; ++j)
                        if(pancakes[j] == '+') {
                            pancakes[j] = '-';
                        } else {
                            pancakes[j] = '+';
                        }
                }
            }
        }

        if(bad) {
            cout << "IMPOSSIBLE\n";
        } else {
            cout << ans << "\n";
        }
    }
}
