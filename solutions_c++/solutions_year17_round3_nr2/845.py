#include <bits/stdc++.h>
#define DEBUG(x) cout << #x << " = " << x << endl
#define pb push_back
#define ff first
#define ss second
using namespace std;
typedef long long ll;
const int MOD = 0;
const int MAXN = 1005;
const int DAY = 60 * 24;

pair <pair <int, int> , int > a[MAXN];
set <int> sN, sM;

int solve()
{
    int n , m;
    cin >> n >> m;

    int remN = 720;
    int remM = 720;
    int ansN = n;
    int ansM = m;

    for (int i = 0; i < n; i++)
    {
        cin >> a[i].ff.ff >> a[i].ff.ss;
        a[i].ss = 0;
        remN -= a[i].ff.ss - a[i].ff.ff;
    }
    for (int i = 0; i < m; i++)
    {
        cin >> a[n+i].ff.ff >> a[n+i].ff.ss;
        a[n+i].ss = 1;
        remM -= a[n+i].ff.ss - a[n+i].ff.ff;
    }

    sort(a, a + n + m);

    sN.clear();
    sM.clear();
    for (int i = 0; i < n + m; i++)
    {
        int j = (i+1) % (n+m);
        if (a[i].ss == 0 && a[j].ss == 0)
            sN.insert((a[j].ff.ff - a[i].ff.ss + DAY) % DAY);

        if (a[i].ss == 1 && a[j].ss == 1)
            sM.insert((a[j].ff.ff - a[i].ff.ss + DAY) % DAY);
    }

    while (!sN.empty())
    {
        remN -= *(sN.begin());
        if (remN < 0)
            break;
        else
        {
            ansN--;
            sN.erase(sN.begin());
        }
    }

    while (!sM.empty())
    {
        remM -= *(sM.begin());
        if (remM < 0)
            break;
        else
        {
            ansM--;
            sM.erase(sM.begin());
        }
    }

    return 2 * max(ansN, ansM);
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t; cin >> t;
    for (int tt = 1; tt <= t; tt++)
    {
        cout << "Case #" << tt << ": " << solve() << endl;
    }

    return 0;
}


