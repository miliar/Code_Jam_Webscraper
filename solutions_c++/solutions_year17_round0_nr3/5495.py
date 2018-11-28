#define _CRT_SECURE_NO_WARNINGS
#include <map>
#include <vector>
#include <algorithm>
#include <inttypes.h>
#include <assert.h>


struct Solution
{
	__int64 l, r;

	__int64 sum() const { return l + r;  }

	__int64 max() const { return std::max< __int64 >( l, r ); }
	__int64 min() const { return std::min< __int64 >( l, r ); }

	bool operator < ( const Solution &rhs ) const
	{
		return sum() < rhs.sum();
	}
};

Solution subSolve( __int64 N )
{
	Solution result;
	__int64 pos = N / 2;
	result.l = pos;
	result.r = N - pos - 1;
	return result;
}

Solution solve( __int64 N, __int64 K )
{
	std::map< __int64, __int64 > range;

	range.insert( { N, 1 } );

	while ( K )
	{
		auto itLast = range.end(); itLast--;

		Solution s = subSolve( itLast->first );
		if ( K == 1 ) return s;

		auto it = range.find( s.l );
		if ( it != range.end() )
			it->second++;
		else range.insert( { s.l, 1 } );

		it = range.find( s.r );
		if ( it != range.end() )
			it->second++;
		else range.insert( { s.r, 1 } );

		itLast->second--;
		if ( itLast->second == 0 )
			range.erase( itLast );

		K--;
	}

	assert( false );
	return Solution();
}
/*
Solution solve_slow( __int64 N, __int64 K )
{

}
*/
int main()
{
	FILE *fin, *fout;
	if ( !( fin = fopen( "C-small-2-attempt1.in", "r" ) ) ) return -1;

	if ( !( fout = fopen( "res.txt", "w" ) ) ) return -1;

	int nCases;
	fscanf( fin, "%d\n", &nCases );
	for ( int iCase = 1; iCase <= nCases; iCase++ )
	{
		__int64 N, K;
		fscanf( fin, "%" PRIu64 " %" PRIu64, &N, &K );
		auto s = solve( N, K );
		fprintf( fout, "Case #%d: %" PRIu64 " %" PRIu64  "\n", iCase, s.max(), s.min() );
	}

	fclose( fin );
	fclose( fout );

	return 0;
}
