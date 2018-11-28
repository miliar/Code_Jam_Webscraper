#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <ctime>
#include <vector>
#include <queue>
#include <bitset>
#include <cmath>
#include <time.h>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <stdlib.h>
#include <deque>
#include <iomanip>
#include <complex>

using namespace std;

typedef long long ll;
typedef long double ld;

#define TIME (clock() * 1.0 / CLOCKS_PER_SEC)
#define rand_int ((rand() << 15) | rand())

const ld pi = 3.1415926535897932384626433832795;
const ld eps = 1e-8;
const ll prime = 239;
const ll MOD = 1e9 + 7;
const ll INF = 1e18;
const int BIG = 1e9 + 239;
const int MAX_N = 1e5 + 1;
const int MAX_T = (1 << 18);
const int MAX_LOG = 19;
const int dx[4] = {0, -1, 0, 1};
const int dy[4] = {-1, 0, 1, 0};

void solve()
{
    vector<pair<ll, ll> > v;
    ll n, k;
    cin >> n >> k;
    v = {{n, 1}};
    while (k > 0)
    {
        map<ll, ll> kol;
        for (int i = 0; i < v.size(); i++)
        {
            if (k <= v[i].second)
            {
                ll l = v[i].first;
                cout << l - ((l - 1) / 2) - 1 << " " << (l - 1) / 2;
                return;
            }
            ll l = v[i].first;
            k -= v[i].second;
            kol[l - ((l - 1) / 2) - 1] += v[i].second;
            kol[(l - 1) / 2] += v[i].second;
        }
        vector<pair<ll, ll> > t;
        for (pair<ll, ll> x : kol)
            t.push_back(x);
        sort(t.rbegin(), t.rend());
        v = t;
    }
}

int main()
{
    //freopen("C-large.in", "r", stdin);
    //freopen("small_input.txt", "r", stdin);
    //freopen("small_output.txt", "w", stdout);
    cin.sync_with_stdio(0);
    int number_of_tests;
    cin >> number_of_tests;
    for (int z = 0; z < number_of_tests; z++)
    {
        cout << "Case #" << z + 1 << ": ";
        solve();
        cout << "\n";
    }
    return 0;
}
