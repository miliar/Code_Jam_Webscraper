#include <bits/stdc++.h>

#define fi first
#define se second

using namespace std;

int T,N,R,O,Y,G,B,V,flag1,flag2,flag3;
typedef pair <char,char> cc;
cc ar[11000];
char C[5];

void print( char c ){
	if( c == 'B' ){
		if( flag1 ){
			flag1=0;
			for( int i=1 ; i<=O ; i++ ) printf("BO");
		}
		printf("B");
	}
	if( c == 'R' ){
		if( flag2 ){
			flag2=0;
			for( int i=1 ; i<=G ; i++ ) printf("RG");
		}
		printf("R");
	}
	if( c == 'Y' ){
		if( flag3 ){
			flag3=0;
			for( int i=1 ; i<=V ; i++ ) printf("YV");
		}
		printf("Y");
	}
}

int main(){
	
	cin >> T;
	
	for( int mask=1 ; mask<=T ; mask++){
		cin >> N >> R >> O >> Y >> G >> B >> V;
		B-=O;
		R-=G;
		Y-=V;
		int K=R+Y+B;
		if( R > K/2 || B> K/2 || Y > K/2 || ( O && B< 0 ) || ( G && R<0 ) || ( V && Y < 0 )){
			printf("Case #%d: IMPOSSIBLE\n",mask);
			continue;
		}
		if( ( O && B== 0 && (K || G || V ) ) || ( G && R<0 && (K || O || V ) ) || ( V && Y < 0 && (K || G || O ) ) ){
			printf("Case #%d: IMPOSSIBLE\n",mask);
			continue;
		}
		printf("Case #%d: ",mask);
		if( !K ){
			for( int i=1 ; i<=O ; i++ ) printf("BO");
			for( int i=1 ; i<=G ; i++ ) printf("RG");
			for( int i=1 ; i<=V ; i++ ) printf("YV");
			puts("");
			continue;
		}
		int T1,T2,T3;
		T1=R; T2=B; T3=Y;
		C[1]='R'; C[2]='B'; C[3]='Y';
		if( B >= Y && B > R ){
			T1=B; T2=R;
			C[1]='B'; C[2]='R';
		}else if( Y >= B && Y > R ){
			T1=Y; T3=R;
			C[1]='Y'; C[3]='R';
		}
		for( int i=1 ; i<=K/2 ; i++ ){
			if( T1 ){
				ar[i].fi=C[1];
				T1--;
			}
			else if( T2 ){
				ar[i].fi=C[2];
				T2--;
			}else ar[i].fi=C[3];
		}
		for( int i=1 ; i<=K/2 ; i++ ){
			if( T1 ){
				ar[i].se=C[1];
				T1--;
			}
			else if( T2 ){
				ar[i].se=C[2];
				T2--;
			}else ar[i].se=C[3];
		}
		flag1=(O>0),flag2=(G>0),flag3=(V>0);
		for( int i=1 ; i<=K/2 ; i++ ){
			print( ar[i].fi );
			if( K&1 && i == 1 ) print( C[3] );
			print( ar[i].se );
		}
		puts("");
	}
	
	return 0;
}
