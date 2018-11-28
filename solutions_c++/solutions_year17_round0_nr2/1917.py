#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
using namespace std;

typedef long long LL;

int T, cas = 1;
string s;
int main() {
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    scanf("%d", &T);
    while (cas <= T) {
        cin >> s;
        bool bigger = false;
        for (int i = s.length() - 1; i >= 0; i--) {
            bool ascending = true;
            for (int j = 1; j < i; j++)
                if (s[j] < s[j - 1]) {
                    ascending = false;
                    break;
                }
            bool ascending_i = false;
            if (ascending && (i == 0 || s[i - 1] <= s[i])) ascending_i = true;
            if (!bigger && ascending_i) break;
            if (s[i] > '0' && ascending && (i == 0 || s[i - 1] <= s[i] - 1)) {
                s[i] = s[i] - 1;
                break;
            }
            if (s[i] < '9') bigger = true;
            s[i] = '9';
        }
        printf("Case #%d: %lld\n", cas, stoll(s));
        cas++;
    }
    return 0;
}