#include<bits/stdc++.h>
using namespace std;
#define mult 1e7
#define ll unsigned long long
#define pi 3.14159265359
pair<double, double>cake[1005];
double dp[1005][1005];
int main(){
    freopen("A-large.in", "r", stdin);
    freopen("out1.txt", "w", stdout);
    int t;
    cin>>t;
    for(int k=1; k<=t; k++){
        memset(dp, 0, sizeof dp);
        for(int i=0; i<=1000; i++)
            cake[i].first=cake[i].second=0;
        int n, K;
        ll x, y;
        cin>>n>>K;
        for(int i=1; i<=n; i++){
            cin>>x>>y;
            cake[i].first=x;
            cake[i].second=y;
        }
        sort(cake+1, cake+n+1);
        reverse(cake+1, cake+n+1);



        for(int i=1; i<=n; i++){
            double temp1 = (double)2.0*(double)((double)pi)*(double)cake[i].first*(double)cake[i].second;
            double temp = ((double)pi)*(double)cake[i].first*(double)cake[i].first;
            //cout<<temp1+temp<<endl;
            //if(i==1){
                //cout<<"a";
                dp[i][1] = max(dp[i-1][1], temp1+temp);
                //cout<<dp[2][1]<<endl;
            //}

            for(int j=2; j<=K; j++){

                if(j<=i){
                    //cout<<"a";
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + temp1);
                }
                //cout<<dp[2][1]<<" ";
            }
            //cout<<endl;
        }
        double ans = dp[n][K];
        //ans = (double)((double)ans/(double)mult);
        printf("Case #%d: %.9lf\n", k, ans);
    }
    return 0;
}
