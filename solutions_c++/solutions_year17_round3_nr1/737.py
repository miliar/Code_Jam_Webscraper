#include <bits/stdc++.h>
using namespace std;

using ll=long long;

int cas;
const int N=1e3+5;

ll r[N], h[N];
double s[N];

const double PI=acos(-1);

int main(){
    int T;

    for(cin>>T; T--; ){
        printf("Case #%d: ", ++cas);
        int n, k;
        cin >> n >> k;
        for(int i=0; i<n; i++)
            cin >>  r[i]>>h[i];
        double res=-1;
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++)
                s[j]=2*r[j]*PI*h[j];
            double cur=PI*r[i]*r[i]+s[i];
            s[i]=-1;

            sort(s, s+n, greater<double>());

            for(int j=0; j<k-1; j++)
                cur+=s[j];

            res=max(res, cur);
        }
        printf("%.9f\n", res);
    }
    return 0;
}