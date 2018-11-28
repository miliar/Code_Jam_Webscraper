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
               freopen("in.txt","r",stdin);
            freopen("out.txt","w",stdout);

        int T ;
        cin >> T ;
        for (int i = 1 ; i <= T  ; i++)
        {
            string S ;
            int K ;
            cin >> S >> K ;
            vector<bool> yes (S.size(),0);
            int b = 0  , res = 0;

            for (int j = 0 ; j <= S.size() - K ; j++)
            {
                if (b % 2 == 0 )
                {
                    if (S [j] == '-')
                        yes [j + K -1] =  1 , b++ , res++;
                }
                else
                {
                    if (S [j] == '+')
                        yes [j + K -1] =  1 , b++ , res++ ;
                }
                 if (yes [j]) yes [j] = 0 , b--;
            }

            bool f = 1 ;
            for (int j = S.size() - K + 1 ; j < S.size() ; j ++)
            {
                if (b % 2 == 0 && S [j] == '-')
                    f = 0 ;
                if (b % 2  && S [j] == '+')
                    f = 0 ;
                 if (yes [j]) yes [j] = 0 , b--;
            }
            if (f)
            printf("Case #%d: %d\n",i,res) ;
            else
            printf("Case #%d: IMPOSSIBLE\n",i);
        }
}
