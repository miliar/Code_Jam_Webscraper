//
//  B.cpp
//  Google Codejam 2017
//
//  Created by 허상민 on 2017. 4. 8..
//
//

#include <cstdio>
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
using namespace std;
int T;
typedef long long lld;

lld asc[10000000];
bool chkASC(lld n) {
    lld t = n % 10;
    while(true) {
        n /= 10;
        if(n == 0) break;
        if(n%10 <= t) {
            t = n % 10;
        } else return false;
    }
    return true;
}

lld N;
int main () {
    asc[0] = 1;
    for(lld i = 1; i < 10000000; i++) {
        if(chkASC(i) == true) {
            asc[i] = i;
        } else {
            asc[i] = asc[i-1];
        }
    }

    cin >> T;
    for(int tcase=1;tcase<=T;tcase++) {
        cin >> N;
        
        if(N < 10000000) {
            cout << "Case #" << tcase << ": " << asc[N] << endl;
        } else {
            lld S = 0, t = 1;
            while (!chkASC(N)) {
                if(N%10 == 0) {
                    N -= 1;
                    continue;
                }
                N = N * t + S;
                S = 0, t = 1;
                while(N%10 == 9) {
                    S = S * 10 + 9;
                    t *= 10;
                    N /= 10;
                }
                
                if((N % 10000000) == asc[N % 10000000]) {
                    N -= asc[N % 10000000];
                } else {
                    N -= (N % 10000000) - asc[N % 10000000];
                }
                // cout << "Candidate #" << tcase << ": " << N << S << endl;
            }
            N = N * t + S;
            cout << "Case #" << tcase << ": " << N << endl;
        }
    }
    
    return 0;
}
