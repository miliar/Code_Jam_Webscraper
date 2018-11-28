#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <algorithm>
#include <sstream>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <random>
#include <bitset>
#include <cassert>
#include <tuple>
#include <list>
#include <iterator>
#include <unordered_set>
#include <unordered_map>
#include <numeric>

using namespace std;

typedef long long ll;
typedef long double ld;

template<class htpe, class cmp>
using heap = priority_queue<htpe, vector<htpe>, cmp>;

template<class htpe>
using min_heap = heap<htpe, greater<htpe> >;

template<class htpe>
using max_heap = heap<htpe, less<htpe> >;

#define mp make_pair
#define pb push_back
#define mt make_tuple
#define ff first
#define ss second

#define forn(i, n) for (int i = 0; i < ((int)(n)); ++i)
#define forrn(i, s, n) for (int i = (int)(s); i < ((int)(n)); ++i)
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()

#define PYMOD(a, m) ((((a) % (m)) + (m)) % (m))

const int INF = 1791791791;
const ll INFLL = 1791791791791791791ll;

int solve(int test) {
    int n, k;
    cin >> n >> k;

    vector<pair<int, int> > cur;
    cur.pb(mp(0, n + 1));

    int ansl, ansr;
    
    while (k) {
        vector<pair<int, int> > nxt;
        forn(i, cur.size()) {
            int l, r;
            tie(l, r) = cur[i];
            int mid = (l + r) >> 1;
            if (l == r - 1)
                continue;
            k--;
            if (k == 0) {
                ansl = mid - l - 1;
                ansr = r - mid - 1;
                goto got_it;
            }
            nxt.pb(mp(mid, r));
            nxt.pb(mp(l, mid));
        }
        sort(all(nxt), [](const pair<int, int>& a, const pair<int, int>& b)-> bool {return a.ss - a.ff > b.ss - b.ff;});
        cur = nxt;
    }
 got_it:
    cout << "Case #" << test << ": " << ansr << " " << ansl << endl;
    return 0;
}

int main() {
    // Code here:
   
    int t;
    cin >> t;
    forn(i, t)
        solve(i + 1);

    return 0;
}

