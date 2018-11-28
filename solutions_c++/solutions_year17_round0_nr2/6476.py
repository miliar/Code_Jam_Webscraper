#include <iostream>
#include <fstream>
#include <sstream>

#include <vector>
#include <set>
#include <bitset>
#include <map>
#include <deque>
#include <string>

#include <algorithm>
#include <numeric>

#include <cstdio>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cmath>

#define pb push_back
#define pbk pop_back
#define mp make_pair
#define fs first
#define sc second
#define all(x) (x).begin(), (x).end()
#define foreach(i, a) for (__typeof((a).begin()) i = (a).begin(); i != (a).end(); ++i)
#define len(a) ((int) (a).size())

#ifdef CUTEBMAING
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
#define eprintf(...) 42
#endif

using namespace std;

typedef long long int64;
typedef long double ld;
typedef unsigned long long lint;

const int inf = (1 << 30) - 1;
const int64 linf = (1ll << 62) - 1;
const int N = 19;

int64 n;

int digits[N];

int64 dp[N + 1][10][2];

void go(int i, int j, int z) {
    assert(dp[i][j][z] > 0);
    if (i == N) {
        return ;
    }
    for (int l = 9; l >= j; l--) {
        if (!z && l > digits[i]) {
            continue;
        }
        int ni = i + 1, nj = l, nz = z || l < digits[i]; 
        if (dp[ni][nj][nz] > 0) {
            digits[i] = l;
            go(ni, nj, nz);
            return ;
        }
    }
    assert(false);
}

void run() {
    cin >> n;
    for (int i = N - 1; i >= 0; i--) {
        digits[i] = n % 10;
        n /= 10;
    }
    memset(dp, 0, sizeof(dp));
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 2; j++) {
            dp[N][i][j] = 1;
        }
    }
    for (int i = N - 1; i >= 0; i--) {
        for (int j = 0; j < 10; j++) {
            for (int z = 0; z < 2; z++) {
                for (int l = j; l < 10; l++) {
                    if (!z && l > digits[i]) {
                        continue;
                    }
                    int ni = i + 1, nj = l, nz = z || l < digits[i];
                    dp[i][j][z] += dp[ni][nj][nz];
                }
            }
        }
    }
    go(0, 0, 0);
    int64 ans = 0;
    for (int i = 0; i < N; i++) {
        ans = ans * 10 + digits[i];
    }
    cout << ans << endl;
}

int main() {
#ifdef XCODE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int t; cin >> t;
    for (int i = 0; i < t; i++) {
        printf("Case #%d: ", i + 1);
        run();
    }
    return 0;
}
