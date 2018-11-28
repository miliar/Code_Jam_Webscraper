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

int tc;

ll  n, k, x, y, low, hi;
map<ll, ll> m;
map<ll, ll>::iterator it;

int main() {
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    scanf("%i", &tc);
    for(int tt = 1; tt <= tc; ++tt) {
        scanf("%lld%lld", &n, &k);
        
        m.clear();
        m[n] = 1;

        while (k) {
            it = m.end();
            it--;
            x = it->first;
            y = it->second;
            m.erase(it);
            low = (x - 1) / 2;
            hi = (x - 1) - low;

            m[low] = m[low] + y;
            m[hi] = m[hi] + y;

            if (y >= k) break;
            k -= y;
        }
        printf("Case #%i: %lld %lld\n", tt, hi, low);
    }
    return 0;
}