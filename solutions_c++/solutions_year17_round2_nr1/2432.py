#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;




int main() {
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {
        int d, n;
        cin>>d>>n;

        pair<int,int> h[1111];
        for(int i=0;i<n;i++)
        {
            cin>>h[i].first>>h[i].second;
        }

        sort(h, h+n);
        double max_h=-1;
        for(int i=0;i<n;i++)
        {
            int left = d - h[i].first;
            double hour = (double)left / h[i].second;
            max_h = max(max_h, hour);
        }

        double ans = (double)d / max_h;

        printf("Case #%d: %lf\n", tt, ans);
    }

    return 0;
}