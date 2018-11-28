#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <assert.h>
#include <vector>
#include <algorithm>

struct HorseStart_t
{
	double pos;
	double speed;
	bool operator < ( const HorseStart_t &rhs ) const
	{
		return pos < rhs.pos;
	}
};

double solve( int distance, const std::vector< HorseStart_t > &horsesStart )
{
	struct MoveSegment_t
	{
		double startPos;
		double speed;
		double endTime;
	};
	struct HorseInfo_t
	{
		std::vector< MoveSegment_t > segments;
	};

	std::vector< HorseInfo_t > horses( horsesStart.size() );

	{
		HorseInfo_t &hi = horses.back();
		hi.segments.push_back( { horsesStart.back().pos, horsesStart.back().speed, DBL_MAX } );
	}

	for ( int i = (int)horses.size() - 2; i >= 0; i-- )
	{
		HorseInfo_t &horse = horses[i];
		horse.segments.push_back( { horsesStart[i].pos, horsesStart[i].speed, DBL_MAX } );
		HorseInfo_t &hNext = horses[i + 1];
		for ( size_t iSeg = 0; iSeg < hNext.segments.size(); iSeg++ )
		{
			auto &nextSeg = hNext.segments[iSeg];
			double meetTime = ( nextSeg.startPos - horsesStart[i].pos ) / ( horsesStart[i].speed - nextSeg.speed );
			if ( meetTime <= 0 ) break;
			if ( meetTime < nextSeg.endTime )
			{
				horse.segments.back().endTime = meetTime;
				horse.segments.push_back( { horsesStart[i].pos + meetTime * horsesStart[i].speed, nextSeg.speed, nextSeg.endTime } );
				horse.segments.insert( horse.segments.end(), hNext.segments.begin() + iSeg + 1, hNext.segments.end() );
			}
		}
	}

	HorseInfo_t &hi = horses.front();

	size_t iSeg = 0;
	double startTime = 0;
	while ( true )
	{
		auto &seg = hi.segments[iSeg];
		double endTime = ( distance - seg.startPos ) / seg.speed + startTime;
		if ( endTime <= seg.endTime ) return distance / endTime;
		startTime = seg.endTime;
		iSeg++;
		assert( iSeg < hi.segments.size() );
	}

	return -1;
}

int main()
{
	FILE *fin, *fout;
	if ( !( fin = fopen( "A-small-attempt1.in", "r" ) ) ) return -1;

	if ( !( fout = fopen( "res.txt", "w" ) ) ) return -1;

	int nCases;
	fscanf( fin, "%d\n", &nCases );
	for ( int iCase = 1; iCase <= nCases; iCase++ )
	{
		int distance;
		int n = fscanf( fin, "%d", &distance );
		assert( n == 1 );
		int numHorses;
		n = fscanf( fin, "%d", &numHorses );
		assert( n == 1 );

		std::vector< HorseStart_t > horses;
		for ( int iHorse = 0; iHorse < numHorses; iHorse++ )
		{
			int pos, speed;
			n = fscanf( fin, "%d %d", &pos, &speed );
			assert( n == 2 );
			horses.push_back( { double( pos ), double( speed ) } );
		}

		std::sort( horses.begin(), horses.end() );

		double res = solve( distance, horses );

		fprintf( fout, "Case #%d: %f\n", iCase, res );
	}

	fclose( fin );
	fclose( fout );

	return 0;
}
