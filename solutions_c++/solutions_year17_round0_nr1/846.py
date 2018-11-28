#include <algorithm>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <string>
#include <cstring>
using namespace std;

#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define RFOR(i,a,b) for(int i=(a);i>=(b);--i)
typedef long long LL;

void run() {
    string s;
    int k;
    cin >> s >> k;
    int len = s.length();
    int res = 0;
    for (int i = 0; i <= len - k; ++i) {
        if (s[i] == '+') continue;
        ++res;
        for (int j = 0; j < k; ++j) {
            s[i + j] = (s[i + j] == '-' ? '+' : '-');
        }
    }
    for (int i = len - k + 1; i < len; ++i) {
        if (s[i] == '-') {
            cout << "IMPOSSIBLE" << endl;
            return;
        }
    }
    cout << res << endl;
}

int main() {
    int k;
    cin >> k;
    FOR(c,1,k) {
        cout << "Case #" << c << ": ";
        run();
    }
    return 0;
}
