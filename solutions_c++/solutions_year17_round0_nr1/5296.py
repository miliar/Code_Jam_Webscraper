#define _CRT_SECURE_NO_WARNINGS
#include <map>
#include <vector>
#include <algorithm>
#include <assert.h>
#include <set>
#include <random>


struct Row
{
	Row() = default;

	Row( const Row &r, int start, int end )
	{
		cakes.insert( cakes.end(), r.cakes.begin() + start, r.cakes.begin() + end );
	}

	int size() const { return (int)cakes.size(); }

	bool allTrue() const
	{
		for ( const auto &b : cakes )
			if ( !b ) return false;
		return true;
	}

	int all() const
	{
		bool allTrue = true;
		bool allFalse = true;
		for ( const auto &b : cakes )
		{
			if ( b ) allFalse = false;
			else allTrue = false;
		}
		if ( allTrue ) return 1;
		else if ( allFalse ) return 0;
		else return -1;
	}

	void flip( int start, int count )
	{
		for ( int i = start; i < start + count; i++ )
			cakes[i] = !cakes[i];
	}

	bool operator < ( const Row &rhs ) const
	{
		if ( cakes.size() < rhs.cakes.size() ) return true;
		else if ( cakes.size() > rhs.cakes.size() ) return false;
		for ( size_t i = 0; i < cakes.size(); i++ )
		{
			if ( int( cakes[i] ) < int( rhs.cakes[i] ) ) return true;
			else if ( int( cakes[i] ) > int( rhs.cakes[i] ) ) return false;
		}
		return false;
	}

	std::vector< bool > cakes;
};


int solve( const Row &row, int K )
{
//	if ( K > row.size() ) return -1;
	assert( K <= row.size() );

	if ( row.size() == K )
	{
		int all = row.all();
		if ( all == 1 ) return 0;
		else if ( all == 0 ) return 1;
		else return -1;
	}

	int iLeft = 0;
	while ( iLeft + K <= row.size() && row.cakes[iLeft] ) iLeft++;
	if ( iLeft + K <= row.size() )
	{
		auto r = Row( row, iLeft, row.size() );
		r.flip( 0, K );
		iLeft = solve( r, K );
	}
	else iLeft = -1;

	int iRight = row.size();
	while ( iRight - K >= 0 && row.cakes[iRight - 1] ) iRight--;
	if ( iRight - K >= 0 )
	{
		auto r = Row( row, 0, iRight );
		r.flip( iRight - K, K );
		iRight = solve( r, K );
	}
	else iRight = -1;

	if ( iRight != -1 && iLeft != -1 )
		return std::min< int >( iLeft, iRight ) + 1;
	else if ( iRight >= 0 ) return iRight + 1;
	else if ( iLeft >= 0 ) return iLeft + 1;
	else
	{
		if ( row.allTrue() ) return 0;
		else return -1;
	}
}

int solve_brute( const Row &row, int K, const std::set< Row > &states )
{
	if ( row.allTrue() ) return 0;

	int result = -1;
	for ( int i = 0; i <= row.size() - K; i++ )
	{
		Row r = row;
		r.flip( i, K );
		if ( states.find( r ) != states.end() ) continue;
		auto ns = states;
		ns.insert( r );
		int t = solve_brute( r, K, ns );
		if ( t >= 0 && ( t < result || result == -1 ) ) result = t + 1;
	}

	return result;
}

int main()
{
	FILE *fin, *fout;
	if ( !( fin = fopen( "A-small-attempt0.in", "r" ) ) ) return -1;

	if ( !( fout = fopen( "res.txt", "w" ) ) ) return -1;

	int nCases;
	fscanf( fin, "%d\n", &nCases );
	for ( int iCase = 1; iCase <= nCases; iCase++ )
	{
		Row row;
		while ( true )
		{
			char c = fgetc( fin );
			if ( c == '+' ) row.cakes.push_back( true );
			else if ( c == '-' ) row.cakes.push_back( false );
			else if ( c == ' ' ) break;
			else assert( false );
		}
		int K;
		int n = fscanf( fin, "%d", &K );
		assert( n == 1 && K > 0 && K <= row.size() );

		char c = fgetc( fin );
		assert( c == '\n' || c == -1 );

		int result = solve( row, K );

		fprintf( fout, "Case #%d: ", iCase );
		if ( result >= 0 ) fprintf( fout, "%d\n", result );
		else fprintf( fout, "IMPOSSIBLE\n" );
	}

	fclose( fin );
	fclose( fout );

	return 0;

#if 0
	std::mt19937 randEngine;
	for ( int i = 1; i <= 100; i++ )
	{
		int n = std::uniform_int_distribution< int >( 1, 1000 )( randEngine );
		int k = std::uniform_int_distribution< int >( 1, n )( randEngine );
		
		Row row;
		row.cakes.resize( n );
		for ( int i = 0; i < n; i++ )
			row.cakes[i] = std::uniform_int_distribution< int >( 0, 1 )( randEngine ) != 0;

/*		printf( "case %d (%d,%d) ", i, n, k );

		int s1 = solve( row, k );
		int s2 = solve_brute( row, k, { row } );
		if ( s1 == s2 )
			printf( "ok\n" );
		else throw std::runtime_error( "booo" );*/

		solve( row, k );
	}
#endif
}
