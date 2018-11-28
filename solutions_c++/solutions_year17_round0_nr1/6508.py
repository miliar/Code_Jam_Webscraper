#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <map>

using namespace std;

void Flip( unsigned int BeginFlip, unsigned int EndFlip, string & InputStack );

int main( int argc, char * argv[] )
{
	//Find out how many iterations there are
	unsigned int nInputs = 0;
	cin >> nInputs;

	//Loop over all inputs
	for ( unsigned int inputIndex = 0; inputIndex < nInputs; ++inputIndex )
	{
		//Read input
		string inputStack = "";
		unsigned int flipperSize = 0;
		cin >> inputStack >> flipperSize;

		unsigned int flips = 0;
		while ( true )
		{
			//Find the first unhappy pancake
			unsigned int firstUnhappy = 0;
			for (; firstUnhappy < inputStack.size(); ++firstUnhappy )
			{
				if ( inputStack[ firstUnhappy ] == '-' ) break;
			}

			if ( firstUnhappy == inputStack.size() )
			{
				//Output
				cout << "Case #" << inputIndex + 1 << ": " << flips << endl;
				break;
			}
			else
			{
				if ( firstUnhappy + flipperSize <= inputStack.size() )
				{
					//Flip from first unhappy
					Flip( firstUnhappy, firstUnhappy + flipperSize, inputStack );
					++flips;
				}
				else
				{
					//Impossible
					cout << "Case #" << inputIndex + 1 << ": IMPOSSIBLE" << endl;
					break;
				}
			}
		}
	}

	return 0;
}

void Flip( unsigned int BeginFlip, unsigned int EndFlip, string & InputStack )
{
	for ( unsigned int flipIndex = BeginFlip; flipIndex < EndFlip; ++flipIndex )
	{
		if ( InputStack.at( flipIndex ) == '+' )
		{
			InputStack[ flipIndex ] = '-';
		}
		else
		{
			InputStack[ flipIndex ] = '+';
		}
	}
	//cout << "flipped to " << InputStack << endl;
}
