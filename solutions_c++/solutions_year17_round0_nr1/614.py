#include <memory.h>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <climits>
#include <cctype>
#include <cstring>
#include <climits>
#include <cmath>
#include <vector>
#include <string>
#include <memory>
#include <functional>
#include <set>
#include <map>
#include <bitset>
#include <stack>
#include <queue>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>
#include <iostream>

using namespace std;

#define PROFILE_START(i)    clock_t start##i = clock()
#define PROFILE_STOP(i)     fprintf(stderr, "elapsed time (" #i ") = %f\n", double(clock() - start##i) / CLOCKS_PER_SEC)

#define rep(i,n)        for (int i = 0; i < n; i++)
#define REP(i,s,e)      for (int i = s; i <= e; i++)
#define repr(i,n)       for (int i = n - 1; i >= 0; i--)
#define REPR(i,s,e)     for (int i = e; i >= s; i--)

#ifndef M_PI
#define M_PI       3.14159265358979323846   // pi
#define M_1_PI     0.318309886183790671538  // 1/pi
#define M_SQRT2    1.41421356237309504880   // sqrt(2)
#endif

typedef long long           ll;
typedef unsigned long long  ull;

typedef vector<int>     vi;
typedef pair<int, int>  pii;
typedef pair<ll, ll>    pll;
#define fi              first
#define se              second
#define pb              push_back
#define eb              emplace_back
#define em              emplace
#define mp              make_pair

#define MAXN    1000

string gS;
int gK;

int solve() {
    int res = 0;
    string s = gS;

    int n = (int)gS.length() - gK;
    for (int i = 0; i <= n; i++) {
        if (s[i] == '-') {
            for (int j = 0; j < gK; j++) {
                s[i + j] = (s[i + j] == '-') ? '+' : '-';
            }
            res++;
        }
    }

    for (int i = n; i < (int)gS.length(); i++) {
        if (s[i] == '-')
            return -1;
    }

    return res;
}

int main(void) {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;

    cin >> T;
    for (int tn = 1; tn <= T; tn++) {
        cin >> gS >> gK;

        int ans = solve();

        cout << "Case #" << tn << ": ";
        if (ans >= 0)
            cout << ans;
        else
            cout << "IMPOSSIBLE";
        cout << endl;
    }

    return 0;
}
