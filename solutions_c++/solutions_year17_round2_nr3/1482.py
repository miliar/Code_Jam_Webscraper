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

template <class T>
void remin (T &a, T b)
{
    a = min(a, b);
}

void solve (int n, int test)
{
    int q;
    cin >> q;

    vi e(n), speed(n);
    forn (i, n)
        cin >> e[i] >> speed[i];

    const ll llinf = (ll)1e18;
    vector<vll> d(n, vll(n, llinf));
    forn (i, n) forn (j, n)
    {
        cin >> d[i][j];
        if (d[i][j] == -1)
            d[i][j] = llinf;
        if (i == j)
            d[i][j] = 0;
    }
    forn (i, n) forn (j, n) forn (k, n)
        d[i][j] = min(d[i][j], d[i][k] + d[k][j]);

    typedef double T;
    const T inf = 1e40;

    vi u(q), v(q);
    forn (i, q)
    {
        cin >> u[i] >> v[i];
        --u[i], --v[i];
    }

    vector<vector<T>> need(n, vector<T>(n, inf));
    forn (s, n) if (count(all(u), s))
    {
//        cerr << s << endl;
//        cerr << (double)clock() / CLOCKS_PER_SEC << endl;

        vector<vector<T>> mtime(n, vector<T>(n, inf));
        mtime[s][s] = 0;
        vector<vc> used(n, vc(n));

//        set<pair<T, pii>> bytime;
//        forn (i, n) forn (j, n)
//            bytime.insert(mp(mtime[i][j], mp(i, j)));

        forn (iter, n * n)
        {
            int who = -1, horse = -1;
            T best = inf;
            forn (i, n) forn (j, n)
            if (!used[i][j] && mtime[i][j] < best)
                best = mtime[i][j], who = i, horse = j;
//            best = bytime.begin() -> fst;
//            who = bytime.begin() -> snd .fst;
//            horse = bytime.begin() -> snd .snd;
//            bytime.erase(bytime.begin());
//            if (best == inf)
//                break;
            if (who == -1)
                break;

            ll rem = (ll)e[horse] - d[horse][who];
            used[who][horse] = 1;
            {
//                bytime.erase(mp(mtime[who][who], mp(who, who)));
                remin(mtime[who][who], mtime[who][horse]);
//                bytime.insert(mp(mtime[who][who], mp(who, who)));
            }
            forn (to, n) if (d[who][to] <= rem)
            {
//                bytime.erase(mp(mtime[to][horse], mp(to, horse)));
                remin(mtime[to][horse], mtime[who][horse] +
                      d[who][to] / (T)speed[horse]);
//                bytime.insert(mp(mtime[to][horse], mp(to, horse)));
            }
        }

        forn (to, n) forn (horse, n)
            remin(need[s][to], mtime[to][horse]);
    }

    printf("Case #%d:", test);
    forn (i, q)
    {
        T ans = need[u[i]][v[i]];
        assert(ans < 1e20);
        printf(" %.15f", (double)ans);
    }
    printf("\n");
}

int main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "w", stdout);
    #endif // ONLINE_JUDGE

    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    int n;
    int test = 1;
    while (cin >> n)
        solve(n, test), test++;
}
