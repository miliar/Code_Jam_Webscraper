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
#include<iomanip>
#define INF  1000000007
using namespace std;

int main()
{
         freopen("A-large.in","r",stdin);
        freopen("out.txt","w",stdout);

        int T ;

        cin >> T ;

        for (int tes = 1 ; tes <= T  ; tes++)
        {
            long long D ;
            int N ;

            cin >> D >> N ;
            double MX = 0 ;
            for (int i = 0 ; i < N ; i++)
            {
                long long dis , s ;
                cin >> dis >> s ;

                MX = max(MX , (D - dis ) / (double (s)) ) ;

            }

            cout << "Case #"<< tes << ": " << fixed << setprecision (6) << D /  MX << "\n" ;
        }
}
