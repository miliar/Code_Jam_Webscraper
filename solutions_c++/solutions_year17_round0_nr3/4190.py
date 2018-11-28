#include <iostream>
#include <fstream>
#include <cstdio>
#include <iomanip>
#include <sstream>
#include <cstring>
#include <string>
#include <cmath>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <numeric>
#include <utility>
#include <functional>
#include <limits>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int ui;
typedef pair<int,int> pii;
typedef vector<vector<int> > graph;

const double pi = acos(-1.0);

#define oned(a, x1, x2) { cout << #a << ":"; for(int _i = (x1); _i < (x2); _i++){ cout << " " << a[_i]; } cout << endl; }
#define twod(a, x1, x2, y1, y2) { cout << #a << ":" << endl; for(int _i = (x1); _i < (x2); _i++){ for(int _j = (y1); _j < (y2); _j++){ cout << (_j > y1 ? " " : "") << a[_i][_j]; } cout << endl; } }

#define mp make_pair
#define pb push_back
#define fst first
#define snd second

ll n, k;

struct Elem {
    ll l, r, mn, mx;
    Elem() {}
    Elem(ll l, ll r) : l(l), r(r) {
        ll free = r-l;
        ll ls = free/2;
        ll rs = free-ls;
        mn = min(ls,rs);
        mx = max(ls,rs);
    }
    bool operator < (const Elem &e) const {
        if(mn != e.mn) {
            return mn > e.mn;
        } else if(mx != e.mx) {
            return mx > e.mx;
        } else {
            return l < e.l;
        }
    }
};

set<Elem> S;

void solve() {
    S.clear();
    S.insert(Elem(1,n));
    for(int i = 0; i < k-1; i++) {
        Elem e = *S.begin();
        S.erase(S.begin());
        ll pos = (e.l+e.r)/2;
        if(e.l<pos) {
            S.insert(Elem(e.l,pos-1));
        }
        if(pos<e.r) {
            S.insert(Elem(pos+1,e.r));
        }
    }
    Elem e = *S.begin();
    printf("%I64d %I64d\n", e.mx, e.mn);
}

int main() {
	freopen("C-small-2-attempt0.in", "r", stdin);
	freopen("C-small-2-attempt0.out", "w", stdout);

	int T; scanf("%d", &T);
	for(int C = 1; C <= T; C++) {
            cerr << C << endl;
        printf("Case #%d: ", C);

        scanf("%I64d %I64d", &n, &k);
        solve();
	}
}
