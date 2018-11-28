#include <bits/stdc++.h>
using namespace std;

int main(){
	
	int test,t=0,n,k,i,j,ans,ans2;
	int c,m,seat[1002],ctr[1002];
	scanf("%d",&test);
	
	for( t=0 ; t<test ;){
		scanf("%d%d%d",&n,&c,&m);
		memset(ctr,0,sizeof(ctr));
		memset(seat,0,sizeof(seat));
		ans=0;
		for( i=0 ; i<m ; i++ ){
			scanf("%d%d",&j,&k);
			ctr[k]++;
			seat[j]++;
			if( ctr[k]> ans ) ans = ctr[k];
		}
		
		while( true ){
			ans2 = 0;
			j =0 ;
			for( i=1 ; i<=n ; i++ ){
				if( seat[i] <= ans ) j+= ans-seat[i];
				else{
					if( seat[i]-ans <= j ){
						j -= seat[i]-ans;
						ans2 += seat[i]-ans;	
					}
					else{
						goto next;	
					}
				}
			}
			break;
			next:
			ans++;
		}
		
		printf("Case #%d:",++t);	
		printf(" %d %d\n",ans,ans2);
	}
	return 0;
}

