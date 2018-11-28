/******************************************************************************\
*                         Author:  Dumbear                                     *
*                         Email:   dumbear[#at]163.com                         *
*                         Website: http://dumbear.com                          *
\******************************************************************************/
#include <algorithm>
#include <bitset>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <typeinfo>
#include <utility>
#include <vector>

using namespace std;

#define output(x) cout << #x << ": " << (x) << endl;

typedef long long LL;
typedef vector<int> VI;
typedef vector<long long> VL;
typedef vector<double> VD;
typedef vector<string> VS;

const int max_len = 30;

int t, n;
char num[max_len];

bool check(int k) {
    for (int i = k + 1; i < n; ++i) {
        if (num[i] > num[k]) {
            return true;
        }
        if (num[i] < num[k]) {
            return false;
        }
    }
    return true;
}

string get_max_tidy() {
    string res;
    for (int i = 0; i < n; ++i) {
        if (check(i)) {
            res += num[i];
        } else {
            if (num[i] == '1') {
                return string(n - i - 1, '9');
            }
            res += (num[i] - 1);
            res += string(n - i - 1, '9');
            return res;
        }
    }
    return res;
}

void solve() {
    scanf("%s", num);
    n = strlen(num);
    printf("Case #%d: %s\n", ++t, get_max_tidy().c_str());
}

int main() {
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i)
        solve();
    return 0;
}
