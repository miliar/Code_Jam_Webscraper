#include <iostream>
#include <string>

#define HAPPY '+'
#define BLANK '-'
#define FLIP_CHAR( x ) ( ( x ) == HAPPY ? BLANK : HAPPY )

typedef long long num;

num posOfGreatestConsecutiveBlank( const std::string& pancakes, num maxSize )
{
    num bestPos       = -1;
    num secBestPos    = -1;
    num thisPos       = 0;
    num bestLength    = 0;
    num secBestLength = 0;
    num thisLength    = 0;

    for( size_t i = 0; i < pancakes.size(); ++i )
    {
	if( pancakes[ i ] == BLANK )
	{
	    //new consecutive
	    if( thisLength == 0 )
	    {
		thisPos = i;
	    }
	    ++thisLength;

	    if( thisLength >= maxSize )
	    {
		return thisPos;
	    }
	}
	else
	{
	    if( thisLength > bestLength )
	    {
		secBestPos    = bestPos;
		secBestLength = bestLength;

		bestLength = thisLength;
		bestPos    = thisPos;
	    }
	    thisLength = 0;
	}
    }
    if	   ( bestPos + maxSize <= pancakes.size() )
	return bestPos;
    else if( secBestPos != -1 and secBestPos + maxSize <= pancakes.size() )
	return secBestPos;
    else
	return -1;
}

void flip( std::string& pancakes, const num& pos, const num& panSize )
{
    for( size_t i = pos; i < pos + panSize; ++i )
    {
	pancakes[ i ] = FLIP_CHAR( pancakes[ i ] );
    }
}

bool isSolved( const std::string& pancakes )
{
    for( const char& c : pancakes )
    {
	if( c != HAPPY ) return false;
    }
    return true;
}

num solve( std::string& pancakes, const num& panSize )
{
    for( num i = 0; true; ++i )
    {
	//std::cout << pancakes << " " << panSize << "\n";
	num pos = posOfGreatestConsecutiveBlank( pancakes, panSize );
	if( pos == -1 and isSolved( pancakes ) ) return i;
	else if( pos == -1 and !isSolved( pancakes ) ) return -1;
	else flip( pancakes, pos, panSize );
    }
}

int main()
{
    num cases;
    std::cin >> cases;
    for( num i = 1; i <= cases; ++i )
    {
	std::string pancakes;
	num panSize;
	std::cin >> pancakes >> panSize;
	num flips = solve( pancakes, panSize );
	std::cout << "Case #" << i << ": ";
	if( flips != -1 ) std::cout << flips  << "\n";
	else              std::cout << "IMPOSSIBLE\n";
    }
}
