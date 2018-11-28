#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("controlLarge.txt","w",stdout);
    int t;
    cin >> t;
    for(int I = 1 ; I <=t ; I++){
        int d,n;
        cin >> d >> n;
        vector<pair<int,int>> v;
        for(int i = 0 ; i < n ; i ++){
            int x,y;
            cin >> x >> y;
            if(x >= d)continue;
            v.push_back({x,y});
        }

        double lo = 0 , hi = 1e18;
        for(int j = 0 ; j < 100000 ; j++){
            double mid = lo + (hi-lo)/2;
            bool isTrue = true;
            for(int i = 0 ; i < n ; i++){
                if(v[i].second > mid)continue;
                double t1 =  mid/d;
                double t2 = 1.0 * v[i].second / (d-v[i].first);
                if(t1 > t2 )isTrue = false;
            }
            if(isTrue)lo = mid;
            else hi = mid;
        }
        printf("Case #%d: %.6lf\n",I,lo);
    }
    return 0;
}
