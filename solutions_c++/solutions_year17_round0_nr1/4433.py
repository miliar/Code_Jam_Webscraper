//
//  main.cpp
//  CodeJam1
//
//  Created by Vivek Gangwar on 08/04/17.
//  Copyright © 2017 Vivek Gangwar. All rights reserved.
//

#include<iostream>
#include<string>

#define ll long long
using namespace std;

int main() {
    ll t;
    cin >> t;
    for(int i = 1 ; i <= t ; i++) {
        string s;
        ll k;
        ll count = 0;
        cin >> s >> k;
        int n = s.find('-');
        bool flag = true;
        if(n == -1) {
            cout << "Case #" << i << ": 0\n";
        } else {
            while (flag) {
                if (n+k > s.length()) {
                    cout << "Case #" << i << ": IMPOSSIBLE\n";
                    flag = false;
                }else {
                    count++;
                    for(int j = n ; j < n+k && n+k <= s.length(); j++) {
                        if(s[j] == '-') {
                            s[j] = '+';
                        } else {
                            s[j] = '-';
                        }
                    }
                    n = s.find('-');
                    if (n == -1) {
                        cout << "Case #" << i << ": "<< count <<"\n";
                        flag = false;
                    }
                }
            }
        }
    }
    return 0;
}

