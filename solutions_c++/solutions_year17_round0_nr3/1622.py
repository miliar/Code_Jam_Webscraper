#include <iostream>
#include <fstream>
#include <limits>
#include <string>
#include <algorithm>
#include <map>

typedef signed long long Number;

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

void solve_case( Number n, Number k ) {
  std::map<Number, Number> regions;
  regions[n] = 1;
  int max_lr = 0;
  int min_lr = 0;
  Number left;
  Number right;
  while ( k > 0 ) {
    auto largest = *regions.rbegin();
    left = (largest.first - 1) / 2;
    right = (largest.first - 1) - left;
    regions[left] += largest.second;
    regions[right] += largest.second;
    if ( largest.second >= k )
      break;
    k -= largest.second;
    regions.erase( largest.first );
  }
  
  std::cout << std::max(left, right) << " " << std::min( left, right ) << std::endl;
}


int main() {
  int t;
  std::ifstream is( "L:/cj17/C-large.in" );
  is >> t;
  int c = 1;
  while ( t-- > 0 ) {
    Number n;
    Number k;
    is >> n >> k;
    std::cout << "Case #" << c++ << ": ";
    solve_case( n, k );

  }
  return 0;
}