#include <iostream>
#include <string>


std::string largest(std::string s)
{
  bool good;
  do
  {
    good = true;
    for ( size_t i = 1; i < s.length(); ++i )
    {
      if ( s[i] < s[i - 1] )
      {
        good = false;
        s[i - 1]--;
        for ( size_t j = i; j < s.length(); ++j )
          s[j] = '9';
        break;
      }
    }
  }
  while ( !good );
  size_t p = 0;
  while ( p < s.length() && s[p] == '0' )
    ++p;
  s.erase(0, p);
  if ( s.empty() )
    s.push_back('0');
  return s;
}


int main()
{
  int T;
  std::cin >> T;
  for ( int t = 1; t <= T; ++t )
  {
    std::string s;
    std::cin >> s;
    std::cout << "Case #" << t << ": " << largest(s) << '\n';
  }
  return 0;
}
