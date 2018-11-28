
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <utility>
#include <queue>
#include <stack>
#include <set>
#include <map>

using namespace std ; 

typedef long long ll ; 

void sol(){
    ll N, K ; 
    scanf("%lld%lld", &N, &K);
    map<ll, ll> M ; 
    M[N] = 1;
    while(true) {
        map<ll, ll> newMap;
        for(auto iter = M.rbegin() ; iter != M.rend() ; iter++) {
            if(K <= iter->second) {
                ll itv = iter->first - 1 ; 
                printf("%lld %lld\n", itv - itv/2,
                                      itv/2);
                return ;
            }
            K -= iter->second;
            ll itv = iter->first;
            if(itv % 2) {
                newMap[(itv-1)/2] += 2*(iter->second);
            }
            else {
                ll i = itv-1;
                ll h = i/2;
                newMap[h] += iter->second;
                newMap[i-h] += iter->second;
            }
        }
        M = newMap;
    }
}

int main()
{
    int T ; 
    scanf("%d", &T) ; 
    for(int time = 1 ; time <= T ; time++){
        fprintf(stderr, "solving case (%d / %d)...\n", time, T) ; 
        printf("Case #%d: ", time) ; 
        sol() ; 
    }
    return 0 ; 
}


