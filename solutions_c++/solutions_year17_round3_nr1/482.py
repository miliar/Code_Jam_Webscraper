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

int T,N,K;
long long int dn[1100][1100];
typedef pair <long long int, long long int > ii;
ii ar[1100];

int main(){
	
	cin >> T;

	for( int mask=1 ; mask<=T ; mask++ ){
		cin >> N >> K;
		for( int i=1,a,b ; i<=N ; i++ ){
			scanf(" %d %d",&a,&b);
			ar[i].fi=a;
			ar[i].se=1LL*a*b;
		}

		sort( ar+1 , ar+1+N );

		for( int j=1 ; j<=K ; j++ ){
			long long int mx=-1e15;
			if( j == 1 ) mx=0;
			for( int i=1 ; i<=N ; i++ ){
				dn[i][j]=mx+ar[i].se;
				mx=max( mx , dn[i][j-1] );
			}
		}

		double ans=0;
		for( int i=K ; i<=N ; i++ ){
			ans=max( ans , M_PI*ar[i].fi*ar[i].fi+2*M_PI*dn[i][K] );
		}

		printf("Case #%d: %.6lf\n",mask,ans);

	}

	return 0;
}