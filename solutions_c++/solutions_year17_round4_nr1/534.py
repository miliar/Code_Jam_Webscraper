#include <bits/stdc++.h>
using namespace std;
int main(){
	
	int test,t=0,n,k,i,j,ans;
	int p,ctr[5];
	scanf("%d",&test);
	
	for( t=0 ; t<test ;){
		scanf("%d%d",&n,&p);
		memset(ctr,0,sizeof(ctr));
		for( i=0 ; i<n ; i++ ){
			scanf("%d",&j);
			ctr[j%p]++;
		}
		
		ans = ctr[0];
	
		if( p==2 ){
			ans += (ctr[1]+1)/2;
		}
		else if( p==3 ){
			j = min(ctr[1],ctr[2]);
			ans +=j;
			ctr[1] -= j;
			ctr[2] -= j;
			
			ans += (ctr[1]+ctr[2]+2)/3;
			
		}
		else{
			j = min(ctr[1],ctr[3]);
			ans += j;
			ctr[1] -= j;
			ctr[3] -= j;
//			printf("%d\n",ans);
			j = ctr[2]/2;
			ans += j;
			ctr[2] -= j*2;
//			printf("%d\n",ans);
			j = ctr[1] + ctr[3];
			if( j>1 && ctr[2] ){	// 2 + 1/3 + 1/3 = 4
				ans++;
				j-=2;
				ctr[2]--;
			}
			
			if( ctr[2] && j==0 ) ans++;
			else{
				ans += (j+3)/4;
			}
		}
		
		printf("Case #%d:",++t);	
		printf(" %d\n",ans);
	}
	return 0;
}

