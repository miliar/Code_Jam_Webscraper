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
        cout << "Case #" << TT + 1 << ": ";
        string s;
        cin >> s;
        REP(i,1,(int)s.size()) {
            if (s[i] < s[i - 1]) {
                REP(j,i,(int)s.size()) {
                    s[j] = '9';
                }
                s[i - 1]--;
                --i;
                while(i > 0 && s[i] < s[i - 1]) {
                    s[i - 1]--;
                    s[i] = '9';
                    --i;
                }
                break;
            }
        }
        int k = 0;
        while(k < (int)s.size() && s[k] == '0') {
            ++k;
        }
        REP(i,k,(int)s.size()) {
            cout << s[i];
        }
        cout << "\n";

    }
    return 0;
}