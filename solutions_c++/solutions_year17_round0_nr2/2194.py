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

vector <int> to_vec(int x) {
    vector <int> result;
    if (x == 0) {
        result.push_back(0);
    }
    while (x) {
        result.push_back(x % 10);
        x /= 10;
    }
    reverse(all(result));
    return result;
}


void construct(const vector <int>& N, bool already_lower, int pos, vector <int>& curRes, bool& succeded) {
    if (pos == N.size()) {
        succeded = true;
        return;
    }
    
    int prevNum = 1;
    if (curRes.size()) {
        prevNum = curRes.back();
    }
    
    if (already_lower) {
        for (int i = 9; i >= prevNum; --i) {
            curRes.push_back(i);
            construct(N, already_lower, pos + 1, curRes, succeded);
            if (succeded) {
                return;
            } else {
                curRes.pop_back();
            }
        }
    } else {
        for (int i = N[pos]; i >= prevNum; --i) {
            curRes.push_back(i);
            
            if (i < N[pos]) {
                construct(N, true, pos + 1, curRes, succeded);
            } else {
                construct(N, false, pos + 1, curRes, succeded);
            }
            if (succeded) {
                return;
            } else {
                curRes.pop_back();
            }
        }
    }
}

void solve() {
    int N;
    cin >> N;
    vector <int> vecN = to_vec(N);
    
    vector <int> ans;
    bool succeded = false;
    construct(vecN, false, 0, ans, succeded);
    if (!succeded) {
        ans = vector <int> (vecN.size() - 1, 9);
    }
    for (int x: ans) {
        cout << x;
    }
    cout << "\n";
}
