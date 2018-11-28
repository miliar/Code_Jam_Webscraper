// Nurbakyt Madibek
// Look at my code! IT'S AWESOME

#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <algorithm>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <ctime>
#include <queue>
#include <stack>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <cassert>
#include <unordered_map>
#include <bitset>
#include <unordered_set>

using namespace std;

#define pb push_back
#define pp pop_back
#define f first
#define s second
#define mp make_pair
#define sz(a) (int)((a).size())
#ifdef _WIN32
#  define I64 "%I64d"
#else
#  define I64 "%lld"
#endif
#define fname "."

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair < int, int > pi;
typedef pair < double, double > pd;

const int mod = (int)1e9 + 7;
const int inf = (int)1e9 + 123;
const ll infl = (ll)1e18 + 123;
const double eps = 1e-12;

const int MAX_N = (int)1e6 + 123;

int n;
int cnt[6];

void bad() {
    printf("IMPOSSIBLE\n");
    return;
}

map < pair < int, vector < int > >, int > used;
queue < pair < int, vector < int > > > q;

char c[3] = {'R', 'Y', 'B'};

void output(int last) {
    vector < int > now = {0, 0, 0};
    string ans = "";
    for (int i = n; i > 0; i--) {
        ans += c[last];
        int add = last;
        last = used[mp(last, now)];
        now[add]++;
    }
    cout << ans << endl;
}

map < char, int > CNT;

char cc[6] = {'R', 'O', 'Y', 'G', 'B', 'V'};

bool check(string &s) {
    CNT.clear();
    for (auto i : s)
        CNT[i]++;
    for (int i = 0; i < 6; i++) {
        if (cnt[i] != CNT[cc[i]]) {
            cout << "asdfasdfadsf" << endl;
            cout << s << endl;
            exit(0);
        }
    }
    return 1;
}

void solve() {
    scanf("%d", &n);
    for (int i = 0; i < 6; i++) {
        scanf("%d", &cnt[i]);
    }
    
    vector < pair < int, string > > q = {mp(cnt[0], "R"), mp(cnt[2], "Y"), mp(cnt[4], "B")};
    
    
    sort(q.begin(), q.end());
    if (!q[0].f) {
        if (!q[1].f) {
            if (q[2].f > 1) {
                bad();
            } else {
                cout << q[2].s << endl;
            }
            return;
        } else {
            if (q[1].f != q[2].f) {
                bad();
            } else {
                for (int i = 0; i < q[1].f; i++)
                    cout << q[1].s << q[2].s;
                printf("\n");
            }
            return;
        }
    }
    
    if (q[2].f > q[0].f + q[1].f) {
        bad();
        return;
    }
    int last = q[0].f + q[1].f - q[2].f;
    string ans = "";
    for (int i = 0; i < last; i++)
        ans += q[1].s + q[0].s + q[2].s;
    q[0].f -= last, q[1].f -= last;
    for (int i = 0; i < q[1].f; i++)
        ans += q[1].s + q[2].s;
    for (int i = 0; i < q[0].f; i++)
        ans += q[0].s + q[2].s;
    check(ans);
    cout << ans << endl;
}

int main() {
#ifdef DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int numberOfTests;
    scanf("%d", &numberOfTests);
    for (int i = 1; i <= numberOfTests; i++) {
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}

