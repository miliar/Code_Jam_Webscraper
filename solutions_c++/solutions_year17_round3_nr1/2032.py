#include<bits/stdc++.h>
using namespace std;

#define l long long
#define ld long double
#define pb push_back
#define mod 1000000007
#define ii pair<l,l>
#define jj pair<ii,ii>

l k1;
l n,k;
l dp[1001][1001];
double solve(vector<ii>vec,int i,int k){
    if(dp[i][k]!=-1) return dp[i][k];
    if(k==0)    return 0;
    if(i==n)    return -mod;
    if(k==k1){
        double ans1=vec[i].first*vec[i].first+2*vec[i].first*vec[i].second+solve(vec,i+1,k-1);
        double ans2=solve(vec,i+1,k);

        return dp[i][k]=max(ans1,ans2);
    }
    else{
        double ans1=2*vec[i].first*vec[i].second+solve(vec,i+1,k-1);
        double ans2=solve(vec,i+1,k);

        return dp[i][k]=max(ans1,ans2);
    }
}

bool cmp(ii a,ii b){
    return a.first>b.first;
}

int main(){

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;cin>>t;

    for(int ix=1;ix<=t;ix++){


        memset(dp,-1,sizeof(dp));
        printf("Case #%d: ",ix);
        cin>>n>>k;
        k1=k;
        vector<ii>vec;
        for(int i=0;i<n;i++){
            l x,y;cin>>x>>y;
            vec.push_back(ii(x,y));
        }

        sort(vec.begin(),vec.end(),cmp);
        cout<<setprecision(32)<<fixed;
        cout<<M_PI*solve(vec,0,k)<<endl;
    }
}
