#include <bits/stdc++.h>
using namespace std;

int dp[105][105][105][5];
int tc,n,p;
int f[5];

int rek( int a, int b, int c, int sisa){
	
	int &res = dp[a][b][c][sisa];
	if ( res != -1 ) return res;
	res = 0;
	
	if ( sisa == 0 ){
		if ( a > 0 ) res = max(res, rek(a-1,b,c,p-1) + 1);
		if ( b > 0 ) res = max(res, rek(a,b-1,c,p-2) + 1);
		if ( c > 0 ) res = max(res, rek(a,b,c-1,p-3) + 1);
	} else {
		if ( a > 0 ){
			res = max(res, rek(a-1,b,c,(sisa+p-1)%p) );
		}
		if ( b > 0 ){
			res = max(res, rek(a,b-1,c,(sisa+p-2)%p) );
		}
		if ( c > 0 ){
			res = max(res, rek(a,b,c-1,(sisa+p-3)%p) );
		}
	}
	
	return res;
}

int main(){
	
	freopen("out.txt","w",stdout);
	scanf("%d",&tc);
	for ( int t = 1; t <= tc; t++){
		scanf("%d%d",&n,&p);
		memset(f,0,sizeof(f));
		
		int res = 0;
		for ( int i = 0; i < n; i++ ){
			int x; scanf("%d",&x);
			int y = x % p;
			if ( y == 0 ) res++;
			else f[y]++;
		}
		
		for ( int i = 0; i <= f[1]; i++ )
			for ( int j = 0; j <= f[2]; j++ )
				for( int k = 0; k <= f[3]; k++ )
					for ( int l = 0; l <= p; l++ )
						dp[i][j][k][l] = -1;
		printf("Case #%d: %d\n",t,rek(f[1],f[2],f[3],0) + res);
	}	
		
	fclose(stdout);
	return 0;
}
