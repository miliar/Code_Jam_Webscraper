#include <string>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <iostream>
#include <cassert>
#include <iomanip>
using namespace std;

#define INF 1e+9
#define mp make_pair
#define lint long long

char revert(char x) {
    if (x == '+') return '-';
    if (x == '-') return '+';
}

int main() {
    ios_base::sync_with_stdio(false);
    cout << setprecision(10) << fixed;
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        string s; 
        int k;
        cin >> s >> k;
        int ans = 0;
        for (int j = 0; j < s.length(); j++) {
            if (s[j] == '-') {
                if (j + k > s.length()) {
                    ans = -1;
                    break;
                }
                ans++;
                for (int l = 0; l < k; l++)
                    s[j + l] = revert(s[j + l]);
            }
        }
        if (ans != -1)
            cout << "Case #" << i+1 << ": " << ans << endl;
        else
            cout << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl;
    }

}
