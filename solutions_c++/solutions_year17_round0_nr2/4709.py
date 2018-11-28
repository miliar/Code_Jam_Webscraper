#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <assert.h>
#include <algorithm>
#include <vector>
#include <set>
#include <queue>
#include <unordered_map>
#include <string.h>
#include <bitset>

#define pb push_back
#define mp make_pair
#define fst first
#define snd second
#define ll long long
#define forn(i, n) for (int i = 0; i < (int) (n); i++)
#define forlr(i, l, r) for (int i = (int) l; i <= (int) (r); i++)
#define forrl(i, r, l) for (int i = (int) r; i >= (int) (l); i--)

using namespace std;

ll const MOD = 1000000007;
ll const LLINF = 1000000000000000000;
int const INF = 1000000000;

int const MAXN = 1000000;
set<ll> s;

void gen_tidy(int n, int min_x, ll x) {
    s.insert(x);
    // cout << x << "\n";
    if (n == 18) {
        return;
    }
    forlr(i, min_x, 9) {
        gen_tidy(n + 1, i, x * 10 + i);
    }
}


int main() {
    freopen("a.in", "rt", stdin);
    freopen("a.out", "wt", stdout);

    int t;
    cin >> t;
    gen_tidy(0, 1, 0);

    forn(cur_t, t) {
        ll n;
        cin >> n;

        ll res = *(--s.upper_bound(n));

        cout << "Case #" << cur_t + 1 << ": " << res << "\n";       
    }
    
    

    return 0;
}









