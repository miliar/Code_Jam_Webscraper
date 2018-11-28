#include <iostream>
#include <cstdio>
#include <cstring>
#include <bitset>

using namespace std;

int main()
{
  int t;
  cin >> t;
  for( int c = 1 ; c <= t ; ++c )
  {
    string s;
    int k;
    cin >> s >> k;
    int tot = 0;
    for( int i = 0;  i <= s.size()- k  ; ++i  )
    {
      if( s[ i ] == '-' )
      {
        ++tot;
        for( int j = 0 ; j < k ; ++j )
        {
          if( s[ i + j ] == '-' )
            s[ i + j ] = '+';
          else
            s[ i + j ] = '-';
        }
      }
    }
    bool fin = true;
    for( int i = 0; i < s.size() ; ++i )
    {
      if( s[ i ] == '-' )
        fin = false;
    }
    cout << "Case #" << c << ": ";
    if( fin )
      cout << tot ;
    else
      cout << "IMPOSSIBLE";
    cout << "\n";
    // cout << s << endl;
  }
  return 0;
}
