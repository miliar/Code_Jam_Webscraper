#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define fi first
#define se second
#define ii pair<int,int>
#define vii vector<pair<int,int> >
#define vi vector<int>

int n , m , dp[30][30] ;
char s[30][30] , ans[30][30] ;

void sol(int xf,int xl , int yf , int yl){
	if( ( dp[xl+1][yl+1] - dp[xl+1][yf] - dp[xf][yl+1] + dp[xf][yf] ) == 1 ){
		char tmp ;
		for(int i=xf ; i<=xl ; i++){
			for(int j=yf ; j<=yl ; j++){
				if(s[i][j] <= 'Z' && s[i][j] >= 'A') tmp = s[i][j] ;
			}
		}
		for(int i=xf ; i<=xl ; i++){
			for(int j=yf ; j<=yl ; j++){
				ans[i][j] = tmp ;
			}
		}
		return ;
	}
	//printf("%d %d %d %d\n",xf,xl,yf,yl) ;
	int xmid = -1 , ymid = -1 ;
	for(int i=xf+1 ; i<=xl ; i++){
		if( ( dp[i][yl+1] - dp[i][yf] - dp[xf][yl+1] + dp[xf][yf] )>0 && ( dp[xl+1][yl+1] - dp[xl+1][yf] - dp[i][yl+1] + dp[i][yf] )>0 ) xmid = i ;
	}
	for(int i=yf+1 ; i<=yl ; i++){
		if( ( dp[xl+1][yl+1] - dp[xl+1][i] - dp[xf][yl+1] + dp[xf][i] )>0 && ( dp[xl+1][i] - dp[xl+1][yf] - dp[xf][i] + dp[xf][yf] )>0 ) ymid = i ;
	}
	//printf("%d %d\n",xmid , ymid) ;
	if(xmid != -1){
		sol( xf , xmid-1, yf ,yl) ; sol( xmid , xl , yf , yl) ;
	}
	else{
		sol( xf , xl , yf ,ymid-1) ; sol( xf , xl , ymid , yl) ;
	}
}

int main(){
    freopen("A_large.in","r",stdin);
    freopen("A_large.out","w",stdout);
	int t;
	scanf("%d",&t) ;
	for(int T=1;T<=t;T++){
		scanf("%d%d",&n,&m) ;
		for(int i=0;i<n;i++) scanf("%s",s[i]) ;
		memset(dp , 0 , sizeof dp) ;
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] - dp[i][j] + ( ( s[i][j] <= 'Z' && s[i][j] >= 'A' ) ? 1 : 0 );
//				printf("%d ",dp[i+1][j+1]);
			}
//			printf("\n");
		}
		sol(0,n-1 , 0, m-1) ;
		printf("Case #%d:\n" , T );
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++) printf("%c", ans[i][j]) ;
			printf("\n");
		}
	}
	return 0;
}
