#include <iostream>
#include <vector>
#include <algorithm>

typedef long long num;

typedef struct
{
    num min, max;
} Solution;

typedef struct
{
    num value, occurences;
} gap_type;

void printVec( const std::vector< gap_type >& nums )
{
    for( const gap_type& n : nums )
    {
	std::cout << n.value << "-" << n.occurences << " ";
    }
    std::cout << "\n";
}

void addToOccurences( std::vector< gap_type >& nums, const num& value, const num& times )
{
    //std::cout << "b";
    //std::cout.flush();
    num i = 0;
    while( i < nums.size() and nums[ i ].value > value ) ++i;
    if( nums[ i ].value == value ) nums[ i ].occurences += times;
    else nums.insert( nums.begin() + i, { value, times } );
    if( nums[ 0 ].occurences == 0 ) nums.erase( nums.begin() );
    //std::cout << "e";
    //std::cout.flush();
    //printVec( nums );
}

Solution solve( const num& stalls, const num& people )
{
    std::vector< gap_type > gaps;
    gaps.push_back( { stalls, 1 } );

    //std::cout << "pers 0:";
    //printVec( gaps );

    for( num i = 1; i < people; ++i )
    {
	//if is odd
	if( gaps[0].value % 2 )
	{
	    num greatestGap = gaps[ 0 ].value;
	    gaps[ 0 ].occurences -= 1;

	    addToOccurences( gaps, ( greatestGap - 1 ) / 2, 2 );
	    //if( gaps[ 0 ].occurences == 0 ) gaps.erase( gaps.begin() );
	}
	//if is even
	else
	{
	    num greatestGap = gaps[ 0 ].value;
	    gaps[ 0 ].occurences -= 1;

	    addToOccurences( gaps, greatestGap / 2,     1 );
	    addToOccurences( gaps, greatestGap / 2 - 1, 1 );
	    //if( gaps[ 0 ].occurences == 0 ) gaps.erase( gaps.begin() );
	}
  	//std::cout << "pers. " << i << ": ";
  	//printVec( gaps );
	//short out
	if( gaps[0].value == 1 ) return { 0, 0 };
    }

    //if is odd
    if( gaps[0].value % 2 )
    {
	num greatestGap = gaps[ 0 ].value;
	return { ( greatestGap - 1 ) / 2, ( greatestGap - 1 ) / 2 };
    }
    //if is even
    else
    {
	num greatestGap = gaps[ 0 ].value;
	return { greatestGap / 2, greatestGap / 2 - 1 };
    }
}

int main()
{
    num cases;
    std::cin >> cases;
    for( num i = 1; i <= cases; ++i )
    {
	num stalls, people;
	std::cin >> stalls >> people;
	Solution solution = solve( stalls, people );
	std::cout << "Case #" << i << ": " << solution.min << " " << solution.max << "\n";
    }
}
