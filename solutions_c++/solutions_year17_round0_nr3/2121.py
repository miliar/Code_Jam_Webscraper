#include <stdio.h>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cctype>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <map>

using namespace std;

typedef long long ll;
typedef unsigned int ui;
typedef long double ld;
typedef pair<int, int> pii;

#define pb push_back
#define ft first
#define sd second
#define mpr make_pair
#define all(x) begin((x)), end((x))
#define rall(x) (x).rbegin(), (x).rend()
#define forn(i, n) for(int (i) = 0; (i) < (n); ++(i))
#define isz(x)(x).size()

/* <----------------------------------------------------------> */

map<ll, char> us;
set<ll, greater<ll> > len;
map<ll, ll> cnt;

ll n, k;

void init_len()
{
    queue<ll> q;
    q.push(n);
    us[n] = true;
    while (!q.empty())
    {
        ll v = q.front();
        q.pop();
        if (!v) break;
        len.insert(v);
        if (!us[v / 2])
        {
            us[v / 2] = true;
            q.push(v / 2);
        }
        if (!us[(v - 1) / 2])
        {
            us[(v - 1) / 2] = true;
            q.push((v - 1) / 2);
        }
    }
}

void subsolve()
{
    us.clear();
    len.clear();
    cnt.clear();

    scanf("%lld%lld", &n, &k);

    init_len();
    ++cnt[n];
    --k;

    auto it = len.begin();

    while (k && it != len.end())
    {
        ll take = min(k, cnt[*it]);
        cnt[(*it - 1) / 2] += take;
        cnt[*it / 2] += take;
        cnt[*it] -= take;
        if (!(cnt[*it])) ++it;
        k -= take;
    }

    ll ans = *it;
    printf("%lld %lld\n", ans / 2, (ans - 1) / 2);
}

void solve()
{
    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; ++i)
    {
        printf("Case #%d: ", i);
        subsolve();
    }
}

/* <----------------------------------------------------------> */

 #define LOCAL
// #define FILE_NAME ""

int main()
{
    #if defined LOCAL
        freopen("C-large.in", "r", stdin);
        freopen("output.txt", "w", stdout);
    #elif defined FILE_NAME
        freopen(FILE_NAME".in", "r", stdin);
        freopen(FILE_NAME".out", "w", stdout);
    #endif

    ios_base::sync_with_stdio(0);
    cin.tie(0);

    solve();

    return 0;
}
