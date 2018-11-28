#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <vector>
#include <stack>
#include <map>
#include <set>
#include <cmath>
#include <cctype>
#include <ctime>
#include <cassert>

using namespace std;

#define REP(i, n) for (int i = 0; i < (n); ++i)
#define eps 1e-9

typedef long long ll;
typedef pair<int, int> pii;

const int INF = 0x7fffffff;
int T;
string str;
int n;

bool is_in(int x) {
    int t = INF;
    while (x) {
        if (x % 10 > t) { return false; }
        t = x % 10; x /= 10;
    }
    return true;
}

int main() {
//#ifdef __AiR_H
//    freopen("B-large.in", "r", stdin);
//    freopen("B-large.out", "w", stdout);
//#endif // __AiR_H
    scanf("%d", &T);
    int Case = 0;
    while (T--) {
        printf("Case #%d: ", ++Case);
        cin >> str;
        bool flag = true;
        int len = str.length();
        int cur = 0;
        for (int i = 1; i < len; ++i) {
            if (str[i] < str[i - 1]) { cur = i - 1; flag = false; break; }
        }
        if (flag) { cout << str << endl; continue; }
        for (int i = cur - 1; i >= 0; --i) {
            if (str[i] != str[cur]) { break; }
            cur = i;
        }
        string ans = "";
        for (int i = 0; i < cur; ++i) { ans += str[i]; }
        if (str[cur] != '1') { ans += (str[cur] - 1); }
        for (int i = cur + 1; i < len; ++i) { ans += '9'; }
        cout << ans << endl;
    }
    return 0;
}
