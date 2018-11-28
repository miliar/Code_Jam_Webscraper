#include <cstdio>
#include <cstdlib>
#include <stack>
#include <algorithm>
#include <cmath>
#include <cstring>
#define ll long long
#define N 111111
#define md 100000000
#define PI 2*acos(0.0)
using namespace std;

int t;
ll n;

ll solve(ll m){
    // check if m is increasing
    bool inc = true;
    for(ll k = m, ld = k % 10; k; ld = k % 10, k /= 10){
        if(k % 10 > ld) inc = false;
    }
    if(inc) return m;
    return solve(m/10-1)*10 + 9;
}

int main(){
    
    scanf("%d", &t);
    for(int s = 1; s <= t; s++){
        scanf("%lld", &n);
        printf("Case #%d: %lld\n", s, solve(n));
    }
    
    return 0;
}
