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
char c;
vector<char> a;
int lp;

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin >> _T;
    FOR1(T, _T) {
        cout << "Case #" << T << ": ";

        bool solved = false;

        cin >> r;
        c = '0';
        FOR0(i, r.length()){
            if (r[i] > c) {
                lp = i;
                c = r[i];
            }
            else if (r[i] < c) {
                if (c > '1' || c == '1' && lp > 0) {
                    r[lp] -= 1;
                    for (j = lp + 1; j < r.length(); ++j) {
                        r[j] = '9';
                    }
                    FOR0(i, r.length()) {
                        cout << r[i];
                    }
                    cout << endl;
                }
                else {
                    a.resize(r.length() - 1);
                    FOR0(i, r.length() - 1) {
                        cout << '9';
                    }
                    cout << endl;
                }
                solved = true;
                break;
            }
        }
        if (!solved) {
            FOR0(i, r.length()) {
                cout << r[i];
            }
            cout << endl;
        }
    }
}