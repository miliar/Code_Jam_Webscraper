#include <iostream>
#include <fstream>
#include <math.h>
#include <stdlib.h>
#include <string>
#include <set>
#include <map>
#include <bitset>
#include <vector>

using namespace std;

int main( int argc, char* argv[] )
{
	ifstream filereader;
	filereader.open( "C-small-2-attempt0.in" );
	char output[64];

	ofstream filewriter;
	filewriter.open( "C-small-2-attempt0.out" );

	unsigned int testcases = 0;
	unsigned int currentcase = 0;

	if( filereader.is_open() )
	{
		filereader.getline( output, 64 );
		testcases = atoi( output );

		unsigned long long n, k;

		for( currentcase = 1; currentcase <= testcases; ++currentcase )
		{
			filereader.getline( output, 64, ' ' );
			n = std::stoll( output );

			filereader.getline( output, 64 );
			k = std::stoll( output );

			double sqrt_k, temp, fractpart, intpart;
			unsigned int level, tree_level_items, tree_element_element, element, tree_level_min;
			unsigned long long value, max, min, child;

			level = log2( k );
			tree_level_items = pow( 2, level );
			tree_element_element = k - tree_level_items;
			temp = ( ( n - tree_level_items + 1 ) / ( tree_level_items * 1.0 ) );
			fractpart = modf( temp, &intpart );
			element = (unsigned int)( fractpart * tree_level_items );
			tree_level_min = (unsigned int)intpart;

			value = ( tree_element_element >= element ? tree_level_min : tree_level_min + 1 );
				
			--value;
			max = min = value / 2;
			if( value % 2 == 1 ) ++max;

			filewriter << "Case #" << currentcase << ": " << max << " " << min << endl;
		}
	}
	filereader.close();
	filewriter.close();

	return 0;
}