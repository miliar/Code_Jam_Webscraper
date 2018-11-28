#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <assert.h>
#include <vector>
#include <algorithm>
#include <map>
#include <array>
#include <inttypes.h>

struct Number
{
	Number( __int64 x )
	{
		do
		{
			digits[numDigits++] = x % 10;
			x /= 10;
		} while ( x );

		for ( int i = 0; i < numDigits / 2; i++ )
			std::swap( digits[i], digits[numDigits - i - 1] );
	}

	__int64 toInt64() const
	{
		__int64 result = 0;
		__int64 pow = 1;
		for ( int i = numDigits - 1; i >= 0; i-- )
		{
			result += digits[i] * pow;
			pow *= 10;
		}
		return result;
	}

	bool isDidy() const
	{
		for ( int i = 0; i + 1 < numDigits; i++ )
			if ( digits[i] > digits[i + 1] ) return false;
		return true;
	}

	void make_tidy()
	{
		int pos = 0;
		while ( pos + 1 < numDigits )
		{
			if ( digits[pos] > digits[pos + 1] )
				break;
			pos++;
		}

		if ( pos + 1 == numDigits ) return;

		for ( int i = pos + 1; i < numDigits; i++ )
			digits[i] = 9;

		while ( pos >= 0 )
		{
			int dp = ( pos ? digits[pos - 1] : 0 );
			if ( digits[pos] - 1 >= dp )
			{
				digits[pos]--;
				break;
			}
			else digits[pos] = 9;
			pos--;
		}
	}

	int numDigits = 0;
	std::array< int, 32 > digits;
};

__int64 solve_fast( __int64 x )
{
	Number n( x );
	n.make_tidy();
	return n.toInt64();
}

__int64 solve_slow( __int64 x )
{
	while ( true )
	{
		Number n( x );
		if ( n.isDidy() ) return x;
		x--;
	}
}

int main()
{
/*	for ( int i = 1; i <= 100000; i++ )
	{
		auto s1 = solve_fast( i );
		auto s2 = solve_slow( i );
		assert( s1 == s2 );
	}*/

	FILE *fin, *fout;
	if ( !( fin = fopen( "B-large.in", "r" ) ) ) return -1;

	if ( !( fout = fopen( "res.txt", "w" ) ) ) return -1;

	int nCases;
	fscanf( fin, "%d\n", &nCases );
	for ( int iCase = 1; iCase <= nCases; iCase++ )
	{
		__int64 x;
		fscanf( fin, "%" PRIu64, &x );
		x = solve_fast( x );
		fprintf( fout, "Case #%d: %" PRIu64 "\n", iCase, x );
	}

	fclose( fin );
	fclose( fout );
}
