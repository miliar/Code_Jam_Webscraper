#include <bits/stdc++.h>

int main(){
	
	int test,t=0,n,k,i,j,ans;
	int r,c;
	char kek[30][30];
	scanf("%d",&test);
	
	for( t=0 ; t<test ;){
		scanf("%d%d",&r,&c);
		for( i=0 ; i<r ; i++ ) scanf("%s",kek[i]);
		
		for( i=0 ; i<r ; i++ ){
			// fill right
			for( j=1 ; j<c ; j++ ) if( kek[i][j]=='?' ) kek[i][j]=kek[i][j-1];
			// fill left
			for( j=c-2 ; j>=0 ; j-- ) if( kek[i][j]=='?' ) kek[i][j]=kek[i][j+1];
		}
		
		// fill downward
		for( i=1 ; i<r ; i++ ) if( kek[i][0]=='?' ) strcpy(kek[i],kek[i-1]);
		// fill upward
		for( i=r-2 ; i>=0 ; i-- ) if( kek[i][0]=='?' ) strcpy(kek[i],kek[i+1]);
		
		printf("Case #%d:\n",++t);	
		for( i=0 ; i<r ; i++ ){
			printf("%s\n",kek[i]);
		}
	}
	return 0;
}

