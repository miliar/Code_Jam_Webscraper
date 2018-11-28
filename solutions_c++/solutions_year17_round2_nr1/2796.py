#include <bits/stdc++.h>

using namespace std;

int t, n, d;
double pos[10010], v[10010];

bool check(long double ans){
    for(int i = 1; i <= n; ++i){
        if(v[i] < ans){
            long double t1 = ((double)(d - pos[i])) / v[i];

            long double t2 = ((double)d) / ans;
            //cout<<t1<<" "<<t2<<" "<<ans<<" "<<i<<endl;
            if(t1 > t2)
                return false;
        }
    }
    return true;
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    cin>>t;
    for(int c = 1; c <= t; ++c){
        cin>>d>>n;

        for(int i = 1; i <= n; ++i)
            cin>>pos[i]>>v[i];

        long double l = 0, r = 1000000000;
        r = r * r;
        long double ans;
        ans = -1;
        for(int j = 1; j <= 1000; ++j){
            long double mid = (l + r) / 2.0;
            if(check(mid) == true){
                ans = mid, l = mid;
            } else
                r = mid;
        }
        cout.precision(9);
        cout<<fixed<<"Case #"<<c<<": "<<ans<<endl;
    }

    return 0;
}
