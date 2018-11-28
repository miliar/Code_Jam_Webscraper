#include <bits/stdc++.h>
#define ll long long
#define ss second
#define ff first
using namespace std;


vector<double> p;

double check(double mid){
    double k = 0;

    for(int i = 0; i < p.size(); ++i){

            if(p[i] < mid)k += mid - p[i];
    }
    return k;
}

int main(){
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int t;
    cin >> t;
    for(int z = 1; z <= t; ++z)
    {
        p.clear();
        int n, k;
        cin >> n >> k;
        double u;
        cin >> u;
        double y = u/n;
        for(int i = 0; i < n; ++i){
            double x;
            cin >> x;
            p.push_back(x);
        }
        double l  = 0, h = 1;
        double mid;
        for(int i = 0; i < 300; ++i)
        {
            mid = (l+h)/2;
            if(check(mid) <= u)l = mid;
            else h = mid;
        }
        double ans = 1;
        for(int i = 0; i < p.size(); ++i)
        {
            if(p[i] > h)ans *= p[i];
            else ans *= h;
        }

        printf("Case #%d: %.6lf\n", z, ans);
    }
}
