//
//  AmpleSyrup.cpp
//  TBGJCUtils
//
//  Created by trongbangvp@gmail.com on 4/30/17.
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

typedef struct Cake {
    double r;
    double h;
} Cake;

double maxArea = 0;
void selectCake(int N, int K, vector<Cake>& cakeVec, int startIdx, double currArea)
{
    assert(K>0);
    for(int i = 0, n = N-K+1; i<n; ++i)
    {
        Cake* aCake = &cakeVec[startIdx + i];
        double tempArea = currArea + 2 * M_PI * aCake->r * aCake->h;
        if(startIdx == 0) {
            tempArea += M_PI * aCake->r * aCake->r;
        }
        if(K>1) {
            selectCake(N-i-1, K-1, cakeVec, startIdx+i+1, tempArea);
        } else {
            maxArea = max(maxArea, tempArea);
        }
    }
}

bool compareFunc(Cake& a, Cake& b)
{
    return a.r > b.r;
}

int main(int argc, const char * argv[]) {
    int numTest;
    cin >> numTest;
    for(int i = 0; i<numTest; ++i)
    {
        int N, K;
        cin >> N >> K;
        vector<Cake> cakeVec;
        for(int j=0; j<N; ++j)
        {
            double r, h;
            cin >> r >> h;
            Cake aCake = {r, h};
            cakeVec.push_back(aCake);
        }
        sort(cakeVec.begin(), cakeVec.end(), compareFunc);
        selectCake(N, K, cakeVec, 0, 0);
        printf("Case #%d: %0.9f\n", i+1, maxArea);
        maxArea = 0;
    }
}

