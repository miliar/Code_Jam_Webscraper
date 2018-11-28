#include<bits/stdc++.h>

using namespace std;

char a[1009];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for( int t = 1 ; t <= T ; t++ ){
		int K;
		scanf("%s",a);
		scanf("%d",&K);
		int n = strlen(a),ans = 0 ; 
		for( int i = 0 ; i < n ; i++ ){
			if( a[i] == '-' )
			{
				if( i + K <= n  ){
					for( int j = i ; j < i + K ; j++ ){
						if( a[j] == '-' ) {
							a[j] = '+';
						}
						else 
							a[j] = '-'; 
					}
					ans++;
				}
				else {
					ans = -1;
					break;
				}
			}
			//printf("%s\n",a);
		}
		printf("Case #%d: ",t);
		if( ans == -1 ){
			printf("IMPOSSIBLE\n");
		}
		else 
			printf("%d\n",ans);
	}
}