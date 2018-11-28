#include <stdio.h>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <cstring>
#include <cassert>
#include <bitset>
#include <sstream>
#include <queue>

#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define sz(a) ((int) (a).size())
#define eprintf(...) fprintf(stderr, __VA_ARGS__)

using namespace std;

typedef long long int64;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const long long inf64 = ((long long)1 << 62) - 1;
const long double pi = acos(-1);

template <class T> T sqr (T x) {return x * x;}
template <class T> T abs (T x) {return x < 0 ? -x : x;}

int main () {
    ios_base::sync_with_stdio(0);
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int tc;
    cin >> tc;
    for (int ti = 0; ti < tc; ++ti) {
        long long n;
        cin >> n;

        long long cur = 1;
        while (cur <= n) {
            cur = 10 * cur + 1;
        }

        long long res = 0;
        while (cur > 0) {
            while (res % 10 != 9 && res + cur <= n) {
                res += cur;
            }
            cur /= 10;
        }
        
        cout << "Case #" << ti + 1 << ": " << res << endl;
    }

    return 0;
}