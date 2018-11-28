#include<bits/stdc++.h>
using namespace std;

vector<pair<int, int> > v;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t, d, n, x, y;
    long double tim, mtim, ans;
    scanf("%d", &t);
    for(int qu = 1; qu <= t; qu++)
    {
        mtim = 0;
        v.clear();
        scanf("%d %d", &d, &n);
        for(int i = 0; i < n; i++)
        {
            scanf("%d %d", &x, &y);
            v.push_back(make_pair(x, y));
        }
        sort(v.begin(), v.end());
        reverse(v.begin(), v.end());
        for(auto it : v)
        {
            tim = ((d - it.first) / (long double)it.second);
            mtim = max(mtim, tim);
        }
        ans = d / mtim;
        printf("Case #%d: %Lf\n", qu, ans);
    }
    return 0;
}
