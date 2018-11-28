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

int T,N,M;
double U,ar[110];

priority_queue <int , vector <int> , greater <int> > q;

int main(){

	cin >>T;

	for( int mask=1 ; mask<=T ; mask++ ){
		cin >> N >> M;
		cin >> U;
		for( int i=1 ; i<=N ; i++ )	cin >> ar[i];
		sort( ar+1 , ar+1+N );
		ar[N+1]=1.0;
		N=N+1;
		for( int i=1 ; i<N ; i++ )
			if( ar[i] != ar[i+1] ){
				double dif=ar[i+1]-ar[i];
				if( dif*i > U ){
					for( int j=1 ; j<=i ; j++ ) ar[j]+=U/i;
					break;
				}else{
					for( int j=1 ; j<=i ; j++ ) ar[j]+=dif;
					U-=dif*i;
				}
			}
		double ans=1;
		for( int i=1 ; i<=N ; i++ ) ans*=ar[i];
		printf("Case #%d: %.6lf\n",mask,ans);
	}

	return 0;
}