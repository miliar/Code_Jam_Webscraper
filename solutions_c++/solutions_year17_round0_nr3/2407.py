#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>
#include <utility>

using namespace std;

typedef long long lint;

int main() {
    int t;
    lint n, k;
    scanf("%d", &t);
    pair<lint, lint> sol;
    for(int CASE = 1; CASE <= t; CASE++) {
        scanf("%lld %lld", &n, &k);
        lint new_k = k;
        while(new_k ^ (new_k & -new_k)) new_k -= (new_k & -new_k);
        lint num_odd = (n+1) % new_k;
        //cout<<new_k<<" "<<num_odd<<endl;
        lint sz = n, ukup = n, num_pl = 1;
        while(k > num_pl) {
            k -= num_pl;
            ukup -= num_pl;
            num_pl = min(num_pl*2, ukup);
            sz = sz / 2;
        }
        if(sz) sz--;
        sol.second = sz / 2;
        sol.first = sz - sol.second;
        if(num_odd && k > num_odd) {
            if(sz & 1) sol.first--;
            else sol.second--;
        }
        printf("Case #%d: %lld %lld\n", CASE, sol.first, sol.second);
    }
    return 0;
}