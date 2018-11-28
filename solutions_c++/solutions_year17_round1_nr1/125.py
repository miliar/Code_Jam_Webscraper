#include <iostream>
#include <fstream>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <bitset>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <queue>
#include <functional>

#define mp make_pair
#define pb push_back


typedef long long ll;
typedef long long llong;
typedef long double ld;

using namespace std;

#ifndef LOCAL
#define cerr _cer
struct _cert
{
    template <typename T> _cert& operator << (T) { return *this; }
};
_cert _cer;
#endif

template <typename T> void dprint(T begin, T end) {
    for (auto i = begin; i != end; i++) {
		cerr << (*i) << " ";
    }
    cerr << "\n";
}
int n, m;
string s[120];

void solve() {
    cin >> n >> m;
    for (int i = 0; i < n; ++i)
        cin >> s[i];
    int lst = -1;
    for (int i = 0; i < n; ++i) {
        int fl = 0;
        for (int j = 0; j < m; ++j)
            if (s[i][j] != '?')
                fl = 1;
        if (!fl && lst == -1)
            continue;
        if (!fl) {
            for (int j = 0; j < m; ++j)
                s[i][j] = s[i - 1][j];
        }
        else {
            char fs = 0;
            for (int j = 0; j < m; ++j)
                if (s[i][j] != '?') {
                    fs = s[i][j];
                    break;
                }
            for (int j = 0; j < m; ++j) {
                if (s[i][j] == '?')
                    s[i][j] = fs;
                else
                    fs = s[i][j];
            }
            if (lst == -1) {
                for (int k = 0; k < i; ++k)
                    for (int j = 0; j < m; ++j)
                        s[k][j] = s[i][j];
                lst = 1;
            }
        }
    }
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
            assert(s[i][j] != '?');
    for (int i = 0; i < n; ++i)
        cout << s[i] << "\n";
}

int main() {
    int tt;
    cin >> tt;
    for (int i = 0; i < tt; ++i) {
        printf("Case #%d:\n", i + 1);
        solve();
    }
	return 0;
}


