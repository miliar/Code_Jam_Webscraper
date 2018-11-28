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

const int inf = (int)1e9;

struct edge
{
    int to;
    int cap;
};

struct flow
{
    vvi g;
    vector<edge> e;
    int n, s, t;
    vc used;

    flow (int n_) : n(n_), s(n_ - 2), t(n_ - 1)
    {
        used.assign(n, 0);
        g.resize(n);
    }

    void add_edge (int from, int to, int cap)
    {
        g[from].pb(sz(e));
        e.pb(edge{to, cap});
        g[to].pb(sz(e));
        e.pb(edge{from, 0});
    }

    bool dfs (int v)
    {
        if (v == t)
            return true;
        if (used[v])
            return false;
        used[v] = true;

        for (int en : g[v])
        {
            int to = e[en].to;
            if (e[en].cap > 0 && dfs(to))
            {
                e[en].cap--;
                e[en ^ 1].cap++;
                return true;
            }
        }

        return false;
    }

    int add_flow ()
    {
        fill(all(used), 0);
        return dfs(s);
    }

    int max_flow ()
    {
        int ans = 0;
        while (int add = add_flow())
            ans += add;
        return ans;
    }

    bool sat (int x, int y)
    {
        for (int en : g[x]) if (e[en].to == y)
            return e[en].cap == 0;
        assert(false);
        return false;
    }
};

void solve (int n, int test)
{
    vector<string> grid(n, string(n, '.'));
    int m;
    cin >> m;

    forn (i, m)
    {
        char type;
        int x, y;
        cin >> type >> x >> y;
        --x, --y;
        grid[x][y] = type;
    }

    flow flow(6 * n);
    vc banl(3 * n - 1), banr(3 * n - 1);

    int ans = 0;
    forn (i, n) forn (j, n)
    {
        if (grid[i][j] != 'x' && grid[i][j] != 'o')
            flow.add_edge(i, 3 * n - 1 + j, 1);
        else
        {
            ans += 1;
            banl[i] = 1;
            banr[j] = 1;
        }

        int dsum = (i + j), ddiff = (i - j + n - 1);
        if (grid[i][j] != '+' && grid[i][j] != 'o')
            flow.add_edge(n + dsum, 4 * n - 1 + ddiff, 1);
        else
        {
            banl[n + dsum] = 1;
            banr[n + ddiff] = 1;
            ans += 1;
        }
    }

    forn (i, 3 * n - 1)
    {
        if (!banl[i])
            flow.add_edge(flow.s, i, 1);
        if (!banr[i])
            flow.add_edge(i + 3 * n - 1, flow.t, 1);
    }

    ans += flow.max_flow();
    vector<string> ngrid(n, string(n, '.'));

    int realans = 0;
    int diff_cnt = 0;
    forn (i, n) forn (j, n)
    {
        ngrid[i][j] = grid[i][j];

        if (grid[i][j] != 'x' && grid[i][j] != 'o')
        if (flow.sat(i, 3 * n - 1 + j))
            ngrid[i][j] = (ngrid[i][j] == '+' ? 'o' : 'x');

        int dsum = (i + j), ddiff = (i - j + n - 1);
        if (grid[i][j] != '+' && grid[i][j] != 'o')
        if (flow.sat(n + dsum, 4 * n - 1 + ddiff))
            ngrid[i][j] = (ngrid[i][j] == 'x' ? 'o' : '+');

        realans += (ngrid[i][j] != '.');
        realans += (ngrid[i][j] == 'o');
        diff_cnt += (ngrid[i][j] != grid[i][j]);
    }

    assert(ans == realans);
    cout << "Case #" << test << ": " << ans << ' ' << diff_cnt << endl;
    forn (i, n) forn (j, n) if (grid[i][j] != ngrid[i][j])
        cout << ngrid[i][j] << ' ' << i + 1 << ' ' << j + 1 << '\n';
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

    int n;
    int test = 1;
    while (cin >> n)
        solve(n, test), test++;
}
