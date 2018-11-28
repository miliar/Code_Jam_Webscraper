#include <bits/stdc++.h>
using namespace std;
#define maxn 1440

int tc;
int n,m;
bool C[maxn+5];
bool J[maxn+5];	
int dp[maxn+5][725][2][2];

int rek( int p, int k, int b, int fir){
	if ( p == maxn ){
		if ( k > 0 ) return 1e9;
		if ( b == fir ) return -1;
		return 0;
	}
	
	int &res = dp[p][k][b][fir];
	if ( res != -1 ) return res;
	res = 1e9;
	
	if ( !C[p] && k > 0 ) {
		if ( b == 0 ) res = min(res, rek(p+1,k-1,0,fir) );
		else res = min(res, rek(p+1,k-1,0,fir) + 1 );
	}
	
	if ( !J[p] ){
		if ( b == 1 ) res = min(res, rek(p+1,k,1,fir) );
		else res = min(res, rek(p+1,k,1,fir) + 1 );
	}
	
	return res;
}

int main(){
	
	freopen("out.txt","w",stdout);
	scanf("%d",&tc);
	for ( int t = 1; t <= tc; t++ ){
		memset(C,0,sizeof(C));
		memset(J,0,sizeof(J));
		memset(dp,-1,sizeof(dp));
		scanf("%d%d",&n,&m);
		
		for ( int i = 0; i < n; i++ ){
			int x,y; scanf("%d%d",&x,&y);
			for ( int j = x; j < y; j++ ) C[j] = 1;
		}
		
		for ( int i = 0; i < m; i++ ){
			int x,y; scanf("%d%d",&x,&y);
			for ( int j = x; j < y; j++ ) J[j] = 1;
		}
		
		int res = 1e9;
		if ( !C[0] ) res = min(res, rek(1,720-1,0,0) + 1);
		if ( !J[0] ) res = min(res, rek(1,720,1,1) + 1);
		
		printf("Case #%d: %d\n",t,res);
	}
	
	fclose(stdout);
	return  0;
}
