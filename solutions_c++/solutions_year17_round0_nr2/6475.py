#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <map>

using namespace std;

unsigned int FirstUntidy( string const& InputNumber );
void TenX( unsigned int FailIndex, string & InputNumber );
void StripLeadingZeros( string & InputNumber );

int main( int argc, char * argv[] )
{
	//Find out how many iterations there are
	unsigned int nInputs = 0;
	cin >> nInputs;

	//Loop over all inputs
	for ( unsigned int inputIndex = 0; inputIndex < nInputs; ++inputIndex )
	{
		//Read input
		string inputNumber = "";
		cin >> inputNumber;

		while ( true )
		{
			unsigned int failIndex = FirstUntidy( inputNumber );
			if ( failIndex == inputNumber.size() )
			{
				//Output
				StripLeadingZeros( inputNumber );
				cout << "Case #" << inputIndex + 1 << ": " << inputNumber << endl;
				break;
			}
			else
			{
				TenX( failIndex, inputNumber );
			}
		}
	}

	return 0;
}

unsigned int FirstUntidy( string const& InputNumber )
{
	char lastDigit = '0';
	for ( unsigned int digitIndex = 0; digitIndex < InputNumber.size(); ++digitIndex )
	{
		char digitValue = InputNumber.at( digitIndex );
		if ( digitValue < lastDigit )
		{
			return digitIndex;
		}
		else if ( digitValue > lastDigit )
		{
			lastDigit = digitValue;
		}
	}
	return InputNumber.size();
}

void TenX( unsigned int FailIndex, string & InputNumber )
{
	InputNumber[ FailIndex - 1 ]--;

	for ( unsigned int digitIndex = FailIndex; digitIndex < InputNumber.size(); ++digitIndex )
	{
		InputNumber[ digitIndex ] = '9';
	}
}

void StripLeadingZeros( string & InputNumber )
{
	while ( InputNumber.at( 0 ) == '0' )
	{
		InputNumber = InputNumber.substr( 1 );
	}
}
