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
    string num;
    cin >> num;
    int idx = -1;
    int len = num.length();
    for (int i = 1; i < len; ++i) {
        if (num[i] < num[i - 1]) {
            idx = i - 1;
            break;
        }
    }
    if (idx == -1) {
        cout << num << endl;
        return;
    }
    while (idx - 1 >= 0 && num[idx] - 1 < num[idx - 1]) --idx;
    num[idx] -= 1;
    for (int i = idx + 1; i < len; ++i) num[i] = '9';
    if (num[0] == '0') num = num.substr(1);
    cout << num << endl;
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
