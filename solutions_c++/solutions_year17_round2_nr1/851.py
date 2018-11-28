#include <bits/stdc++.h>
#define DEBUG(x) cout << #x << " = " << x << endl
#define pb push_back
using namespace std;
typedef long long ll;


const int MAXN = 100005;

void cans(int test, double ans)
{
    cout << "Case #" << test << ": " << ans << endl;
}


int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    cout << setprecision(10) << fixed;

    int t; cin >> t;
    for (int tt = 1; tt <= t; tt++)
    {
        int n;
        double d;
        cin >> d >> n;
        double tim = 0;
        for (int i = 0; i < n; i++)
        {
            double k, s;
            cin >> k >> s;
            tim = max(tim, (d - k) / s);
        }

        cans(tt, d / tim);
    }

    return 0;
}

