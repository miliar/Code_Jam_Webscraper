#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

int solve(string& s, int K) {
    int ans = 0;
    for (int i = 0; i + K - 1 < s.size(); ++i) {
        if (s[i] == '-') {
            for (int x = i; x < i + K; ++x) {
                s[x] = (s[x] == '-' ? '+' : '-');
            }
            ++ans;
        }
    }
    return ans;
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        string s;
        int K;
        cin >> s >> K;
        int ans = solve(s, K);
        bool exists = true;
        for (int i = 0; i < s.size() && exists; ++i) {
            exists &= (s[i] == '+');
        }
        cout << "Case #" << t << ": ";
        if (exists) {
            cout << ans;
        }
        else {
            cout << "IMPOSSIBLE";
        }
        cout << endl;
    }
    return 0;
}
