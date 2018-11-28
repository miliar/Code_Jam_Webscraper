#include <iostream>
#include <cstdio>
#include <vector>
#include <array>
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

class solver {
    int n, m, c;
    vector<pair<int, int> > tickets;
    vector<vector<pair<int, int> > > construct;
    vector<set<int> > persons;
    int get_diff(vector<pair<int, int> > vec) {
        vector<int> u;
        for (auto p : vec)
            u.pb(p.ff);
        sort(all(u));
        return unique(all(u)) - u.begin();
    }
public:
    pair<int, int> solve() {
        sort(all(tickets));
        for (auto p : tickets) {
            int where = -1;
            forn(i, construct.size()) {
                if ((int)construct[i].size() <= p.ff && !persons[i].count(p.ss))
                    if (where == -1 || construct[i].size() < construct[where].size())
                        where = i;
            }
            if (where == -1) {
                where = construct.size();
                construct.pb(vector<pair<int, int> >());
                persons.pb(set<int>());
            }
            construct[where].pb(p);
            persons[where].insert(p.ss);
        }
        int prom = 0;
        vector<int> nums(n, 0);
        for (auto p : tickets)
            nums[p.ff]++;
        forn(i, n)
            prom += max(0, nums[i] - (int)construct.size());
        return mp(construct.size(), prom);
    }
    void input() {
        cin >> n >> c >> m;
        forn(i, m) {
            int p; cin >> p; p--;
            int b; cin >> b; b--;
            tickets.pb(mp(p, b));
        }
    }
};

int main() {
    // Code here:
   
    int t; cin >> t;
    forn(i, t) {
        solver s;
        s.input();
        auto p = s.solve();
        cout << "Case #" << (i + 1) << ": " << p.ff << " " << p.ss << endl;
    }

    return 0;
}

