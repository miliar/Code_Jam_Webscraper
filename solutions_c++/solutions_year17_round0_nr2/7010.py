#include <stdio.h>
#include <algorithm>
#include <string.h>

using namespace std;

long long n , l;
char z[220];
long long ans;
long long pow[20];
void work () {
	long long i , j , k , t;
	scanf ( "%s" , z + 1 );
	l = strlen ( z + 1 );
	n = 0;
	pow[0] = 1;
	ans = 0;
	for ( i = 1 ; i <= 18 ; i++ ) pow[i] = pow[i-1] * 10;
	for ( i = 1 ; i <= l ; i++ ) n = n * 10 + z[i] - '0';
	if ( n == 1000000000000000000ll ) {
		printf ( "999999999999999999\n" );
		return ;
	}
	for ( i = 1 ; i <= l ; i++ ) {
		for ( j = 9 ; j >= 0 ; j-- ) {
			t = ans;
			for ( k = i ; k <= l ; k++ ) t += j * pow[l-k];
			//printf ( "  %d %d\n" , t , j );
			if ( t <= n ) break;
		}
		//printf ( "%d %d\n" , j , j * pow[l-i] );
		ans += j * pow[l-i];
	}
	printf ( "%lld\n" , ans );
}
int main () {
	FILE *fpw = freopen ( "b.out" , "w" , stdout );
	int i = 0 , t;
	scanf ( "%d" , &t );
	while ( t-- ) {
		printf ( "Case #%d: " , ++i );
		work ();
	}
	return 0;
}
