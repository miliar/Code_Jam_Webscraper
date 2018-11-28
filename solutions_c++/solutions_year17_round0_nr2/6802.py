#include <iostream>
#include <string>

std::string StripLeadingZeros( std::string& s1 ) {
  int zeroes = 0;
  for( int i=0; i<s1.length() && s1[i] == '0'; i++ ) {
    zeroes++;
  }
  if( s1.length() == zeroes ) return "0";
  else return s1.substr(zeroes, s1.length()-zeroes);
}

int main( void ) {
  int T;
  std::cin >> T;
  for( int t=1; t<=T; t++ ) {
    std::string s;
    std::cin >> s;
    int k = 0;
    for( int i=0; i<s.length()-1; i++ ) {
      if( s[i] > s[i+1] ) {
        s[i-k] = int(s[i-k]) - 1;
        for( int j=i-k+1; j<s.length(); j++ ) {
          s[j] = '9';
        }
      } else if( s[i] == s[i+1] ) {
        k++;
      } else {
        k = 0;
      }
    }
    std::cout << "Case #" << t << ": " << StripLeadingZeros(s) << std::endl;
  }
  return 0;
}