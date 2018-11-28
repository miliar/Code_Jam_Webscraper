#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <bitset>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>
#include <queue>
#include <memory.h>
#include <cmath>

using namespace std;

#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define FOR0(i,n) for( i = 0 ; i < n ; ++i )
#define FOR1(i,n) for( i = 1 ; i <= n ; ++i )
#define FI first
#define SE second
#define pb push_back
#define mp make_pair

typedef long long LL;

int T, _T;

int n, r, o, y, g, b, v;

string ans;

bool try_solve() {
    ans = "";
    set<pair<int, char>> st;
    if (r)
        st.insert(mp(-r, 'R'));
    if (y)
        st.insert(mp(-y, 'Y'));
    if (b)
        st.insert(mp(-b, 'B'));
    while (!st.empty()) {
        if ( ans.length() == 0 ) {
            pair<int, char> tk = *st.begin();
            st.erase(tk);
            ans.pb(tk.SE);
            tk.FI += 1;
            if (tk.FI)
                st.insert(tk);
            continue;
        }
        if ((*(st.begin())).SE != ans.back()) {
            pair<int, char> tk = *st.begin();
            st.erase(tk);
            ans.pb(tk.SE);
            tk.FI += 1;
            if (tk.SE == 'R' && g > 0) {
                ans.pb('G');
                ans.pb('R');
                --g;
                tk.FI += 1;
            }
            else if (tk.SE == 'B' && o > 0) {
                ans.pb('O');
                ans.pb('B');
                --o;
                tk.FI += 1;
            }
            else if (tk.SE == 'Y' && v > 0) {
                ans.pb('V');
                ans.pb('Y');
                --v;
                tk.FI += 1;
            }
            if (tk.FI)
                st.insert(tk);
        }
        else if (st.size() > 1){
            pair<int, char> tk = *(++st.begin());
            st.erase(tk);
            ans.pb(tk.SE);
            tk.FI += 1;
            if (tk.SE == 'R' && g > 0) {
                ans.pb('G');
                ans.pb('R');
                --g;
                tk.FI += 1;
            }
            else if (tk.SE == 'B' && o > 0) {
                ans.pb('O');
                ans.pb('B');
                --o;
                tk.FI += 1;
            }
            else if (tk.SE == 'Y' && v > 0) {
                ans.pb('V');
                ans.pb('Y');
                --v;
                tk.FI += 1;
            }
            if (tk.FI)
                st.insert(tk);
        }
        else {
            return false;
        }
    }
    return ans[0] != ans.back();
}

bool try_solve2() {
    ans = "";
    set<pair<int, char>> st;
    if (r)
        st.insert(mp(-r, 'R'));
    if (y)
        st.insert(mp(-y, 'Y'));
    if (b)
        st.insert(mp(-b, 'B'));
    while (!st.empty()) {
        if ( ans.length() == 0 ) {
            pair<int, char> tk = *st.begin();
            st.erase(tk);
            ans.pb(tk.SE);
            tk.FI += 1;
            if (tk.FI)
                st.insert(tk);
            continue;
        }
        if ((*(st.begin())).SE != ans.back()) {
            pair<int, char> tk = *st.begin();
            st.erase(tk);
            ans.pb(tk.SE);
            tk.FI += 1;
            if (tk.SE == 'R' && g > 0) {
                ans.pb('G');
                ans.pb('R');
                --g;
                tk.FI += 1;
            }
            else if (tk.SE == 'B' && o > 0) {
                ans.pb('O');
                ans.pb('B');
                --o;
                tk.FI += 1;
            }
            else if (tk.SE == 'Y' && v > 0) {
                ans.pb('V');
                ans.pb('Y');
                --v;
                tk.FI += 1;
            }
            if (tk.FI)
                st.insert(tk);
        }
        else if (st.size() > 1){
            pair<int, char> tk = *(++st.begin());
            st.erase(tk);
            ans.pb(tk.SE);
            tk.FI += 1;
            if (tk.SE == 'R' && g > 0) {
                ans.pb('G');
                ans.pb('R');
                --g;
                tk.FI += 1;
            }
            else if (tk.SE == 'B' && o > 0) {
                ans.pb('O');
                ans.pb('B');
                --o;
                tk.FI += 1;
            }
            else if (tk.SE == 'Y' && v > 0) {
                ans.pb('V');
                ans.pb('Y');
                --v;
                tk.FI += 1;
            }
            if (tk.FI)
                st.insert(tk);
        }
        else {
            return false;
        }
    }
    if (ans.size() > 2) {
        swap(ans[ans.size() - 1], ans[ans.size() - 2]);
        if (ans[ans.size() - 2] != ans[ans.size() - 3])
            return ans[0] != ans.back();
    }
    return false;
}

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    ios::sync_with_stdio(false);
    cin >> T;
    for (_T = 1; _T <= T; ++_T) {
        cout << "Case #" << _T << ": ";
        cin >> n >> r >> o >> y >> g >> b >> v;
        if (2 * g > r || 2 * o > b || 2 * v > y) {
            cout << "IMPOSSIBLE\n";
            continue;
        }
        if (try_solve()) {
            cout << ans << endl;
            continue;
        }
        else if (try_solve2()) {
            cout << ans << endl;
        }
        else {
            cout << "IMPOSSIBLE\n";
            continue;
        }
    }
}