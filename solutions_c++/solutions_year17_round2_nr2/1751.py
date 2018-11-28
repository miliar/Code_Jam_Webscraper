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


bool trySwitch(string& u) {
    if(u.size()<4)
        return false;

    int first = u[0];

    int lastPos = u.size()-1;
    int last = u[lastPos];

    int preLastPos = u.size()-2;
    int preLast = u[preLastPos];

    int previousPos = u.size()-3;
    int prev = u[previousPos];

    if( abs(last-prev) >= 2 and abs(first-preLast) >= 2) {
        std::swap(u[lastPos], u[preLastPos]);
        return true;
    }
    return false;
}

string translate(string u) {
    string res = "";
    for(int i=0;i<u.size();++i) {
        if (u[i]=='0')
            res += "R";
        else if (u[i]=='1')
            res += "O";
        else if (u[i]=='2')
            res += "Y";
        else if (u[i]=='3')
            res += "G";
        else if (u[i]=='4')
            res += "B";
        else if (u[i]=='5')
            res += "V";
    }
    return res;
}


int takeNext(vector<int>& u, int pos) {

    int i = (pos + 2) % 6;
    bool cond = true;
    if(pos==0) {
        pos = 5;
    } else {
        pos--;
    }
    int res = -1;
    int nb = 0;

    while (i != pos) {
        if(u[i] > 0) {
            if(res==-1) {
                nb = u[i];
                res = i;
            } else {
                if (u[i] > nb) {
                    nb = u[i];
                    res = i;
                }
            }
        }
        i = (i+1)%6;
    }

    if(res != -1) {
        u[res]--;
    }
    return res;
}

int main()
{
    /** READ INPUT FILE */
    FILE *fp = freopen("/home/alex/Projects/googlecodejam/B-small-attempt2.in", "r", stdin);
    freopen("/home/alex/Projects/googlecodejam/B-small-attempt2.out", "w", stdout);
    if(fp==0) cout <<"ERROR reading input file" << endl;

    /** BEGIN ALGORITHM */
    int T;
    cin>> T; /// T test cases follow

    for(int t=1; t<=T; t++)
    {
        int n;
        cin >> n;

        int next = -1;

        vector<int> unicorns;
        for (int i=0;i<6;i++) {
            int color;
            cin >> color;
            unicorns.push_back(color);
            if (color > 0 && next == -1)
                next = i;
        }

        string res = "";
        while(true) {
            next = takeNext(unicorns,next);
            if (next == -1)
                break;
            res += to_string(next);

        }

        if(res.size() == n) {
            if(res[0]==res[res.size()-1]) {
                bool possible = trySwitch(res);
                if (!possible) {
                    cout << "Case #"<<t<<": IMPOSSIBLE"<<endl;
                    continue;
                }
            }
            cout << "Case #"<<t<<": "<<translate(res)<<endl;
        }
        else
            cout << "Case #"<<t<<": IMPOSSIBLE"<<endl;
    }
    /** END ALGORITHM */
}


