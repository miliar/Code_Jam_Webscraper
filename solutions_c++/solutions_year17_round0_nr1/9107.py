#include <iostream>
#include <string>
using namespace std;

int main()
{
  int tot, k, n, cnt=0, step;
  string s;
  cin >> tot;
  while ( ++ cnt <= tot )
    {
      step = 0;
      cin >> s >> k;
      n = s.length();
      int cur = 0;
      while (cur <= n - k) {
        if ( s[ cur ] == '-' )
          {
            ++ step;
            for (int j = cur; j < cur + k ; ++ j )
              if ( s[ j ] == '-' )
                s[ j ] = '+';
              else
                s[ j ] = '-';
          }
        ++ cur;
      }
      for (int i = 0 ; i < s.length() ; ++ i )
        if ( s[ i ] == '-' )
          {
            cout << "Case #" << cnt << ": IMPOSSIBLE" << endl;
            break;
          }
        else if ( i == s.length() - 1 )
          cout << "Case #" << cnt << ": " << step << endl;
    }
  return 0;
}
