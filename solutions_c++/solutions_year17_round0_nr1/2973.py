#include <functional>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <numeric>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <string>
#include <vector>
#include <bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <list>
#include <set>
#include <map>

using namespace std;

int main() {
    freopen("A-large.in" , "r" , stdin);
    freopen("a.out" , "w" , stdout);

    int T;
    cin >> T;

    for (int kase = 0; kase < T; kase++) {
        string s;
        int k;
        cin >> s >> k;

        int ans = 0;
        for (int i = 0; i <= s.length() - k; i++) {
            if (s[i] == '+') {
                continue;
            }
            ans++;
            for (int j = i; j < i + k; j++) {
                if (s[j] == '+') {
                    s[j] = '-';
                } else {
                    s[j] = '+';
                }
            }
        }
        for (int i = s.length() - k; i < s.length(); i++) {
            if (s[i] == '-') {
                ans = -1;
            }
        }

        cout << "Case #" << kase + 1 << ": ";
        if (ans == -1) {
            cout << "IMPOSSIBLE" << endl;
        } else {
            cout << ans << endl;
        }
    }
    return 0;
}
