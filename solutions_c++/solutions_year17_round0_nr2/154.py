#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <stack>
#include <set>
#include <queue>
#include <functional>
#include <map>
#include <bitset>

#define INF 0x7fffffff
#define REP(i,j,k) for(int i = j;i <= k;i++)
#define squr(x) (x) * (x)
#define lowbit(x) (x&(-x))
#define getint(x) scanf("%d", &(x))

typedef long long LL;

using namespace std;

int n, m;
int T;
char s[20];
char sans[20];
int t[20];

bool check(int len) {
    for (int i = 1; i < len; i++) {
        if (s[i] < s[i- 1]) {
            return false;
        }
    }
    return true;
}

int main(int argc, const char * argv[]) {
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin >> T;
    REP(ca, 1, T) {
        cin >> s;
        LL ans = -1;
        int len = (int)strlen(s);
        LL temp;
        REP(i, 0, len - 1) {
            t[i] = s[i] - '0';
        }
        for (int i = 1; i < len; i++) {
            for (int j = 0; j < i; j++) {
                sans[j] = s[j];
            }
            if (s[i] > s[i - 1] && check(i)) {
                sans[i] = s[i] - 1;
            } else {
                continue;
            }
            for (int j = i + 1; j < len; j++) {
                sans[j] = '9';
            }
            sans[len] = '\0';
            sscanf(sans, "%lld", &temp);
            ans = max(ans, temp);
        }
        sans[0] = s[0] - 1;
        for (int j = 1; j < len; j++) {
            sans[j] = '9';
        }
        sans[len] = '\0';
        sscanf(sans, "%lld", &temp);
        ans = max(ans, temp);
        if (check(len)) {
            sscanf(s, "%lld", &temp);
            ans = max(ans, temp);
        }
        printf("Case #%d: %lld\n", ca, ans);
    }
    
    return 0;
}









