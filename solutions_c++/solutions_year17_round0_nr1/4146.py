/** @xigua */
#include<cstdio>
#include<cmath>
#include<iostream>
#include<algorithm>
#include<vector>
#include<stack>
#include<cstring>
#include<queue>
#include<set>
#include<string>
#include<map>
#include<climits>
#define PI acos(-1)
using namespace std;
typedef long long ll;
typedef double db;
const int maxn = 2e2 + 5;
const int mod = 1e9 + 7;
const int INF = 1e8 + 5;
const ll inf = 1e15 + 5;
const db eps = 1e-6;

void solve() {
    char s[1005]; int k;

    scanf("%s%d", s+1, &k);
    int len = strlen(s + 1);
    int ans = 0;
    for (int i = 1; i <= len; i++) {
        if (i + k - 1 > len) break;
        if (s[i] == '-') {
            ans++;
            for (int j = i; j <= i + k - 1; j++) {
                if (s[j] == '+') s[j] = '-';
                else s[j] = '+';
            }
        }
      //  for (int j = 1; j <= len; j++)
     //       cout << s[j];
     //   cout << endl;
    }
    int flag = 1;
    for (int i = 1; i <= len; i++) {
     //   cout << s[i];
        if (s[i] == '-') flag = 0;
    }
    if (flag) cout << ans << endl;
    else cout << "IMPOSSIBLE\n";
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t = 1, cas = 1;
    cin >> t;
    //init();
    while(t--) {
        printf("Case #%d: ", cas++);
        solve();
    }
    return 0;
}
