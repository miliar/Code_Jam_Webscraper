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
#define sys_p system( "pause" )
#define pb push_back
#define mp make_pair
#define FI first
#define SE second
#define sz(a) (int)a.size()

typedef long long LL;

int T, _T;

int i, j;
string r;
int s[1000], l, cnt;

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin >> _T;
    FOR1(T, _T) {
        cin >> r >> l;
        FOR0(i, r.length()) {
            if (r[i] == '-')
                s[i] = 0;
            else
                s[i] = 1;
        }
        cnt = 0;
        FOR0(i, r.length() - l + 1) {
            if (s[i] == 0) {
                cnt += 1;
                for (j = i; j < i + l; ++j) {
                    s[j] = (s[j] + 1) % 2;
                }
            }
        }
        string ans = to_string(cnt);
        FOR0(i, r.length()) {
            if (s[i] == 0) {
                ans = "IMPOSSIBLE";
                break;
            }
        }
        cout << "Case #" << T << ": " << ans << endl;
    }
}