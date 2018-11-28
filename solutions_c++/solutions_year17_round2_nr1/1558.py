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

void solve (int d, int test)
{
    int n;
    cin >> n;
    vi k(n), s(n);
    forn (i, n)
        cin >> k[i] >> s[i];

    typedef long double T;
    T ans = (T)1e18;
    forn (i, n)
    {
        T tm = (T)(d - k[i]) / (T)s[i];
        ans = min(ans, (T)d / (T)tm);
    }
    printf("Case #%d: %.15f\n", test, (double)ans);
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
