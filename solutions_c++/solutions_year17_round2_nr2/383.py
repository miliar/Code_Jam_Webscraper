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

void printerr() {
    cout << "IMPOSSIBLE\n";
}

bool check(const vector <char>& s) {
    if (s[0] == s.back()) {
        return false;
    }
    for (int i = 1; i < s.size(); ++i) {
        if (s[i] == s[i - 1]) {
            return false;
        }
    }
    return true;
}

void print(const vector <char>& s) {
    for (char c: s) {
        cout <<c;
    }
    cout << "\n";
}

void solve() {
    int n;
    cin >> n;
    vector <char> lets = {'R', 'O', 'Y', 'G', 'B', 'V'};
    vector <int> num(6);
    for (int i = 0; i < 6; ++i) {
        cin >> num[i];
    }
    
    for (int i = 0; i < 6; ++i) {
        if (num[i] == 0) {
            continue;
        }
        vector <int> curnum = num;
        vector <char> result(n);
        for (int j = 0; j < n; j += 2) {
            if (curnum[i]) {
                result[j] = lets[i];
                --curnum[i];
            } else {
                break;
            }
        }
        if (curnum[i]) {
            continue;
        }
        bool ok = true;
        for (int j = n - 1; j >= 0; --j) {
            if (result[j]) {
                continue;
            }
            bool found = false;
            for (int t = 0; t < 6; ++t) {
                if (curnum[t]) {
                    if (j + 1 < n && result[j + 1] == lets[t]) {
                        continue;
                    }
                    result[j] = lets[t];
                    --curnum[t];
                    found = true;
                    break;
                }
            }
            if (!found) {
                ok = false;
                break;
            }
        }
        if (ok && check(result)) {
            print(result);
            return;
        }
    }
    printerr();
}
