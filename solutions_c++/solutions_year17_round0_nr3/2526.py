//
//  main.cpp
//  GoogleJam
//
//  Created by Alexandre Decuq on XX/XX/XXXX.
//  Copyright (c) 2014 Alexandre Decuq. All rights reserved.
//

#include "main.h"

#include <vector>
#include <set>
#include <map> ///set_intersection()
#include <queue>
#include <algorithm>
#include <stdio.h>
#include <iostream>
#include <string>  ///memset
#include <cstring>
#include <cassert>
#include <iomanip> ///setprecision()
#include <cmath> ///ceil() or floor()
#include <climits> ///INT_MAX

using namespace std; ///std::to_string(int)

int main()
{
    /** READ INPUT FILE */
    FILE *fp = freopen("/home/alex/Projects/googlecodejam/C-large.in", "r", stdin);
    freopen("/home/alex/Projects/googlecodejam/C-large.out", "w", stdout);
    if(fp==0) cout <<"ERROR reading input file" << endl;

    /** BEGIN ALGORITHM */
    int T;
    cin>> T; /// T test cases follow

    for(int t=1; t<=T; t++)
    {
        long long n;
        cin >> n;
        long long k;
        cin >> k;

        if(k==n) {
            cout << "Case #"<<t<<": 0 0"<<endl;
        } else {
            long long log2 = k;
            long long maxDistance, minDistance;

            while(log2>0) {
                maxDistance = n/2;
                if(n%2==0) {
                    minDistance = maxDistance - 1;
                } else {
                    minDistance = maxDistance;
                }

                if (maxDistance>minDistance && (log2-1)%2==0)
                    n--;

                log2/=2;
                n/=2;
            }

            minDistance = max(minDistance,(long long)0);
            cout << "Case #"<<t<<": "<<maxDistance<<" "<<minDistance<<endl;
        }
    }
    /** END ALGORITHM */
}


