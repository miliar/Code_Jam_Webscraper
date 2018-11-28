#include<bits/stdc++.h>
#define PI 3.141592653589793
using namespace std;

int h[1005], r[1005];
vector<pair<int, long double> > god;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t, n, k;
    long double ans, tans;
    scanf("%d", &t);
    for(int qu = 1; qu <= t; qu++)
    {
        ans = tans = 0.0;
        god.clear();
        scanf("%d %d", &n, &k);
        for(int i = 0; i < n; i++)
        {
            scanf("%d %d", &r[i], &h[i]);
            god.push_back(make_pair(r[i], (long double)PI * 2.0000000 * r[i] * h[i]));
            //cout<<god[i].first<<" "<<god[i].second<<endl;
        }
        sort(god.begin(), god.end());
        reverse(god.begin(), god.end());
        for(int i = 0; i <= n - k; i++)
        {
            int r = god[i].first;
            tans = (long double)PI * r * r;
            //cout<<god[i].first<<" "<<god[i].second<<endl;
            tans += god[i].second;
            vector<long double> temp;
            for(int j = i + 1; j < n; j++)
            {
                temp.push_back(god[j].second);
            }
            sort(temp.begin(), temp.end());
            reverse(temp.begin(), temp.end());
            for(int j = 0; j < k - 1; j++)
            {
                tans += temp[j];
            }
            ans = max(ans, tans);
        }
        printf("Case #%d: %.15Lf\n", qu, ans);
    }
    return 0;
}
