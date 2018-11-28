/*
░░░░░░░▄▀▀▀▀▀▀▀▄▄░░░░░░
░░░░░░▐░░░▄▄▄▄▄░ ▀▀▄
░░░░░▐░$░▐▀░░░░▀▀▀▀▄▀
░░░░░▌░░▐░░░░░░░░░░▄▄
░░░░▐░░░░▀▄▄▄▄▄▄▀▀▀░▄▀
░░░░▌▒░▒░▒░▒░░░▄▄▄▀▀
░░░░▌▒▒░▒▒▒▒▄▄▀▀
░░░▐░░▒▒▒▄▀▀░░░░░░░
░░░▐░▒▒▒▐░░░░░░░░░
░░░▐▒▒▒▒▌░░░░░░░░
░░░▐▒▒▒░▐░░░░░░░░░▄▀▄
░░░▐▒▒░▒▐▄▄▀▀▀▀▄▄▄▀░▌
░░░▐░▒▒░▄▄▄▄▀▀▄▄▄▄▄▀
░░▐▒▒▄▒▒▀▄▄▄▄▄▀░░░▄▌░░
░░▌▒▐░▀▀▄▄▄▄▄▄▄▀▀▀░░░░
░▐▒▒▌░░░░░░░░░░░░░ 
*/
#include <bits/stdc++.h>
#define double long double

using namespace std;

typedef long long ll;

int main()
{
#ifdef ONPC
    freopen("lrg.in", "r", stdin);
    freopen("a.out", "w", stdout);
#else
    //freopen("a.in", "r", stdin);
    //freopen("a.out", "w", stdout);
#endif
    int t;
    cin >> t;
    for (int it = 0; it < t; it++)
    {
        int d, n;
        cin >> d >> n;
        vector <int> k(n), s(n);
        vector <double> de(n);
        vector <pair <int, int> > a;
        for (int i = 0; i < n; i++)
        {
            cin >> k[i] >> s[i];
            a.push_back({k[i], s[i]});
        }
        for (int i = 0; i < n; i++)
        {
            double res = (d - k[i]) / (double) s[i];
            for (int j = 0; j < n; j++)
            {
                if (s[i] > s[j])
                {
                    res = min(res, (k[i] - k[j]) / (double) (s[j] - s[i]));
                }
            }
            de[i] = res;
        }
        double l = 0, r = 1e18;
        int cnt = 200;
        while (cnt--)
        {
            double m = (l + r) / 2;        
            bool good = true;
            for (int i = 0; i < n; i++)
            {
                if (s[i] < m)
                {
                    good &= ((k[i] / (double) (m - s[i])) >= de[i]);
                }
            }
            if (good)
            {
                l = m;
            }
            else
            {
                r = m;
            }
        }
        cout << fixed << setprecision(20) << "Case #" << it + 1 << ": " << l << endl;
    }
}
