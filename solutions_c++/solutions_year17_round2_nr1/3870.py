#include <bits/stdc++.h>
using namespace std;

int main ()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int cs; cin>>cs;
    for(int t=1; t<=cs; t++) {
        double D; int n; vector<double> v;
        cin>>D>>n;
        for(int i=0; i<n; i++) {
            double speed, dis;
            cin>>dis>>speed;
            v.push_back((D-dis)/speed);
        }
        sort(v.begin(), v.end());
        printf("Case #%d: %0.6f\n", t, D/v.back());
    }
    return 0;
}
