//
//  main.cpp
//  B
//
//  Created by Jonas Blåsås Lønnum on 08.04.2017.
//  Copyright © 2017 blasas. All rights reserved.
//

#include <algorithm>
#include <string>
#include <cmath>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

#define F0(i,n) for(int i=0;i<n;i++)
#define F1(i,n) for(int i=1;i<=n;i++)

typedef long long i64;
typedef vector<bool> bvec;
typedef vector<string> svec;
typedef vector<int> ivec;
typedef pair<int, int> pair_ii;
typedef pair<double, double> pair_dd;
typedef pair<int, char> pair_ic;

ivec toDigits(i64 value)
{
    ivec digits ;
    for( ; value > 0 ; value /= 10 ) digits.push_back( value%10 ) ;
    reverse( digits.begin(), digits.end() ) ;
    return digits ;
}

bool isTidy(i64 num) {
    bool res = true;
    
    ivec digits = toDigits(num);
    F1(i, digits.size()-1) {
        if(digits[i] < digits[i-1]) {
            res = false;
            break;
        }
    }
    
    return res;
}

void solve() {
    i64 N;
    scanf("%lld", &N);
    
    while(!isTidy(N)) {
        N--;
    }
    
    printf("%lld", N);
}

int main(int argc, const char * argv[]) {
    freopen("/Users/Jonas/Documents/Development/github/google-codejam/2017OnlineQualRound/B/sample.in","r",stdin);
    freopen("/Users/Jonas/Documents/Development/github/google-codejam/2017OnlineQualRound/B/sample.out","w",stdout);
    int T;
    scanf("%d",&T);
    F1(t, T) {
        printf("Case #%d: ", t);
        solve();
        printf("\n");
        
    }
    return 0;
}
