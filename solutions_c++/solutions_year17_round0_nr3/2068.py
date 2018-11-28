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
#define INPUT freopen("C-large.in","r",stdin);
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

struct Twos
{
    long long int segment1;
    long long int cnt1 ;
    long long int segment2;
    long long int cnt2 ;
};

struct Twos transition(struct Twos in);

struct Twos transition(struct Twos in)
{
    struct Twos out;

    long long int minn , maxx ;

    long long int t11,t12,t21,t22;

    t11 = ((in.segment1-1)/2);
    t12 = ((in.segment1-1)/2) + ((in.segment1-1)%2) ;
    t21 = ((in.segment2-1)/2);
    t22 = ((in.segment2-1)/2) + ((in.segment2-1)%2) ;

    out.segment1 = SMALLER(t11,t21);
    out.segment2 = BIGGER(t12,t22);

    out.cnt1 = 0 ;
    out.cnt2 = 0 ;

    if(out.segment1==t11)
    {
        out.cnt1 += in.cnt1;
    }

    if(out.segment1==t12)
    {
        out.cnt1 += in.cnt1;
    }

    if(out.segment1==t21)
    {
        out.cnt1 += in.cnt2;
    }

    if(out.segment1==t22)
    {
        out.cnt1 += in.cnt2;
    }


    if(out.segment2==t11)
    {
        out.cnt2 += in.cnt1;
    }

    if(out.segment2==t12)
    {
        out.cnt2 += in.cnt1;
    }

    if(out.segment2==t21)
    {
        out.cnt2 += in.cnt2;
    }

    if(out.segment2==t22)
    {
        out.cnt2 += in.cnt2;
    }

    if(out.segment1==out.segment2)
    {
        out.cnt1 /= 2 ;
        out.cnt2 /= 2 ;
    }

    return out;
}

int main()
{
    // Bismillahir Rahmanir Rahim
    // Rabbi Zidni Ilma

    int T,tp=1;
    long long int N,K;
    long long int current;
    Twos state1,state2;
    int timee;

    INPUT
    OUTPUT

    getInt(T)

    while(T--)
    {
        getLong(N)
        getLong(K)

        if(K==1)
        {
            printf("Case #%d: %lld %lld\n",tp,((N-1)/2)+((N-1)%2),((N-1)/2));
            goto done;
        }

        else
        {
            timee = 0 ;
            state1.segment1 = ((N-1)/2) ;
            state1.segment2 = ((N-1)/2) + ((N-1)%2) ;
            state1.cnt1 = 1 ;
            state1.cnt2 = 1 ;
            K--;

            while(1)
            {
                if(timee==0)
                {
                    timee = 1 ;

                    if(K<=state1.cnt2)
                    {
                        printf("Case #%d: %lld %lld\n",tp,((state1.segment2-1)/2)+((state1.segment2-1)%2),((state1.segment2-1)/2));
                        goto done;
                    }

                    K-= state1.cnt2;

                    if(K<=state1.cnt1)
                    {
                        printf("Case #%d: %lld %lld\n",tp,((state1.segment1-1)/2)+((state1.segment1-1)%2),((state1.segment1-1)/2));
                        goto done;
                    }

                    K-= state1.cnt1;

                    state2 = transition(state1);

                }

                else
                {
                    timee = 0 ;

                    if(K<=state2.cnt2)
                    {
                        printf("Case #%d: %lld %lld\n",tp,((state2.segment2-1)/2)+((state2.segment2-1)%2),((state2.segment2-1)/2));
                        goto done;
                    }

                    K-= state2.cnt2;

                    if(K<=state2.cnt1)
                    {
                        printf("Case #%d: %lld %lld\n",tp,((state2.segment1-1)/2)+((state2.segment1-1)%2),((state2.segment1-1)/2));
                        goto done;
                    }

                    K-= state2.cnt1;

                    state1 = transition(state2);

                }
            }
        }

        done :

            tp++;

    }





    return 0;
}
