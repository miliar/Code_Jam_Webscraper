//
//  main.cpp
//  Ques1
//
//  Created by Vivek Gangwar on 22/04/17.
//  Copyright © 2017 Vivek Gangwar. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;

int main() {
    long long t;
    cin >> t;
    for (int i = 1 ; i <= t ; i++) {
        double tmp = 0,d,n,s,res;
        cin >> d >> n;
        for(int i = 0 ; i < n ; i++) {
            long long j ,k;
            cin >> j >> k;
            s = (d-j)/(float)k;
            if(s > tmp) {
                tmp = s;
            }
        }
        res = d/tmp;
        cout << "Case #" << i << ": " ;
        printf("%.6f\n",res);
        
    }
}
