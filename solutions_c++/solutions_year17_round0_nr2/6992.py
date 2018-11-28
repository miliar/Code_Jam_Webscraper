#include <iostream>
#include<cstdio>
#include<string>
#include<cstring>
#include<vector>
#include<algorithm>
#include<set>
#include<math.h>
#include<map>
#include<stack>
#include<sstream>
#include<queue>
#include<list>
#define INF  -10000000000007
using namespace std;

int main()
{
              freopen("B-large.in","r",stdin);
            freopen("out.txt","w",stdout);

        int T ;
        cin >> T ;
        for (int i = 1 ; i <= T  ; i++)
        {
           string a ;
          cin >> a ;

           printf("Case #%d: ",i) ;
           char c= '#' ;
           for (int j = 0 ; j < a.size()-1;j++)
           {
               if (a[j] > a[j+1])
               {
                    c = a[j] ;
                    break ;
               }
           }
           bool f = 1 ;

           for (int j = 0 ; j < a.size() ;j++)
           {
               if (a[j] == c )
               {
                    if ((c == '1' && !f) || c != '1')
                        cout << a[j] - '0' - 1 ;

                    for (int k = j +1 ; k < a.size() ;k++)
                        cout << "9" ;
                    break ;
               }
               else
                cout << a[j] , f = 0 ;
           }
           cout << "\n" ;

           stringstream ss (a) ;
           long long N ;
            ss >> N ;

        }
}
