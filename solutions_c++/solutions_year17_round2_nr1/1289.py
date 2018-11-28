#include <bits/stdc++.h>
using namespace std;

int t;
long double k[2000], s[2000];

int main()
{
    //freopen("A-large.in", "r", stdin);
    //freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> t;
    for(int q = 0; q < t; ++q)
    {
        long double d;
        int n;
        cin >> d >> n;
        long double otv = 0.;
        for(int i = 0; i < n; ++i)
        {
            cin >> k[i] >> s[i];
            otv = max(otv, (d - k[i])/s[i]);
            //cout << fixed << setprecision(7) << (d - k[i])/s[i] << '\n';
        }
        cout << "Case #" << q+1 << ": ";
        cout << fixed << setprecision(7) << d/otv << "\n";
    }
}
