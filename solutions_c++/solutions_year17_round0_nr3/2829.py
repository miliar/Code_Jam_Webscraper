#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <vector>
#include <map>
#include <sstream>
#include <string>
#include <math.h>
#include <queue>

#define FO(i,a,b) for (int i = (a); i < (b); i++)
#define RO(i,b,a) for (int i = (b); i >= (a); i--)
#define pb push_back
#define ARR0(A) memset((A), 0, sizeof((A)))
#define ARR1m(A) memset((A), -1, sizeof((A)))
#define ARR0(A) memset((A), 0, sizeof((A)))
#define ARRINF(A) memset((A), 10000, sizeof((A)))


typedef long long LL;
using namespace std;

LL bcks[3][2];
void Q20173(){
    int t; scanf("%d\n",&t);
    LL n,k;

    FO(i,0,t)
    {
        FO(i,0,3) { bcks[i][0]=0;bcks[i][1]=0;}

        scanf("%lld %lld\n",&n,&k);

        LL tots = 0;
        bcks[0][0] = n;
        bcks[0][1] = 1;

        LL lf,rt,slf;
        printf("Case #%d: ",i+1);

        while(tots<k)
        {   
            lf = (bcks[0][0]%2==0) ? (bcks[0][0]/2 - 1) : bcks[0][0]/2;
            rt = bcks[0][0]/2;
            LL slots = bcks[0][1];
            tots += slots;
            slf = lf;

            if(rt==lf) { lf=0;slots= slots*2;}
            
            if(bcks[1][1]!=0 )
            {   bcks[0][0] = bcks[1][0];
                bcks[0][1] = bcks[1][1];

                bcks[1][0] = bcks[2][0];
                bcks[1][1] = bcks[2][1];

                bcks[2][0]=0;
                bcks[2][1]=0;


                if(rt==bcks[0][0])
                {
                    bcks[0][1] += slots;

                    if(lf!=0)
                        {   bcks[1][0] = lf;
                            bcks[1][1] = slots;
                        }

                }
                else if(rt==bcks[1][0])
                {
                    bcks[1][1] += slots;

                    if(lf!=0)
                    {     bcks[2][0] = lf;
                          bcks[2][1] = slots;
                    }
                }
                else if(bcks[1][0]==0)
                {
                    bcks[1][0] = rt;
                    bcks[1][1] = slots;

                    if(lf!=0)
                    {
                        bcks[2][0] = lf;
                        bcks[2][1] = slots;
                    }
                }



            } 
            else
            {   bcks[0][0] = rt;
                bcks[0][1] = slots;

                if(lf!=0)
                {
                    bcks[1][0] = lf;
                    bcks[1][1] = slots;
                }
            }


        }

        printf("%lld %lld\n",rt,slf);
    }
}

int main()
{   
    Q20173();
    return 0;
}
