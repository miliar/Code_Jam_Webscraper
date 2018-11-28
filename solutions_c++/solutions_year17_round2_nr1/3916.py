#include <bits/stdc++.h>
#define eps 1e-9

using namespace std;

typedef long long ll;

double pos[1007], speed[1007];

vector<pair<double, double> > v;

int main ()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t, i, j, k, l;
    int cs=0;
    int n;
    double d;
    cin >> t;
    while (t--)
    {
        cs++;
        cin >> d >> n;
        for (i=0; i<n; i++)
        {
            cin >> pos[i] >> speed[i];
            v.push_back(make_pair(pos[i], speed[i]));
        }
        sort (v.begin(), v.end());
        for (i=0; i<n; i++)
        {
            pos[i]=v[i].first;
            speed[i]=v[i].second;
        }
        int idx=0;
        for (i=0; i<n-1; i++)
        {
            if (speed[i]<=speed[i+1])
            {
                idx=i;
                break;
            }
            else
            {
                double spd = speed[i]-speed[i+1];
                double time = (pos[i+1]-pos[i])/spd;
                if (pos[i+1]+time*speed[i+1]>d+eps)
                {
                    idx=i;
                    break;
                }
                else
                {
                    idx=i+1;
                }
            }
        }
        double my_time = (d-pos[idx])/speed[idx];
        double ans = d/my_time;
        printf("Case #%d: %.10f\n", cs, ans);
        v.clear();
    }







    return 0;
}
