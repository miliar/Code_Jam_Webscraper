/// OOOooo, moya oborona ///
#include <bits/stdc++.h>
#pragma pack(1)
#pragma GCC optimize("O3")

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector< pii > vii;
typedef long double ld;

#define pb push_back
#define mp make_pair
#define ins insert
#define ers erase

#define elif else if
#define all(v) (v).begin(),(v).end()
#define len(s) int((s).size())

#define fi first
#define se second
#define x first
#define y second

#define fpos krevedka
#define left Levo
#define right ishtenem
#define next nastupniy
#define prev poperedniy
#define div dilyty_sukotay

#define I64 "%lld"

#define I "%d"
#define II I I
#define III II I
#define IIII II II
#define IIIII III II
#define IIIIII III III
#define IIIIIII IIII III
#define IIIIIIII IIII IIII

#define dbg cout << "dbg\n"
#define files(name) freopen(name".in", "r", stdin);freopen(name".out","w", stdout);
#define UOIfiles(name) freopen(name".dat", "r", stdin);freopen(name".sol","w", stdout);


ll sqr(ll x) {return x * x;}

const ll md = 1e9 + 7;
const ll md2 = 2e9 + 7;
const ld PI = acos(-1);
const int MAXN = 5e5 + 1;
const int MAXLOG = 20;
const int INF = 1e9 + 1;
const ld INF_LD = 4e18 + 1;
const int RNG = 1e9;
const pii turns[4] = {{1, 0}, {0, -1}, {0, 1}, {-1, 0}};
const char signs[4] = {'D', 'L', 'R', 'U'};
const ld EPS = 1e-9;

///end template ///

multiset<int> ranges;


main () {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    //freopen("debugerr.txt", "w", stderr);
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    for(int test = 1; test <= t; test++) {
        cout << "Case #" << test << ": ";

        int n, k;
        cin >> n >> k;
        ranges.clear();
        ranges.ins(n);
        int l, r;
        for(int i = 0; i < k; i++) {
            int rng = *ranges.rbegin();
            ranges.ers(ranges.find(rng));
            l = (rng - 1) / 2;
            r = (rng) / 2;
            ranges.ins(l);
            ranges.ins(r);
        }

        cout << r << " " << l << "\n";
    }
}
