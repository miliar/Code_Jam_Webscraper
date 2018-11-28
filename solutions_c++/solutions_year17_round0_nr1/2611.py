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
char inname[]  = "A-large.in";
char outname[] = "A-large.out";
#else
char inname[]  = "A-small.in";
char outname[] = "A-small.out";
#endif

typedef long long LL;


void flip( char* S, int p, int K, int *sum)
{
  for( int i=p; i<p+K; i++)
  {
      S[i] = !S[i];
      *sum += S[i] ? 1 : -1;
  }
}

void solve_case(void)
{
    int K, l, cnt=0, sum=0;
    char S[1000];

    cin >> S >> K;
    l = strlen(S);
    for( int i=0; i<l; i++)
    {
        S[i] = (S[i] == '-');
        if( S[i])
            sum++;
    }
    for( int i=0; i<=l-K; i++)
    {
        if( S[i])
        {
            flip(S,i,K,&sum);
            cnt++;
        }
    }
    if( sum)
        cout << "IMPOSSIBLE";
    else
        cout << cnt;
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

