#include <iostream>
#include <fstream>
#include <limits>
#include <string>

typedef unsigned long long Number;

bool is_tidy( Number n ) {
  if ( n < 10 )
    return true;
  Number digit = 1;
  int right = n % 10;
  for ( ;;) {
    digit *= 10;
    if ( digit > n )
      break;
    int left = (n / digit) % 10;
    if ( left > right ) {
      return false;
    }
    right = left;
  }
  return true;
}

Number find_n( Number n )
{
  Number digit = 1;
  for ( ;;) {
    if ( is_tidy( n ) )
      break;
    int left = (n / digit) % 10;
    if ( left != 9 ) {
      n -= (left + 1) * digit;
    }
    digit *= 10;
  }
  return n;
}
int main()
{
	int t;
	std::ifstream is("L:/cj17/B-large.in");
	is >> t;
	int c = 1;
	while (t-- > 0)
	{
    Number n;
		is >> n;
		Number tidy = find_n(n);
		std::cout << "Case #" << c++ << ": ";
		std::cout << tidy << std::endl;
	}
	return 0;
}