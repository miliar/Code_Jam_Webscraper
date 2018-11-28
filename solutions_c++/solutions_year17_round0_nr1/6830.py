#include <iostream>
#include <string>

int main( void ) {
  int T;
  std::cin >> T;
  for( int i=1; i<=T; i++ ) {

    std::string s;
    int k;

    std::cin >> s;
    std::cin >> k;

    int flips = 0;

    for( int j=0; j<=s.size()-k; j++ ) {

      if( s[j] == '-' ) {

        // Flip j
        s[j] = '+';

        // Flip j+1 to j+k
        for( int p=j+1; p<j+k; p++ ) {
          if( s[p] == '-' ) s[p] = '+';
          else s[p] = '-';
        }

        flips++;

      }

    }

    // Check if result is all +
    int pluses = 0;
    for( int j=0; j<s.size(); j++ ) {
      if( s[j] == '+' ) pluses++;
    }

    std::cout << "Case #" << i << ": ";
    if( pluses == s.size() ) std::cout << flips << std::endl;
    else std::cout << "IMPOSSIBLE" << std::endl;

  }

  return 0;

}
