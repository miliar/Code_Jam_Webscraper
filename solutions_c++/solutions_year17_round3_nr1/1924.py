#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <deque>
#include <unordered_map>
#include <algorithm>
#include <assert.h>


#define PI (3.141592653589793)

using namespace std;

char tblvalid[1024][1024];
long long dptblA[1024][1024]; // top area
long long dptblB[1024][1024];
long long Rlist[1024];
long long Hlist[1024];

int ensureFunc( long long N, long long K );

long long max( long long A, long long B )
{
	if ( A > B ) return A;
	return B;
}

int dpFuncReal( long long N, long long K )
{
	tblvalid[N][K] = 1;
	if ( K == 0 ) {
		dptblA[N][K] = 0;
		dptblB[N][K] = 0;
		return 0;
	}
	
	if ( K == 1 && N == 1 ) {
		dptblA[N][K] = Rlist[0]*Rlist[0];
		dptblB[N][K] = Rlist[0]*Hlist[0]*2;
		return 0;
	}
	
	if ( N == K ) {
		ensureFunc( N-1, K-1 );
		dptblA[N][K] = Rlist[N-1]*Rlist[N-1];
		dptblB[N][K] = Rlist[N-1]*Hlist[N-1]*2 + dptblB[N-1][K-1];
		//printf( "N=%lld K=%lld tblA tblB %lld %lld\n", N, K, dptblA[N][K], dptblB[N][K] );
		return 0;
	}
	
	assert( N >= K );
	assert( N >= 1 );
	
	ensureFunc( N-1, K );
	ensureFunc( N-1, K-1 );
	long long sumA, sumB;
	sumA = dptblB[N-1][K];
	sumB = dptblB[N-1][K-1] + Rlist[N-1]*Hlist[N-1]*2;
	
	//printf( "N=%lld K=%lld, sumA=%lld, sumB=%lld\n", N, K, sumA, sumB );
	if ( sumB > sumA ) {
		//printf( "N=%lld K=%lld choosing (%lld,%lld).\n", N, K, N-1, K-1 );
		dptblA[N][K] = Rlist[N-1]*Rlist[N-1];
		dptblB[N][K] = dptblB[N-1][K-1] + Rlist[N-1]*Hlist[N-1]*2;
	} else {
		//printf( "N=%lld K=%lld choosing (%lld,%lld).\n", N, K, N-1, K );
		dptblA[N][K] = dptblA[N-1][K];
		dptblB[N][K] = dptblB[N-1][K];
	}
	return 0;
}

int ensureFunc( long long N, long long K )
{
	if ( tblvalid[N][K] ) return 0;
	dpFuncReal( N, K );
	return 0;
}

int doSolve( int casenum )
{
	int N, K;
	scanf( " %d %d", &N, &K );
	
	int i;
	memset( tblvalid, 0, sizeof(tblvalid) );
	
	deque<long long> inarr;
	long long Ri, Hi;
	for ( i = 0; i < N; i++ ) {
		scanf( " %lld %lld", &Ri, &Hi );
		inarr.push_back( Ri<<32|(Hi&0x7FFFFFFF) );
	}
	
	sort( inarr.begin(), inarr.end() );
	//reverse( inarr.begin(), inarr.end() );
	
	for ( i = 0; i < N; i++ ) {
		Rlist[i] = inarr[i] >> 32;
		Hlist[i] = inarr[i] & 0x7FFFFFFF;
		//printf( "Ri Hi %lld %lld\n", Rlist[i], Hlist[i] );
	}
	
	ensureFunc( N, K );
	
	long long ires = 0;
	/*for ( i = K; i <= N; i++ ) {
		ensureFunc( i, K );
		printf( "C %lld %lld\n", (Rlist[i-1]*Rlist[i-1])+dptblB[i][K], dptblB[i][K] );
		if ( (Rlist[i-1]*Rlist[i-1])+dptblB[i][K] > ires ) {
			ires = (Rlist[i-1]*Rlist[i-1])+dptblB[i][K];
		}
	}*/
	for ( i = K-1; i < N; i++ ) {
		ensureFunc( i, K-1 );
		//printf( "L %lld\n", (Rlist[i]*Rlist[i])+Rlist[i]*2*Hlist[i]+dptblB[i][K-1] );
		if ( (Rlist[i]*Rlist[i])+Rlist[i]*2*Hlist[i]+dptblB[i][K-1] > ires ) {
			ires = (Rlist[i]*Rlist[i])+Rlist[i]*2*Hlist[i]+dptblB[i][K-1];
		}
	}
	
	double res = ires*PI;
	//printf( "Dbg #%d: %lld\n", casenum, ires );
	printf( "Case #%d: %.9lf\n", casenum, res );
	return 0;
}

int main()
{
	int n;
	scanf( " %d", &n );
	int i;
	for ( i = 0;i < n; i++ ) {
		doSolve( i+1 );
	}
	
	return 0;
}
