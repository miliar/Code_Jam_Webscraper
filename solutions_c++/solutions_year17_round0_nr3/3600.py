#include <algorithm>
#include <map>
#include <iostream>
#include <cstdio>
#include <queue>
#define LL long long
#define xx first
#define yy second
using namespace std;

const int N = 110000;
int a[N];
map<LL, LL> mp;
map<LL, LL>::iterator it;

int main ()
{
    freopen("C-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T, cas = 1;
    cin >> T;
    while (T--) {
        LL n, m, resl, resr;
        cin >> n >> m;
        mp.clear();
        mp[n]++;
        while (m > 0) {
            it = mp.end();
            it--;
            m -= (*it).yy;
            LL num = (*it).xx;
            resl = num / 2;
            resr = (num - 1) / 2;
            mp[resl] += it->yy;
            mp[resr] += it->yy;
            mp.erase(it);
        }
        printf ("Case #%d: %lld %lld\n", cas++, resl, resr);
    }
}
