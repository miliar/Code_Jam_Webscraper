/* بِسْمِ اللهِ الرَّحْمٰنِ الرَّحِيْمِ */
/* رَّبِّ زِدْنِى عِلْمًا */


#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <ctype.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <iostream>
#include <string>
#include <map>
#include <list>
#include <stack>
#include <set>
#include <deque>

using namespace std;

#define OUTPUT freopen("myfile.txt","w",stdout);
#define INPUT freopen("B-large.in","r",stdin);
#define DEBUG(a) cout<<a<<endl;
#define PI acos(-1.0)
#define MAX 100005
#define MOD 1000000007
#define EPS 1e-9
#define BIGGER(a,b) (a>=b ? a : b)
#define SMALLER(a,b) (a<=b ? a : b)
#define getInt(a) scanf("%d",&a);
#define getLong(a) scanf("%lld",&a);
#define pb push_back
#define ppb pop_back
#define setBit(a,n) a|(1<<n)
#define setBitStatement(a,n) a|=1<<n;
#define resetBit(a,n) a&=~(1<<n);
#define checkBit(a,n) ((a&(1<<n))!=0)
#define toggleBit(a,n) a^=1<<n;
#define floatingEqual(a,b) (fabs(a-b)<=EPS)
#define floatingLess(a,b) ((b-a)>=EPS)
#define floatingGreater(a,b) ((a-b)>=EPS)

#define INF 1000000000

char inp[105];

int main()
{
    // Bismillahir Rahmanir Rahim
    // Rabbi Zidni Ilma

    int T,tp=1;
    int i,N;
    int firstChange;

    INPUT
    OUTPUT

    getInt(T)

    while(T--)
    {
        scanf("%s",inp);

        N = strlen(inp);

        for(i=N-1;i>=0;i--)
        {
            inp[i] -= '0' ;
        }

        for(i=N-1;i>0;i--)
        {
            if(inp[i]<inp[i-1])
            {
                for(int j=i;j<N;j++)
                {
                    inp[j] = 9 ;
                }

                inp[i-1] -- ;
            }
        }



        printf("Case #%d: ",tp);

        for(i=0;i<=N;i++)
        {
            if(inp[i]!=0)
            {
                break;
            }
        }

        for(;i<N;i++)
        {
            printf("%c",inp[i]+'0');
        }

        printf("\n");

        tp++;
    }




    return 0;
}
