//
//  main.cpp
//  CodeJamQ2
//
//  Created by Vivek Gangwar on 08/04/17.
//  Copyright © 2017 Vivek Gangwar. All rights reserved.
//

#include <iostream>
#include <bits/stdc++.h>
#define ll long long
using namespace std;
int main() {
    int t;
    cin >> t;
    for (int tst = 1 ; tst <= t ; tst++) {
        ll n, tmp;
        cin >> n;
        int a[20],size;
        tmp = n;
        size =0 ;
        while (tmp != 0) {
            a[size++] = tmp%10;
            tmp = tmp/10;
        }
        //reverse array b
        reverse(a, a+size);
        int tmp1 = -1;
        for (int i = 0 ; i < size-1 ; i++) {
            if(a[i] > a[i+1]) {
                tmp1 = i;
                break;
            }
        }
        if(tmp1 == -1) {
            cout << "Case #" << tst << ":" << " " << n << endl;
        }
        else {
            int tmp2 = -1;
            for (int j = tmp1 ; j > 0 ; j--) {
                if(a[j] != a[j-1]) {
                    tmp2 = j;
                    break;
                }
            }
            if(tmp2 == -1) {
                if(a[0] == 1) {
                    cout << "Case #" << tst << ":" << " ";
                    for (int i = 0 ; i < size-1 ; i++) {
                        cout << "9";
                    }
                    cout << endl;
                } else {
                    cout << "Case #" << tst << ":" << " " << a[0]-1;
                    for (int i = 0 ; i < size-1 ; i++){
                        cout << "9";
                    }
                    cout << endl;
                }
            } else {
                cout << "Case #" << tst << ":" << " ";
                for (int i = 0 ; i < tmp2 ; i++) {
                    cout << a[i];
                }
                cout << a[tmp2]-1;
                for (int i = tmp2+1 ; i < size ; i++) {
                    cout << "9";
                }
                cout << endl;
            }
        }
    }
    return 0;
}
