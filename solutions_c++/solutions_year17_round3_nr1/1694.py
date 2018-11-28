#include <bits/stdc++.h>

using namespace std;
#define pi 3.14159265359
int k;

int main()
{
    int t; cin >> t;
    for(int tc = 1; tc <= t; tc++)
    {
        int n; cin >> n;
        int k; cin >> k;
        vector<pair<double, double> >pks(n);


        for(int i = 0; i < n;i++)
        {
            cin >> pks[i].second >> pks[i].first;
            pks[i].first = 2.0 *pi * pks[i].first * pks[i].second;
        }
        double best = 0;
        sort(pks.begin(), pks.end());
        for(int i = 0; i < n; i++)
        {
            double cur = 0;
            cur += pks[i].first + pks[i].second * pks[i].second * pi;
            int got = 0;
            for(int j = n-1; j >= 0; j--)
            {
                if(got == k-1) break;

                if(j == i) continue;
                if(pks[i].second < pks[j].second) continue;
                got++;
                cur += pks[j].first;
            }
            if(got == k-1)
            {
                best =max(best, cur);
            }

        }
        printf("Case #%d: %.10f\n", tc, best);
    }
    return 0;
}

