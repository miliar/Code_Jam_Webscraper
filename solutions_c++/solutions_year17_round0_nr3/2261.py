#pragma comment (linker, "/STACK:128000000")
#include <iostream>
#include <cstdio>
#include <fstream>
#include <functional>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <bitset>
#include <ctime>
#include <sstream>
#include <stack>
#include <cassert>
#include <list>
#include <deque>

using namespace std;

#define mp make_pair
#define pb push_back
#define all(a) a.begin(), a.end()

typedef long long li;
typedef long long i64;
typedef pair <int, int> pi;
typedef vector <int> vi;
typedef double ld;
typedef vector<int> vi;
typedef pair <int, int> pi;

void solve();

//int timer = 0;
#define FILENAME ""

int main() {
    string s = FILENAME;
#ifdef YA
    //assert(!s.empty());
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    //cerr<<FILENAME<<endl;
    //assert (s != "change me please");
    clock_t start = clock();
#else
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    //freopen(FILENAME ".in", "r", stdin);
    //freopen(FILENAME ".out", "w", stdout);
    cin.tie(0);
#endif
    cout.sync_with_stdio(0);
    cout.precision(10);
    cout << fixed;
    int t = 1;
    
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        //++timer;
        cout << "Case #" << i << ": ";
        solve();
    }
#ifdef YA
    cerr << "\n\n\n" << (clock() - start) / 1.0 / CLOCKS_PER_SEC << "\n\n\n";
#endif
    return 0;
}

#define int li

void solve() {
    int n, k;
    cin >> n >> k;
    
    --k;
    
    set <pair <int, int> > q;
    q.insert(mp(n, 1));
    
    while (k) {
        pair <int, int> cur = *q.rbegin();
        q.erase(cur);
        
        if (cur.second > k) {
            q.insert(mp(cur.first, cur.second - k));
            cur.second = k;
        }
        
        vector <pair <int, int> > to_add;
        k -= cur.second;
        
        if (cur.first & 1) {
            int new_len = cur.first / 2;
            if (new_len) {
                to_add.push_back(mp(new_len, cur.second * 2));
            }
        } else {
            to_add = {mp(cur.first / 2, cur.second), mp(cur.first / 2 - 1, cur.second)};
            if (to_add.back().first == 0) {
                to_add.pop_back();
            }
        }
        
        for (pair <int, int> tt: to_add) {
            auto it = q.lower_bound(mp(tt.first, -1));
            if (it != q.end() && it->first == tt.first) {
                tt.second += it->second;
                q.erase(it);
            }
            q.insert(tt);
        }
    }
    
    pair <int, int> ans = *q.rbegin();
    if (ans.first & 1) {
        cout << ans.first / 2 << " " << ans.first / 2 << endl;
    } else {
        cout << ans.first / 2 << " " << ans.first / 2  - 1 << endl;
    }
}
