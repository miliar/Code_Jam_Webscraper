#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string.h>
#include <math.h>
using namespace std;

#define LARGE 1

#if LARGE==1
char inname[]  = "C-large.in";
char outname[] = "C-large.out";
#else
char inname[]  = "C-small.in";
char outname[] = "C-small.out";
#endif

typedef long long LL;

const int L=10;
int imax=0;

void handle( LL *K, LL *c, LL *v)
{
    LL a,b;

    a = v[0] >> 1;
    b = a;
    if( a+b+1 > v[0])
        b--;
    *K -= c[0];
    if( *K <= 0)
    {
        v[0]=a;
        v[1]=b;
        return;
    }
    for( int i=1; (a+b>0)&&(i<L);i++)
    {
        if(c[i]>0)
        {
            if (a==v[i])
            {
                c[i] += c[0];
                a=0;
            }
            if (b==v[i])
            {
                c[i] += c[0];
                b=0;
            }
        }
        else
        {
            if( a>0 && b==a)
            {
                v[i]=a;
                c[i] = 2*c[0];
                a = 0;
                b = 0;
            }
            if( a>0)
            {
                v[i]=a;
                c[i++]=c[0];
                a = 0;
            }
            if( b>0)
            {
                v[i]=b;
                c[i++]=c[0];
                b=0;
            }
        }
        if(a==0 && b==0 && i>imax)
            imax = i;
    }
    for( int i=0;i<L-1;i++)
    {
        v[i] = v[i+1];
        c[i] = c[i+1];
    }
    c[L-1] = 0;
}

void solve_case(void)
{
    LL N, K;
    LL c[L], v[L];

    cin >> N >> K;
    for(int i=0;i<L;i++)
    {
        c[i]=0;
        v[i]=0;
    }
    c[0] = 1;
    v[0] = N;

    while( K>0)
        handle( &K, c, v);

    cout << v[0] << " " << v[1];
}

int main()
{
    assert( freopen( inname, "r", stdin));
    assert( freopen( outname, "w", stdout));
    int T;
    cin >> T;
    for(int i=1; i<=T; i++)
    {
        cout << "Case #" << i << ": ";
        solve_case();
        cout << endl;
    }
    if(imax>5)
        cout << "WARNING";
}

