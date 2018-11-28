#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define fi first
#define se second
#define ii pair<int,int>
#define vii vector<pair<int,int> >
#define vi vector<int>

int n , k ;
char s[25] ;

int main(){
    freopen("B_large.in","r",stdin);
    freopen("B_large.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int T = 1 ; T<=t;T++){
		k = -1 ;
		int ans = -1 ;
		scanf("%s",s) ;
		n = strlen(s) ;
		for(int i=0 ; i<n ; i++) s[i] -= '0' ;
		for(int i=1;i<n;i++){
			if(s[i] < s[i-1]){
				k = i ;
				break ;
			}
		}
		printf("Case #%d: ",T);
	//	printf("::%d::",k) ;
		if(k == -1){
			for(int i=0;i<n;i++) printf("%d",s[i]) ;
			printf("\n") ;
			continue ;
		}
		for( int i = k - 1 ; i > 0 ; i-- ){
			if( (s[i]-1) >= s[i-1] ){
				ans = i ;
				s[i]-- ;
				break ;
			}
		}
		if(ans == -1){
			if(s[0] - 1 > 0 ) printf("%d",s[0]-1) ;
			for(int i=1;i<n;i++) printf("9") ;
			printf("\n") ;
			continue ;
		}
		for(int i=0;i<=ans ; i++) printf("%d" , s[i] );
		for(int i=ans + 1; i<n;i++) printf("9") ;
		printf("\n");
	}
	return 0;
}
