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

string tostr (ll n)
{
    string ans;
    while (n > 0)
        ans += n % 10 + '0', n /= 10;
    reverse(all(ans));
    return ans;
}

bool isgood (int n)
{
    string ans = tostr(n);
    return is_sorted(all(ans));
}

bool isok (const string &s, int start, int digit)
{
    for (int i = start; i < sz(s); i++)
    {
        int curdig = s[i] - '0';
        if (curdig > digit)
            return true;
        if (curdig < digit)
            return false;
    }
    return true;
}

ll work (ll n)
{
    string ndigs = tostr(n);
    if (!isok(ndigs, 0, 1))
    {
        ndigs = string(sz(ndigs) - 1, '9');
        assert(!ndigs.empty());
    }

    int last = 1;
    bool was = false;

    ll ans = 0;
    forn (i, sz(ndigs))
    {
        int next = -1;
        const int cur = ndigs[i] - '0';
        forn (dig, 10) if (dig >= last)
        {
            if (!was && dig > cur)
                continue;
            if ((dig == cur && !was) && !isok(ndigs, i + 1, dig))
                continue;
            next = dig;
        }

        assert(next != -1);
        last = next;
        was |= (next < cur);
        ans *= 10LL, ans += next;
    }
    return ans;
}

int brut (int n)
{
    for (int i = n; i >= 1; i--)
    if (isgood(i))
        return i;
    assert(false);
    return -1;
}

void solve (ll n, int test)
{
    ll ans = work(n);
    cout << "Case #" << test << ": " << ans << endl;
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

    ll n;
    int test = 1;
    while (cin >> n)
        solve(n, test), test++;
}
