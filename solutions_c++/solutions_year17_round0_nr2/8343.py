#include <bits/stdc++.h>

typedef long long int ll;
typedef unsigned long long int ull;
#define rep(i,n) for(ll i=0;i<(n);i++)

using namespace std;


ll top(ll n){
    ll x = 1;
    while(true){
        ll update = 10*x;
        if(update < n)  x = update;
        else            break;
    }
    return (n/x)*x;
}

int main(){
    int t;
    cin >> t;

    rep(times, t){
        ll n;
        cin >> n;

        ll underOnes = 1;
        while(true){
            ll update = 10*underOnes + 1;
            if(update <= n) underOnes = update;
            else            break;
        }

        ll under = underOnes;
        for(int i = 1; i < 10; i++){
            ll update = i*underOnes;
            if(update <= n) under = update;
        }

        ll adder = underOnes/10;

        while(0 < adder){
            ll over = top(adder);
            if(under%(10*over)/over == 9){
                adder /= 10;
                continue;
            }
            ll update = under + adder;
            if(update <= n) under = update;
            else            adder /= 10;
        }

        cout << "Case #" << times+1 << ": " << under << endl;
    }



    return 0;
}
