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
    FILE *fp = freopen("/home/alex/Projects/googlecodejam/A-large.in", "r", stdin);
    freopen("/home/alex/Projects/googlecodejam/A-large.out", "w", stdout);
    if(fp==0) cout <<"ERROR reading input file" << endl;

    /** BEGIN ALGORITHM */
    int T;
    cin>> T; /// T test cases follow

    for(int t=1; t<=T; t++)
    {
        long long int D;
        cin >> D;
        int N;
        cin >> N;

        long double maxDuration = 0.0;
        for(int i=0;i<N;i++) {
             long double k;
            cin >> k;
             long double s;
            cin >> s;
             long double remainingDistance = D - k;
            long double duration = remainingDistance / s;
            if (duration > maxDuration) {
                maxDuration = duration;
            }
        }

        long double res = D/maxDuration;
        cout << "Case #"<<t<<": "<< std::setprecision(15)<<res<<endl;
    }
    /** END ALGORITHM */
}


