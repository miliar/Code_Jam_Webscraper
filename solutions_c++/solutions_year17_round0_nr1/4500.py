#include <cstdio>
#include <cstdlib>
#include <climits>
#include <cmath>
#include <cctype>
#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <utility>
#include <algorithm>
#include <bitset>
#include <iomanip>

using namespace std;

typedef long long int LLI;

#define _ ios_base::sync_with_stdio(0);

const int inf = 0x3f3f3f3f;
const double eps = 1e-8; 

int b[1005];

int main() { _
    int t, k;
    string str;
    cin >> t;
    for (int kase = 1; kase <= t; ++kase) {
        cout << "Case #" << kase << ": ";
        cin >> str >> k;
        for (int i = 0; i < str.length(); ++i) {
            b[i] = (str[i] == '+' ? 1 : 0);
        }

        int cnt = 0;
        for (int i = 0; i <= str.length()-k; ++i) {
            if (!b[i]) {
                ++cnt;
                for (int j = 0; j < k; ++j) {
                    b[i+j] = 1-b[i+j];
                }
            }
        }
        bool good = 1;
        for (int i = 0; i < str.length() && good; ++i) {
            good = b[i];
        }
        if (!good) cout << "IMPOSSIBLE\n";
        else cout << cnt << "\n";
    }

    return 0;
}
