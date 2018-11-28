#include <bits/stdc++.h>
using namespace std;
double pi=3.14159265358979323846;



int main()
{
    ios::sync_with_stdio(false);
    int t,n,k;
    int caseno=0;
    
    cin>>t;
    while(t--){
        caseno++;
        vector <pair <double,double> > dimension;
        pair <double,double> bc;
        cin>>n>>k;
        for(int i=0;i<n;i++){
            cin>>bc.first>>bc.second;
            dimension.push_back(bc);
        }
        sort(dimension.rbegin(),dimension.rend());
        double dp[1000+45][1000+45];
        double max_height=0;
        double ans=0;
        for(int i=0;i<k;i++){
            max_height=0;
            for(int j=0;j<i;j++){
                if(i!=0){
                    max_height=max(max_height,dp[i-1][j]);
                }
            }
            for(int j=i;j<n;j++){
                if(i==0){
                    dp[i][j]=(pi*dimension[j].first*dimension[j].first)+(2*pi*dimension[j].first*dimension[j].second);
                    ans=max(ans,dp[i][j]);
                    // cout<<ans<<"::\n";
                }
                else{
                    dp[i][j]=max_height+(2*pi*dimension[j].first*dimension[j].second);
                    max_height=max(dp[i-1][j],max_height);
                    ans=max(ans,dp[i][j]);
                }
            }
        }
        cout<<fixed<<setprecision(10)<<"Case #"<<caseno<<": "<<ans<<"\n";
    }
    return 0;
}
