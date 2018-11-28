#include <iostream>
#include <cmath> //pow

typedef long long num;


// returns complement such as complement + n = _99999...
num getComplement( num n )
{
    num complement = 0;
    int power = 0;

    for( ; n != 0; n /= 10, ++power )
    {
	int thisDigit = n % 10;
	complement += ( 9 - thisDigit ) * pow( 10, power );
    }
    complement -= pow( 10, power );
    return complement;
}

num tidy( num n )
{
    int lastDigit = 10; //will allways be greater than first digit
    int power = 0;        //power of ten of the current digit
    num tidied = n;
    num complement = 0;

    //iterate digits right to left
    for( ; n != 0; n /= 10, ++power )
    {
	int thisDigit = n % 10;
	if( thisDigit > lastDigit )
	{
	    tidied += getComplement( complement );
	    return tidy( tidied ); //recursively tidy
	}
	lastDigit = thisDigit;
	complement += thisDigit * pow( 10, power );
    }
    return tidied;
}

int main()
{
    num cases;
    std::cin >> cases;
    for( num i = 1; i <= cases; ++i )
    {
	num untidy;
	std::cin >> untidy;
	std::cout << "Case #" << i << ": " << tidy( untidy ) << "\n";
    }
}
