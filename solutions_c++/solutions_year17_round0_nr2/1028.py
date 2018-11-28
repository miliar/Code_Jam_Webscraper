#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <numeric>
#include <complex>

using namespace std;

typedef long long ll;

#define mp make_pair
#define pb push_back
#define PI 3.1415926535897932384626433832795

#define fill(x, v)  fillchar(x, v, sizeof(x))
typedef pair<int, int>  pii;
typedef vector<int>     vi;
typedef vector< pii >   vpii;

#define MAXD 25
int tc;

ll   d[MAXD];
ll   ans, ans2, n, nc;
int  k;
bool ok;

bool good(int x) {
    bool res = true;
    int prev = 10;
    while (x) {        
        res = res && (x % 10 <= prev);
        prev = x % 10;
        x = x / 10;
    }
    return res;
}

int brute(int x) {
    while (x) {
        if (good(x)) return x;
        x--;
    }
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    scanf("%i", &tc);
    for(int tt = 1; tt <= tc; ++tt) {
        scanf("%lld", &n);

        nc = n;
        k = 0;
        while (nc) {
            d[k++] = nc % 10;
            nc /= 10;
        }

        if (k == 1) ans = n; else {
            ans = 0;
            for(int i = 1; i < k; ++i) ans = ans * 10 + 9;
        }

        reverse(d, d + k);
        

        for(int i = 1; i < k; ++i) if (d[i] < d[i - 1]) {
            if (d[i - 1] == 1) break;
            int t = i - 1;
            for(int j = i - 1; j >= 0; --j) if (d[j] == d[i - 1]) t = j;
            d[t]--;
            for(int j = t + 1; j < k; ++j) d[j] = 9;

            //printf("i=%i\n", i);
            //for(int j=0; j<k; ++j) printf("%i ", d[j]); printf("\n");

            break;
        }

       
        ok = true;
        d[k] = 10;
        ans2 = 0;
        for(int i = 0; i < k; ++i) {
            ok = ok && d[i] <= d[i + 1];
            ans2 = ans2 * 10 + d[i];
        }



        if (ok) ans = max(ans, ans2);

        printf("Case #%i: %lld\n", tt, ans);

    }
    return 0;
}