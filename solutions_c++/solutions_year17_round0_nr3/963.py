#include <algorithm>
#include <string>
#include <iostream>
#include <cassert>
#include <time.h>
#include <vector>
#include <unordered_map>
#include <queue>

typedef unsigned long long int ll;

using namespace std;


ll getMid(ll n){
    ll ret = n / 2;
    if(n % 2 == 1){
        ret++;

    }

    return ret;
}

ll getLeft(ll n){
    return getMid(n) - 1;
}

ll getRight(ll n){
    return n - (getMid(n));
}

ll cielHalf(ll n){
    if(n % 2 == 0){
        return n/2;
    }else{
        return (n/2) + 1;
    }

}

ll recurse(ll n, ll k){
    if(k == 1){
        return n;
    }
    if(k * 2 == n){
        return 2;
    }
    k--;

    if( n % 2 == 1){
        return recurse(n/2, cielHalf(k));
    }else{
        ll large = n/2;
        ll small = (n/2) - 1;

        if(k % 2 == 1){
            return recurse(large, cielHalf(k));
        }else{
            return recurse(small, k/2);
        }

    }

}



int main(){
    int testCases;
    cin >> testCases;

    for(int i = 0 ; i < testCases; i++){
        ll n, k;
        cin >> n;
        cin >> k;

        ll max_a;
        ll min_a;

        ll used = recurse(n, k);


        max_a = max(getLeft(used), getRight(used));
        min_a = min(getLeft(used), getRight(used));

        cout << "Case #" << (i + 1) << ": " << max_a << " " << min_a << endl;

    }




}
