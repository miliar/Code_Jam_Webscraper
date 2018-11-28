#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <map>
#include <queue>

#define yeral() (node *)calloc( 1 , sizeof(node) )
#define fi first
#define se second
#define o ((b+e)/2)

using namespace std;

const int MOD=1e9+7;

typedef pair <int,int> ii;
int dn[722][722][2][2];
int T,N,M;
int ar[1500],as[1500];

int f( int x , int y , int who , int start ){
	int &rev=dn[x][y][who][start];
	if( rev != -1 ) return rev;
	if( !x && !y ) return rev=(who!=start);
	rev=1500;
	int where=1440-x-y;
	if( x && !ar[where] ) rev=min( rev , f( x-1 , y , 0 , start )+(who!=0) );
	if( y && !as[where] ) rev=min( rev , f( x , y-1 , 1 , start )+(who!=1) );
	return rev;
}

int main(){
	
	cin >> T;
	for( int mask=1 ; mask<=T ; mask++ ){
		memset( dn , -1 , sizeof  dn );
		memset( ar , 0 , sizeof  ar );
		memset( as , 0 , sizeof  as );
		cin >> N >> M;
		for( int i=1,a,b ; i<=N ; i++ ){
			scanf(" %d %d",&a,&b);
			for( int j=a ; j<b ; j++ ) ar[j]=1;
		}
		for( int i=1,a,b ; i<=M ; i++ ){
			scanf(" %d %d",&a,&b);
			for( int j=a ; j<b ; j++ ) as[j]=1;
		}
		int ans=min( f( 720 , 720 , 0 , 0 ) , f( 720 , 720 , 1 , 1 ) );
		printf("Case #%d: %d\n",mask,ans);
	}

	return 0;
}