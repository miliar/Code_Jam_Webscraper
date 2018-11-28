#include <iostream>
#include <string>


bool good(std::string const &s)
{
  for ( char c: s )
    if ( c == '-' )
      return false;
  return true;
}


int count(std::string s, int K)
{
  int x = 0;
  int S = s.length();
  for ( int i = 0; i <= S - K; ++i )
    if ( s[i] == '-' )
    {
      for ( int j = i; j < i + K; ++j )
        s[j] = (s[j] == '-' ? '+' : '-');
      ++x;
    }
  if ( good(s) )
    return x;
  return -1;
}


int main()
{
  int T;
  std::cin >> T;
  for ( int t = 1; t <= T; ++t )
  {
    std::string s;
    int K;
    std::cin >> s >> K;
    std::cout << "Case #" << t << ": ";
    int x = count(s, K);
    if ( x >= 0 )
      std::cout << x << '\n';
    else
      std::cout << "IMPOSSIBLE\n";
  }
  return 0;
}
