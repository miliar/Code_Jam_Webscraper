#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;

int dp[1000001][2];
vector<int> arr;

void dfs(int n){
    if(n>0){
        arr.push_back(dp[n][0]);
        arr.push_back(dp[n][1]);
        dfs(dp[n][0]);
        dfs(dp[n][1]);
    }
}

int main(void){
    int t;scanf("%d",&t);
    for(int i=1;i<=1000000;i++){
        if(i%2==1){
            dp[i][0]=i/2;
            dp[i][1]=i/2;
        }
        else{
            dp[i][0]=dp[i-1][0];
            dp[i][1]=dp[i-1][1]+1;
        }
    }
    for(int T=1;T<=t;T++){
        int n,k;
        scanf("%d %d",&n,&k);
        arr.clear();
        arr.push_back(n);
        dfs(n);
        sort(arr.begin(),arr.end());
        printf("Case #%d: %d %d\n",T,dp[arr[arr.size()-k]][1],dp[arr[arr.size()-k]][0]);
    }
    return 0;
}
