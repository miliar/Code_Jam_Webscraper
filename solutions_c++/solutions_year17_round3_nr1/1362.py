#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <bitset>
#include <list>
#include <stack>
#include <queue>
#include <deque>
#include <string>
#include <sstream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <iomanip>

#define ff first
#define ss second
#define pb push_back
#define sz size

#define ms(x,v) memset((x), (v), sizeof(x))
#define bcnt(x) __builtin_popcount(x)

using namespace std;

typedef long long L;
typedef unsigned long long UL;
typedef double D;
typedef pair<L,L> PL;
typedef vector<L> VL;
typedef vector<VL> VVL;
typedef vector<PL> VPL;
typedef vector<VPL>VVPL;

#define _NO_USE_LOG
#ifdef _USE_LOG
#define LOG(x) cout << x;
#else
#define LOG(x)
#endif

const int MAXN = 2000;
const double PI = 3.14159265359;

int n,k;

PL ps[MAXN];
VL candidate_as;

L solve() {
    cin >> n >> k;

    for(int i = 0; i < n; ++i) {
        cin >> ps[i].ff >> ps[i].ss;
    }

    // sort(ps, ps + n, greater<PL>());

    L ans = 0;
    L aux, r_max;
    for(int i = 0; i < n; ++i) {
        r_max = ps[i].ff;
        aux = r_max * r_max + 2 * r_max * ps[i].ss;
        candidate_as.clear();
        for(int j = 0; j < n; ++j) {
            if(i != j && ps[j].ff <= r_max) {
                candidate_as.pb(2 * ps[j].ff * ps[j].ss);
            }
        }

        if((int)candidate_as.sz() >= k - 1) {
            sort(candidate_as.begin(), candidate_as.end(), greater<L>());
            for(int i = 0; i < k - 1; ++i) aux += candidate_as[i];
            ans = max(ans, aux);
        }
    }

    return ans;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin >> t;
    for(int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": ";
        cout << fixed << setprecision(10) << (PI * solve());
        cout << '\n';
    }
}
