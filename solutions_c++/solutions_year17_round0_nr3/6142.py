#include <stdio.h>
#include <algorithm>
#include <queue>

using namespace std;

int n , k;
priority_queue < int > q;
void work () {
	int i , a , b , t;
	while ( q.size () ) q.pop ();
	scanf ( "%d%d" , &n , &k );
	q.push ( n );
	for ( i = 1 ; i <= k ; i++ ) {
		t = q.top (); q.pop ();
		a = (t-1) / 2; b = t - 1 - a;
		q.push ( a ); q.push ( b );
	}
	printf ( "%d %d\n" , max ( a , b ) , min ( a , b ) );
}
int main () {
	FILE *fpw = freopen ( "c.out" , "w" , stdout );
	int i = 0 , t;
	scanf ( "%d" , &t );
	while ( t-- ) {
		printf ( "Case #%d: " , ++i );
		work ();
	}
	return 0;
}
