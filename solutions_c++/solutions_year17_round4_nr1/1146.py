#include <vector>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <string>
#include <map>
#include <deque>
#include <set>
#ifdef __GXX_EXPERIMENTAL_CXX0X__
#include <unordered_map>
#include <cassert>
#endif
#include <ctime>
#include <queue>
#include <stack>
#include<iomanip>
#include <sstream>
#include <cmath>
//#include "utils/haha.h"
//#include "utils/max_flow.h"
using namespace std;
typedef pair<int, int> PII;
typedef pair<string, string> PSS;
typedef pair<string, int> PSI;
typedef pair<int, PII> PIP;
typedef long long ll;
typedef pair<ll, ll> PLL;
typedef pair<double, double> PDD;
typedef pair<ll, PII> PLP;
#define CLS(x, v) (memset((x), (v), sizeof((x))))
const double pi = acos(-1);
const int mod = 1000000007;
const int inf = 0x3fffffff;

void solve(int ncase) {
    cout << "Case #" << ncase << ": ";
    int n, p;
    cin >> n >> p;
    vector<int> num(n);
    vector<int> cnt(p);
    for(int i = 0; i < n; i++) {
        cin >> num[i];
        cnt[num[i] % p] ++;
    }
    int ans = cnt[0];
    if (p == 2) {
        cout << ans + (cnt[1] + 1) / 2 << endl;    
    } else if (p == 3) {
        int z = min(cnt[1], cnt[2]);
        cnt[1] -= z;
        cnt[2] -= z;
        cout << ans + z + (2 + cnt[1] + cnt[2]) / 3 << endl;
    } else {
        int z = min(cnt[1],  cnt[3]);
        cnt[1] -= z;
        cnt[3] -= z;
        ans += z;
        ans += cnt[2] / 2;
        cnt[2] %= 2;
        z = max(cnt[1], cnt[3]);
        if (cnt[2] == 1 && z >= 2) {
            z -= 2;
            cnt[2] --;
            ans++;
        }
        ans += (z + 3) / 4;
        if (z % 4 == 0 && cnt[2] > 0) ans++;
        cout << ans << endl;
    }
}

int main() {
    //ios::sync_with_stdio(false);
    cout << std::fixed;
    cout << setprecision(9);
#ifdef _zzz_
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
#endif
    //precalc();
    int T = 1;
    //scanf("%d", &T);
    cin >> T;
    int ncase = 0;
    while(T --) {
        solve(++ ncase);
    }
}
