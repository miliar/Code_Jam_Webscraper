#include <bits/stdc++.h>
#define ll long long
using namespace std;


int main(){
    freopen("C-large.in", "r", stdin);
    freopen("oneD.txt", "w", stdout);
    int t; cin >> t;
    for(int z = 1; z <= t; ++z){

        ll n, k;
        cin >> n >> k;
        ll c = 1;
        ll co = n%2 == 1 ? 1 : 0 , ce = n%2 == 0 ? 1 : 0;

        while(c < k){
            k -= c;
            c *= 2;
            if(n % 2 == 0){
                n /= 2;
                if(n % 2 == 0){
                    co = ce + 2*co;
                }else {
                    ll prev = co;
                    co = ce;
                    ce = ce + 2*prev;
                }
            }else {
                n /= 2;
                if(n % 2 == 0){
                    ll prev = ce;
                    ce = co*2 + ce;
                    co = prev;
                }else {
                    co = 2*co + ce;
                }

            }
        }

        if(n % 2 == 0){

            if(k <= ce){
                printf("Case #%d: %lld %lld\n",z,  n/2, n/2-1);
            }else {
                --n;
                printf("Case #%d: %lld %lld\n",z,  n/2, n/2);
            }

        }else {

            if(k <= co){
                printf("Case #%d: %lld %lld\n",z,  n/2, n/2);
            }else {
                printf("Case #%d: %lld %lld\n",z, n/2, n/2-1);
            }

        }

    }

}

