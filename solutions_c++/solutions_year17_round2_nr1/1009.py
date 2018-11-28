#include <stdio.h>

int doSolve( int casenum )
{
	int N;
	long double D;
	scanf( " %Lg %d", &D, &N );

	int i;
	long double Ki, Si;
	long double maxtime, restime;
	maxtime = -1.0;
	for ( i = 0; i < N; i++ ) {
		scanf( " %Lg %Lg", &Ki, &Si );
		restime = (D-Ki)/Si;
		if ( restime >= maxtime ) maxtime = restime;
	}

	long double rspeed = D / maxtime;

	printf( "Case #%d: %.9Lg\n", casenum, rspeed );

	return 0;
}


int main()
{
	int cn;
	scanf( " %d", &cn );
	int i;
	for ( i = 0; i < cn; i++ ) {
		doSolve( i+1 );
	}
	return 0;
}

