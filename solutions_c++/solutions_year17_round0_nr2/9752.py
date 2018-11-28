#include <stdio.h>
#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <algorithm>
 
using namespace std;

unsigned long long int N, T = 0;

bool isSol(unsigned long long int x) {
    if( x < 10 ) return true;
    unsigned long long int a, b;
    while(x > 10) {
        a = x%10;
        b = (x%100)/10;
        if(a < b || a == 0 || b == 0) return false;
        x /= 10;
    }
    return true;
}

unsigned long long int solve(unsigned long long int x) {
    while(1) {
        if(isSol(x))
            return x;
        x--;
    }
}


int main() {
    cin >> T;
    for (int caseC = 0; caseC < T; ++caseC) {
        scanf("%lld", &N);
        printf("Case #%d: %lld\n", caseC+1, solve(N));
    }
return 0;
}