#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <bitset>
#include <ctime>
#include <algorithm>
#define ll long long
#define mp make_pair

using namespace std;

string s;
int n, T;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output", "w", stdout);
    
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> s;
        cin >> n;
        int ans = 0;
        for (int i = 0; i + n <= s.size(); ++i)
            if (s[i] == '-') {
                ++ans;
                for (int q = 0; q < n; ++q)
                    s[i + q] = (s[i + q] == '+' ? '-' : '+');
            }
        bool good = 1;
        cout << "Case #" << t << ": ";
        for (auto ch : s)
            if (ch == '-') good = 0;
        if (good) cout << ans << "\n";
        else cout << "IMPOSSIBLE\n";
    }

    return 0;
}

/*

3
2 2
5 2
222 4

*/