#include <bits/stdc++.h>
using namespace std;

char f[1005];
int k;
int tc,n;

int main(){
	freopen("out.txt","w",stdout);
	scanf("%d",&tc);
	for ( int t =1; t <= tc; t++){
		scanf("%s%d",&f,&k);
		int res = 0;
		n = strlen(f);
		for (int i = 0; i < n-k+1; i++ ){
			if ( f[i] == '-' ){
				res++;
				for ( int j = i; j < i+k; j++){
					if ( f[j] == '-' ) f[j] = '+';
					else f[j] = '-';
				}
			}
		}
		
		for ( int i = 0; i < n; i++ ) {
			if ( f[i] == '-' ) res = -1;
		}
		
		if ( res == -1 ) printf("Case #%d: IMPOSSIBLE\n",t);
		else printf("Case #%d: %d\n",t,res);
	}
	fclose(stdout);
	return 0;
}
