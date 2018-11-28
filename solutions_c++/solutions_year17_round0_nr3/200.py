//#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
#define fst first
#define snd second
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vll;
typedef vector<char> vc;
typedef pair<int, int> pii;
typedef vector<pii> vii;
#define sz(c) (int)(c).size()
#define all(c) (c).begin(), (c).end()

pair<ll, ll> work (ll n, ll k)
{
    map<ll, ll> cnt;
    cnt[n] = 1;

    while (k > 0)
    {
        ll curmax = cnt.rbegin() -> fst;
        ll curcnt = cnt.rbegin() -> snd;
        assert(curmax >= 1LL);
        if (curcnt >= k)
            return mp(curmax / 2LL, (curmax - 1LL) / 2LL);

        map<ll, ll> ncnt = cnt;
        k -= curcnt;
        ncnt.erase(curmax);
        ncnt[(curmax) / 2LL] += curcnt;
        ncnt[(curmax - 1LL) / 2LL] += curcnt;
        cnt = ncnt;
    }

    assert(false);
    return mp(-1LL, -1LL);
}

pair<ll, ll> brut (int n, int k)
{
    vc used(n + 2);
    used[0] = used[n + 1] = 1;
    const int inf = (int)1e9;

    int minlr = inf, maxlr = inf;
    forn (i, k)
    {
        minlr = maxlr = -1;
        int where = -1;
        forn (j, sz(used)) if (!used[j])
        {
            int l = inf, r = inf;
            forn (v, sz(used)) if (used[v])
            {
                if (v < j)
                    l = min(l, j - v - 1);
                if (v > j)
                    r = min(r, v - j - 1);
            }

            assert(l != inf && r != inf);
            int curminlr = min(l, r);
            int curmaxlr = max(l, r);
            if (curminlr > minlr || (curminlr == minlr && curmaxlr > maxlr))
                where = j, minlr = curminlr, maxlr = curmaxlr;
        }

        assert(where != -1);
        used[where] = 1;
    }

    return mp((ll)maxlr, (ll)minlr);
}

void solve (ll n, int test)
{
    ll k;
    cin >> k;
    pair<ll, ll> pt = work(n, k);
    cout << "Case #" << test << ": " << pt.fst << ' ' << pt.snd << endl;
}

void print (string s, pair<ll, ll> x)
{
    cerr << s << " (" << x.fst << "," << x.snd << ")" << endl;
}

int main ()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "w", stdout);
    #endif // ONLINE_JUDGE

    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    ll n;
    int test = 1;
    while (cin >> n)
        solve(n, test), test++;
}
