//
//  A.cpp
//  googlecodejam2017
//
//  Created by Tony Li on 9/4/2017.
//  Copyright © 2017 ZeptoMind Creative Ltd. All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <deque>
#include <stack>
#include <queue>
#include <algorithm>

using namespace std;
typedef long long ll;

const int S_LIMIT = 1000;

int main(){
    int n, k;
    string s;
    cin >> n;
    for (int i=0; i<n; i++) {
        cin >> s >> k;
        int flip = 0;
        for (int j=0; j<s.length(); j ++){
            if (s[j] == '-'){
                if (j+k-1 >= s.length()) {
                    // no solution
                    flip = -1;
                    break;
                }else{
                    flip++;
                    for (int ii=0; ii<k; ii++){
                        s[j+ii] = (s[j+ii] == '-')? '+': '-';
                    }
                }
            }
        }
        if (flip==-1){
            cout << "Case #"<< i+1 <<": IMPOSSIBLE" << endl;
        }else{
            cout << "Case #"<< i+1 <<": "<< flip << endl;
        }
    }
    return 0;
}
