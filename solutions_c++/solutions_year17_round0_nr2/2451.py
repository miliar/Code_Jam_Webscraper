//
//  main.cpp
//  GoogleJam
//
//  Created by Alexandre Decuq on 24/03/14.
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

bool isTidy(long long int num) {
    int lastNumber = num % 10;
    int curNumber;
    while (num > 0) {
        num /= 10;
        curNumber =  num % 10;
        if (curNumber > lastNumber)
            return false;
        lastNumber = curNumber;
    }
    return true;
}

long long int solve (long long int n) {
    long long int num = n;
    int pos = 0;
    long long int lastNumber = num % 10;
    long long int curNumber;

    while (num > 0) {
        num /= 10;
        curNumber =  num % 10;
        pos++;
        if (curNumber > lastNumber) {
            long long mod = pow(10,pos);
            long long subSum = (n%mod + 1);
            //update n
            n -= subSum;
            curNumber--;
        }
        lastNumber = curNumber;
    }

    return n;
}

int main()
{
    /** INITIALIZATION */
    FILE *fp = freopen("/home/alex/Projects/googlecodejam/B-large.in", "r", stdin); //small-attempt2
    freopen("/home/alex/Projects/googlecodejam/B-large.out", "w", stdout);
    if(fp==0) cout <<"ERROR reading input file" << endl;

    /** BEGIN ALGORITHM */
    int T;
    cin>> T; /// T test cases follow

    for(int t=1; t<=T; t++)
    {
        long long int n;
        cin >> n;
        int res = 0;

        if(isTidy(n))
            cout << "Case #"<<t<<": "<<n<<endl;
        else {
            long long res = solve(n);
            cout << "Case #"<<t<<": "<<res<<endl;
        }


    }
    /** END ALGORITHM */
}


