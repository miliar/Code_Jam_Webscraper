#include <vector>
#include <deque>
#include <set>
#include <map>
#include <iostream>
#include <string>
#include <sstream>

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;

void pickStall(ULL empty, ULL k, ULL& l, ULL& r)
{
    if(empty == k) {
        l = 0;
        r = 0;
        return;
    }
    //
    ULL ls = (empty-1)/2;
    ULL rs = (empty-1) - ls;

    if(k == 1) {
        l = ls;
        r = rs;
        return;
    }

    ULL kl = (k-1)/2;
    ULL kr = (k-1)-kl;

    if(k%2)
        pickStall(ls, kl, l, r);
    else
        pickStall(rs, kr, l, r);
}

int main()
{
    LL T; cin>>T;
    for(LL t=0; t<T; t++)
    {
        ULL N,K; cin >>N>>K;

        cout << "Case #" << t+1 << ": ";
        
        ULL l,r;
        pickStall(N, K, l, r);
        cout << r << " " << l;

        cout << endl;
    }

    return 0;
}

