#include<bits/stdc++.h>
#define r first
#define h second
using namespace std;

const double pi = atan(1.0)*4.0;

double dp1[1001][1001], dp2[1001][1001];

int main(){
    freopen("a_large.txt", "r", stdin);
    freopen("a_large_out.txt", "w", stdout);
    int T;
    cin>>T;
    for(int t=1 ; t<=T ; ++t){
        for(int i=0 ; i<1001 ; ++i){
            for(int j=0 ; j<1001 ; ++j){
                dp1[i][j] = 0;
                dp2[i][j] = 0;
            }
        }
        int n, k;
        cin>>n>>k;
        vector<pair<double, double> > arr(n);
        pair<double, double> temp;
        double a, b;
        for(int i=0 ; i<n ; ++i){
            cin>>a>>b;
            arr[i] = {a, b};
        }
        sort(arr.rbegin(), arr.rend());
        for(int i=1 ; i<=n ; ++i){
            dp1[1][i] = pi*arr[i-1].r*arr[i-1].r + 2.0*pi*arr[i-1].r*arr[i-1].h;
            dp2[1][i] = max(dp1[1][i], dp2[1][i-1]);
        }
        for(int i=2 ; i<=k ; ++i){
            for(int j=i ; j<=n ; ++j){
                dp1[i][j] = dp2[i-1][j-1] + 2.0*pi*arr[j-1].r*arr[j-1].h;
                dp2[i][j] = max(dp1[i][j], dp2[i][j-1]);
            }
        }
        double ans = 0;
        for(int i=1 ; i<=n ; ++i){
            ans = max(ans, dp1[k][i]);
        }
        cout<<"Case #"<<t<<": "<<fixed<<setprecision(9)<<ans<<endl;
    }

}
