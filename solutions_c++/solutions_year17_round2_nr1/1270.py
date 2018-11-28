#include <bits/stdc++.h>

#define fi first
#define se second
#define o ((b+e)/2)

using namespace std;

typedef pair <int,int> ii;
int T,N;
double D;
ii ar[1100];

bool check( double b ){
	for( int i=1 ; i<=N ; i++ ) if( b > ar[i].se ){
		double t=ar[i].fi/(b-ar[i].se);
		if( t > 0 && b*t < D ) return false;
	}
	return true;
}

int main(){
	
	cin >> T;
	
	for( int i=1 ; i<=T ; i++ ){
		cin >> D >> N;
		for( int i=1 ; i<=N ; i++ )	scanf(" %d %d",&ar[i].fi,&ar[i].se);
		double b=0,e=1e18,ans=-1;
		int cnt=0;
		while( b <= e ){
			if( check( o ) ){
				ans=o;
				b=o;
			}else	e=o;
			cnt++;
			if( cnt == 1000000 ) break;
		}
		printf("Case #%d: %.6f\n",i,ans);
	}
	
	return 0;
}
