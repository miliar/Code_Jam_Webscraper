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

int K;

bool isDone(string s) {
    for(int i=0;i<s.size();++i) {
        if(s[i] !='+')
            return false;
    }
    return true;
}

bool flip(string& s, int pos) {
    if (s.size()-pos < K)
        return false;

    for(int i=pos;i<pos+K;++i) {
        if(s[i] =='-')
            s[i] = '+';
        else
            s[i] = '-';
    }
    return true;
}


bool aSolutionExists;

int solve(string s, int pos) {
    if (s.size()-pos < K) {
        if(isDone(s.substr(pos))) {
            return 0;
        } else {
            return -1;
        }
    }

    if(s[pos]=='+')
        return solve(s,pos+1);

    if (!flip(s,pos)) {
        return -2;
    } else {
        int res = solve(s,pos+1);
        return res >=0? res+1 : -1;
    }
}


int main()
{
    /** INITIALIZATION */
    FILE *fp = freopen("/home/alex/Projects/googlecodejam/A-large.in", "r", stdin); //small-attempt2
    freopen("/home/alex/Projects/googlecodejam/A-large.out", "w", stdout);
    if(fp==0) cout <<"ERROR reading input file" << endl;

    /** BEGIN ALGORITHM */
    int T;
    cin>> T; /// T test cases follow

    for(int t=1; t<=T; t++)
    {
        string S;
        cin >> S;
        cin >> K;

        aSolutionExists = true;
        int res = solve(S,0);

        if(res<0)
            cout << "Case #"<<t<<": IMPOSSIBLE"<<endl;
        else
            cout << "Case #"<<t<<": "<<res<<endl;
    }
    /** END ALGORITHM */
}


