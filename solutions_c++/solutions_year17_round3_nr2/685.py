#include <bits/stdc++.h>
using namespace std;
 
int dp[1441][721][3];
int arr[1441];int first;int solve(int tm, int ac, int prev);
int main(){	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,tt=0; cin>>t;	while(t--){		tt++;		int a,b; cin>>a>>b;		memset(dp,-1,sizeof(dp));		memset(arr,0,sizeof(arr));
		int x,y;
		for(int i=0;i<a;i++){
			cin>>x>>y;		for(int j=x;j<y;j++) arr[j] =1;
		} 		for(int i=0;i<b;i++){
			cin>>x>>y;			for(int j=x;j<y;j++) arr[j] =2;
		}
			cout<<"Case #"<<tt<<": ";
			first = 1;			int q1 = solve(0,0,1);
			memset(dp,-1,sizeof(dp));
			first = 2;			int q2 = solve(0,0,2);
			cout<<min(q1,q2)<<endl;

	}
return 0;

}
int solve(int tm, int ac, int prev){
	int bc = tm - ac;	if(tm == 1440 and ac == 720) return (first == prev)?0:1;
	if(ac > 720 or bc > 720) return 50001;
	if(dp[tm][ac][prev] != -1) return dp[tm][ac][prev];
	
	if(arr[tm] == 1){		if(prev == 1) return dp[tm][ac][prev] = solve(tm+1,ac+1,1);
		else return dp[tm][ac][prev] = 1 + solve(tm+1,ac+1,1);
	}	if(arr[tm] == 2){		if(prev == 2) return dp[tm][ac][prev] = solve(tm+1,ac,2);
		else return dp[tm][ac][prev] = 1 + solve(tm+1,ac,2);
	}
	if(arr[tm] == 0){
		// cout<<prev<<endl;
		if(prev == 1){
			return dp[tm][ac][prev] = min(solve(tm+1,ac+1,1), 1+solve(tm+1,ac,2));
		}
		else{
			return dp[tm][ac][prev] = min(solve(tm+1,ac,2), 1+solve(tm+1,ac+1,1));
		}
	}
}
