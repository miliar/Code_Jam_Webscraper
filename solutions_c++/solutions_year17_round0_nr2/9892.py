#include <iostream>
#include <sstream>

int getNumbericCharValue( char* c )
{
	return static_cast<int>(*c - '0');
}

unsigned long long getLastTidyNumber( unsigned long long* i )
{
	std::string digits = std::to_string( *i );
	int last = -1;
	unsigned long long maxLength = digits.length();
	for( unsigned long long y = 0; y < maxLength; y++ ) {
		int tmp = getNumbericCharValue( &digits[ y ] );

		if( last == -2 ) {
			digits[ y ] = '9';
		}
		else if( tmp >= last )
		{
			last = tmp;
		}
		else
		{	
			char c = static_cast<char>(last - 1) + '0';

			while( y > 0 && getNumbericCharValue( &digits[ y - 1 ] ) >= tmp )
			{
				tmp = getNumbericCharValue( &digits[ y - 1 ] );
				c = static_cast<char>(tmp - 1) + '0';
				y--;
			}

			if( y == 0 && tmp == 1 )
			{
				maxLength--;
				c = '9';
			}

			digits[ y++ ] = c;
			digits[ y ] = '9';
			last = -2;
		}
	}
	digits[ maxLength ] = '\0';

	return std::stoull( digits );
}

int main() {
	int t;
	unsigned long long n;

	std::cin >> t;
	for( int i = 1; i <= t; ++i )
	{
		std::cin >> n;
		std::cout << "Case #" << i << ": " << getLastTidyNumber( &n ) << std::endl;
	}
	return 0;
}