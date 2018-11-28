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

//const ld eps = 1e-07;
const ld eps = 0;

void solve() {
    ld D;
    int n;
    
    cin >> D >> n;
    vector <ld> k(n);
    vector <ld> s(n);
    for (int i = 0; i < n; ++i) {
        cin >> k[i] >> s[i];
    }
    
    ld l = 0;
    ld r = 1000000000000000LL;
    
    for (int it = 0; it < 200; ++it) {
        ld m = (l + r) / 2;
        
        
        bool check = true;
        for (int i = 0; i < n; ++i) {
            if (m <= s[i]) {
                continue;
            }
            ld time = (k[i]) / (m - s[i]) ;
            if (time * m + eps < D) {
                check = false;
                break;
            }
        }
        
        if (check) {
            l = m;
        } else {
            r = m;
        }
    }
    
    cout << l << endl;
}
