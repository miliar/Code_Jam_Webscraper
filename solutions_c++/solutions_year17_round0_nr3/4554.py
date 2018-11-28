//
//  main.cpp
//  CodejamQ3
//
//  Created by Vivek Gangwar on 08/04/17.
//  Copyright © 2017 Vivek Gangwar. All rights reserved.
//

#include <iostream>
#include <queue>
#include <cmath>
#define ll long long
using namespace std;
int main() {
    ll t,op;
    cin >> t;
    for (int tst = 1; tst <= t ; tst++) {
        priority_queue<ll> p;
        ll n , k;
        cin >> n >> k;
        p.push(n);
        for(int i = 0 ; i < k-1 ; i++) {
            ll y = p.top();
            p.pop();
            if( y%2 != 0 ) {
                p.push(y/2);
                p.push(y/2);
            } else if( y%2 == 0 ) {
                p.push(y/2);
                p.push(y/2 - 1);
            }
        }
        op=p.top();
        
        if(op%2!=0) {
            cout << "Case #" << tst << ": " << op/2 << " " << op/2 << endl;
        }
        if(op%2==0) {
            cout << "Case #" << tst << ": " << op/2 << " " << op/2-1 << endl;

        }
    }
    return 0;
}
