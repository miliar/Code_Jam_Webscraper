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
char inname[]  = "B-large.in";
char outname[] = "B-large.out";
#else
char inname[]  = "B-small.in";
char outname[] = "B-small.out";
#endif

typedef long long LL;

void handle( LL *t, LL b)
{
  LL b2 = b*10;
  LL big = *t / b2;
  LL tb = big % 10;
  big *= b2;
  LL ts = (*t - big) / b;
  if( ts < tb)
  {
    *t = big - 1;
  }
}

void solve_case(void)
{
    LL t;
    LL b = 1;
    cin >> t;
    while( b < t)
    {
        handle(&t, b);
        b *= 10;
    }
    cout << t;
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
}

