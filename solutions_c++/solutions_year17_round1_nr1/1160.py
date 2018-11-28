#include <algorithm>
#include <string>
#include <string.h>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <iostream>
#include <fstream>
#include <cmath>
#include <math.h>
#include <iomanip>
#include <stdlib.h>
#include <stdio.h>
#include <bitset>
#include <iterator>
#include <ctime>

using namespace std;

#define FOR(i, n) for (int i=0; i<n; ++i)
#define FORE(i, n) for (int i=0; i<=n; ++i)
#define REP(i, a, b) for (int i=a; i<b; ++i)
#define REPE(i, a, b) for (int i=a; i<=b; ++i)
#define mp make_pair
#define pb push_back

typedef long double dbl;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef long long int LL;
typedef vector<int> VI;
typedef vector<bool> VB;
typedef vector<VI> VVI;
const dbl pi = 3.14159265358979323846;
const int inf = (int) 1e9;
const dbl eps = 1e-9;


int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(false);

    int T;
    cin >> T;
    FOR(TT, T) {
        cout << "Case #" << TT + 1 << ":\n";
        int n,m;
        cin >> n >> m;
        char c[n][m];
        FOR(i,n) {
            FOR(j,m) {
                cin >> c[i][j];
            }
        }
        FOR(j,m) {
            int i = 0;
            while(i < n && c[i][j] == '?') {
                ++i;
            }
            char now = '?';
            if (i < n) {
                FOR(k,i) {
                    c[k][j] = c[i][j];
                }
                now = c[i][j];
            }
            while(i < n) {
                if (c[i][j] == '?') {
                    c[i][j] = now;
                } else {
                    now = c[i][j];
                }
                ++i;
            }
        }
        FOR(i,n) {
            int j = 0;
            while(j < m && c[i][j] == '?') {
                ++j;
            }
            FOR(k,j) {
                c[i][k] = c[i][j];
            }
            char now = c[i][j];
            while(j < m) {
                if (c[i][j] == '?') {
                    c[i][j] = now;
                } else {
                    now = c[i][j];
                }
                ++j;
            }
        }
        FOR(i,n) {
            FOR(j,m) {
                cout << c[i][j];
            }
            cout << "\n";
        }
    }
    return 0;
}