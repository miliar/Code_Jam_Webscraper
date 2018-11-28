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

bool isTidy(ULL x) {

    int oldR = x%10;
    while(x>0) {
        int r = x%10;
        x/=10;
        if(oldR < r)
            return false;
        oldR = r;
    }

    return true;
}

int getDigit(ULL x, int dig) {
    for(int i=0; i<dig; i++) x/=10;
    return x%10;
}

int countDigits(ULL x) {
    int i;
    for(i=0; x>0; i++) {
        x/=10;
    }

    return i;
}

ULL makeTidy(ULL x) {

    ULL y=x;
    ULL z=10;
    for(int i=1; i<countDigits(y); i++) {
        int r = getDigit(y, i);
        int oldR = getDigit(y, i-1);
        if(oldR < r) {
            y = y - y%z - 1;
        }
        z*=10;
    }

    if(isTidy(y)) {
        return y;
    } else {
        return y-1;
    }
}

int main()
{
    LL T; cin>>T;
    for(LL t=0; t<T; t++)
    {
        ULL N; cin >>N;
        cout << "Case #" << t+1 << ": ";

        /*
        while(!isTidy(N)) {
            N--;
        }
        */
        N = makeTidy(N);
        cout << N;

        cout << endl;
    }

    return 0;
}

