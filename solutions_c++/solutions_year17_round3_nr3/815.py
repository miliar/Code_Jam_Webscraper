#include<bits/stdc++.h>
#define ll long long
#define M 1000000007
using namespace std;

void solve(int t) {

    int n, k;
    cin>>n>>k;

    double u;
    cin>>u;

    vector<double>p(n, 0);
    for(int i=0; i<n; i++) {
        cin>>p[i];
    }

    sort(p.begin(), p.end());

    while(u > 1e-9) {
        int i=0;
        double val = p[i];
        while(i<n && abs(p[i]-val)<1e-9) i++;
        if(i>=n) {
            for(int j=0; j<n; j++) {
                p[j] += u*1.0/n;
            }
            u = 0;
        } else {
            for(int j=0; j<i; j++) {
                
                if(u < (p[i]-val)*n) {
                    p[j] += u/n;
                    u -= u/n;
                } else {
                    p[j] += min(p[i]-val, u);
                    u -= min(p[i]-val, u);
                }
            }
        }
        sort(p.begin(), p.end());
    }


    double ans = 1.0;
    for(int i=0; i<n; i++) {
        ans = ans*p[i];
    }

    cout<<"Case #"<<t<<": ";
    printf("%.10f\n", ans);


}


int main() {

    freopen("C-small-1-attempt1.in", "r", stdin); freopen("output.txt", "w", stdout);

    int tc = 1;
    cin>>tc;
    
    for(int t=1; t<=tc; t++) {
        solve(t);
    }

}