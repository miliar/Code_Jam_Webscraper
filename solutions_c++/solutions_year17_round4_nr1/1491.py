#include<iostream>
#include<algorithm>
#include<cmath>
#include<bits/stdc++.h>
using namespace std;
int n, m, t, k, p, i, j, T, ans, a[5], dp[201][201][201];
main(){
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	cin>>t;
	for(int T=1;T<=t;T++){
		cin>>n>>p;
		ans=0;
		memset(a,0,sizeof(a));
		for(int i=1;i<=n;i++){
			int x;
			cin>>x;
			if(x%p==0)ans++;
			else a[x%p]++;
		}
		
		memset(dp,0,sizeof(dp));
		dp[0][0][0]=ans;
		for(int i=0;i<=a[1];i++){
			for(int j=0;j<=a[2];j++){
				for(int k=0;k<=a[3];k++){
					
					int nash=(i+2*j+3*k)%p;
					dp[i+1][j][k]=max(dp[i+1][j][k],dp[i][j][k]+(nash==0));
					
					dp[i][j+1][k]=max(dp[i][j+1][k],dp[i][j][k]+(nash==0));
					
					dp[i][j][k+1]=max(dp[i][j][k+1],dp[i][j][k]+(nash==0));
				}
			}
		}
		cout<<"Case #"<<T<<": "<<dp[a[1]][a[2]][a[3]]<<endl;
	}
}
