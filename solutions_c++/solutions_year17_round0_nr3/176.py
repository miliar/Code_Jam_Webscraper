#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <stdint.h>
#include <climits>
#include <algorithm>
using namespace std;

int main(int argc, char **argv) {
    int T;
    cin >> T;
    for(int cn=1;cn<=T;++cn) {
        long long N,K;
        cin >> N >> K;
        --K;
        typedef map<long long, long long> MA;
        MA ma;
        ma[N] = 1;
        while(K) {
            MA::reverse_iterator iter = ma.rbegin();
            long long X = iter->first;
            long long ct = iter->second;
            long long todo = 0;
            if(ct < K) {
                todo = ct;
                K -= ct;
            }
            else {
                todo = K;
                K = 0;
            }
            ma.erase(X);
            if(todo < ct) {
                ma[X] = ct-todo;
            }
            --X;
            long long A = X/2;
            long long B = (X+1)/2;
            ma[A] += todo;
            ma[B] += todo;
        }
        long long ee = 0;
        ee = ma.rbegin()->first;
        if(ee == 0) {
            ee = 1;
        }
        --ee;
        long long A = ee/2;
        long long B = (ee+1)/2;
        printf("Case #%d: %lld %lld\n", cn, B, A);
    }
    return 0;
}
