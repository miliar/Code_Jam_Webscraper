#include<bits/stdc++.h>
using namespace std;

#define MAX 105
int a[MAX];

int n,p;
int dp[MAX][MAX][MAX][MAX][4];


int compute(int i,int j,int k,int z,int lt) {
	
	if(i == 0 && j == 0 && k == 0)
		return 0;
	
	if(dp[i][j][k][z][lt]!=-1)
		return dp[i][j][k][z][lt];
	
	dp[i][j][k][z][lt] = 0;
	
	if(lt == 0) {
		
		if(i!=0)
			dp[i][j][k][z][lt] = max(dp[i][j][k][z][lt],compute(i-1,j,k,z,0)+1);
		
		if(j!=0)
			dp[i][j][k][z][lt] = max(dp[i][j][k][z][lt],compute(i,j-1,k,z,p-1)+1);
		
		if(k!=0)
			dp[i][j][k][z][lt] = max(dp[i][j][k][z][lt],compute(i,j,k-1,z,p-2)+1);
		
		if(z!=0)
			dp[i][j][k][z][lt] = max(dp[i][j][k][z][lt],compute(i,j,k,z-1,p-3)+1);
	}
	else {
		
		if(i!=0)
		dp[i][j][k][z][lt] = max(dp[i][j][k][z][lt],compute(i-1,j,k,z,lt));
		
		if(j!=0) {
			if(lt>=1)
					dp[i][j][k][z][lt] = max(dp[i][j][k][z][lt],compute(i,j-1,k,z,lt-1));
			else
					dp[i][j][k][z][lt] = max(dp[i][j][k][z][lt],compute(i,j-1,k,z,p-(1-lt)));
		}
		
		if(k!=0) {
			if(lt>=2)
					dp[i][j][k][z][lt] = max(dp[i][j][k][z][lt],compute(i,j,k-1,z,lt-2));
			else
					dp[i][j][k][z][lt] = max(dp[i][j][k][z][lt],compute(i,j,k-1,z,p-(2-lt)));
		}
		
		if(z!=0) {
				if(lt>=3)
					dp[i][j][k][z][lt] = max(dp[i][j][k][z][lt],compute(i,j,k,z-1,lt-3));
			else
					dp[i][j][k][z][lt] = max(dp[i][j][k][z][lt],compute(i,j,k,z-1,p-(3-lt)));	
		}
	}
	return dp[i][j][k][z][lt];
}

int main() {
	
	freopen("input.in","r",stdin);
	freopen("ouptut.txt","w",stdout);
	
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);
	
	int t;
	
	cin>>t;
	
	
	for(int tst = 1;tst<=t;tst++) {
		
		cin>>n>>p;
		
		int z = 0;
		int o = 0;
		int tw = 0;
		int th = 0;
		
		for(int i = 0;i<n;i++) {
			cin>>a[i];
			a[i] %= p;
			
			if(a[i] == 0)
				z++;
			else if(a[i]==1)
				o++;
			else if(a[i] == 2)
				tw++;
			else
				th++;
		}
		
		for(int i = 0;i<=z;i++)
			for(int j = 0;j<=o;j++)
				for(int k = 0;k<=tw;k++)
					for(int z=0;z<=th;z++)
						for(int lt = 0;lt<=3;lt++)
							dp[i][j][k][z][lt] = -1;
							
		cout<<"Case #"<<tst<<": "<<compute(z,o,tw,th,0)<<endl;
		
		
	}
	
	return 0;
}
