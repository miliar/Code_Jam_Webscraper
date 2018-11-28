#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <cmath>
#include <algorithm>
#include <queue>

using namespace std;

const int maxn = 50 + 5;

int n , K;
double prob[maxn] , sum;

int main( int argc , char * argv[] ){
	freopen( "C-small-1-attempt0.in" , "r" , stdin );
	freopen("C-small-1-attempt0.out", "w", stdout );
	int T , cas = 0;
	scanf( "%d" , & T );
	while( T -- ){
		scanf( "%d%d%lf" , & n , & K , & sum );
		for(int i = 1 ; i <= n ; ++ i) scanf( "%lf" , prob + i );
		prob[++ n] = 1;
		sort( prob + 1 , prob + n + 1 );
		for(int i = 1 ; i < n ; ++ i){
			double dis = prob[i + 1] - prob[i];
			if (dis * i <= sum){
				for(int j = 1 ; j <= i ; ++ j)
					prob[j] += dis;
				sum -= dis * i;
			}else{
				dis = sum / i;
				for(int j = 1 ; j <= i ; ++ j)
					prob[j] += dis;
				break;
			}
		}
		double ret = 1;
		for(int i = 1 ; i <= n ; ++ i) ret *= prob[i];
		printf( "Case #%d: %.6f\n" , ++ cas , ret );
	}
	return 0;
}
