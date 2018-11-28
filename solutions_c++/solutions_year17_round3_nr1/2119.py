#include <iostream>
#include<bits/stdc++.h>
using namespace std;
int main()
{
    double pp = 3.14159265358979;
    ifstream in("input1.in");
    ofstream out("output1.out");
    out.precision(17);
    int t;
    in >> t;
    for(int i =0;i<t;i++){
        int n,k;
        in >> n >> k;
        pair<double,double> c[n];
        double ar[n];
        double dp[k+1][n+1];
        for(int j =0;j<n;j++){
           in >> c[j].first >> c[j].second;
        }
        sort(c,c+n);
        for(int j =0;j<n;j++){
          ar[j] = c[j].first * c[j].first  + 2*c[j].first*c[j].second;
        }

        for(int j=0;j<=k;j++){
            for(int s=0;s<=n;s++){
                 if(j==0||s==0 || s<j) dp[j][s] = 0;
                 else if(j==1) dp[j][s] = max(dp[j][s-1],ar[n-s]);
                 else {
                    dp[j][s] = max(dp[j][s-1],dp[j-1][s-1] - c[n-s].first*c[n-s].first + ar[n-s]);
                 }
            }
        }
        out << "Case #" << i+1 << ": " << dp[k][n]*pp <<endl;
    }
    return 0;
}
