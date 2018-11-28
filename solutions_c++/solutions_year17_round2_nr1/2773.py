//
//  CruiseControl.cpp
//  TBGJCUtils
//
//  Created by trongbangvp@gmail.com on 4/22/17.
//  Copyright © 2017 trongbangvp@gmail.com. All rights reserved.
//

#include <stdio.h>
#include <assert.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <math.h>
#include <limits.h>
using namespace std;
//#define printf(...)

int main(int argc, const char * argv[]) {
    int numTest;
    cin >> numTest;
    for(int i = 0; i<numTest; ++i)
    {
        double D, N;
        cin >> D >> N;
        double prevT = __DBL_MAX__;
        for(int j = 0; j<N; ++j)
        {
            double K, S;
            cin >> K >> S;
            double T = (D - K)/S;
            if(j > 0)
            {
                if(T < prevT)
                    T = prevT;
            }
            prevT = T;
        }
        double speed = D/prevT;
        //cout <<"Case #" <<i+1 <<": " <<speed <<endl;
        printf("Case #%d: %0.6f\n", i+1, speed);
    }
}
