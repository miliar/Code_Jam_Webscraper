#include <iostream>
#include <string>
using namespace std;

int main()
{
  int cnt=0, tot, n;
  cin >> tot;
  string s;
  int a[20];
  while ( ++ cnt <= tot )
    {
      cin >> s;
      n = s.length();
      for (int i = 0 ; i < n ; ++ i )
          a[i] = int(s[ i ]) - 48;
      if (n > 1)
        {
          int pos = n - 1;
          while ( pos >= 0 )
            {
              if ( a[ pos ] > a[ pos + 1 ] )
                {
                  if ( a[ pos ] > 0 )
                    -- a[ pos ];
                  else // 0 pos must > 0
                    {
                      a[ pos ] = 9;
                      int j = pos - 1;
                      while ( j >= 0 )
                        if ( a[ j ] > 0 )
                          {
                            -- a[ j ];
                            break;
                          }
                        else
                          a[ j -- ] = 9;
                    }
                  for ( int i = pos + 1 ; i < n ; ++ i )
                    a[ i ] = 9;
                }
              -- pos;
            }
        }
      cout << "Case #" << cnt << ": ";
      for ( int i = 0 ; i < n ; ++ i )
        if ( (i != n - 1 && a[ i ] > 0) || i == n - 1 )
          cout << a[ i ];
      cout << endl;
    }
  return 0;
}
