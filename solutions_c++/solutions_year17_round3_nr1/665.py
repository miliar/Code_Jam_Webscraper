#include<bits/stdc++.h>
using namespace std;

#define INF 
#define MAX 1005

int n,m;
struct node {
	int r,h;
}a[MAX];

bool compare(node a,node b) {
	return a.r>b.r;
}

double dp[MAX][MAX];

double compute(int i,int j) {
	
	if(j == 0)
		return 0.0;
	
	if(i>=n)
		return DBL_MIN;
	
	if(dp[i][j]!=-1.0)
		return dp[i][j];
	
	return dp[i][j] = max(0.0 + compute(i+1,j), 0.0 + (2.0*acos(-1.0)*a[i].r*a[i].h) + compute(i+1,j-1));
}

int main() {
	
	freopen("input.in","r",stdin);
	//freopen("output.txt","w",stdout);
	
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);
	
	int t;
	cin>>t;
	
	for(int tst=1;tst<=t;tst++) {
		
		cin>>n>>m;
		
		for(int i = 0;i<n;i++) {
			cin>>a[i].r>>a[i].h;
		}
		
		sort(a,a+n,compare);
		
		for(int i = 0;i<=n;i++)
			for(int j = 0;j<=m;j++)
				dp[i][j] = -1.0;
		
		
		double result = DBL_MIN;
		
		for(int i = 0;i<n;i++) {
			result = max(result, 0.0 + (1.0*acos(-1.0)*a[i].r*a[i].r)+ (2.0*acos(-1.0)*a[i].r*a[i].h) + compute(i+1,m-1));
		}
		
		cout.precision(10);
		cout<<"Case #"<<tst<<": "<<fixed<<result<<endl;
		
	}
	
	
	return 0;
}
