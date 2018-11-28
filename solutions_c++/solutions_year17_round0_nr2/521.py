//
//  main.cpp
//  CodeJam
//
//  Created by Vasja Pavlov on 4/8/17.
//  Copyright © 2017 Vasja Pavlov. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cstring>

using namespace std;


bool isTidy(long long x) {
    
    vector<int> digs;
    while(x > 0) {
        digs.push_back(x%10);
        x/=10;
    }
    for(int i = (int)digs.size()-2; i >= 0; i--) {
        if(digs[i] < digs[i+1]) return false;
    }
    return true;
}

long long toInt(vector<int> x) {
    long long res = 0;
    for(int i = 0; i < (int)x.size(); i++) {
        res = res * 10 + x[i];
    }
    return res;
}

long long generateNines(int n) {
    long long res = 0;
    for(int i = 0; i < n; i ++) {
        res = res * 10 + 9;
    }
    return res;
}

vector<int> toVector(long long x) {
    vector<int> res;
    
    while(x > 0) {
        res.push_back(x%10);
        x/=10;
    }
    reverse(res.begin(), res.end());
    return res;
}

int main(int argc, const char * argv[]) {
    
    ifstream cin ("input.txt");
    ofstream cout ("output.txt");
    
    int t, caseNum = 1;
    long long n;
    long long tmp, res = -1;
    cin >> t;
    
    
    while(t--) {
        vector<int> digits;
        
        cin >> n;
        
        bool done = false;

        digits = toVector(n);
        
        
        tmp = 0;
        int digitsCount = (int)digits.size();
        for(int i = 0; i < digitsCount; i++) {
            tmp = tmp * 10 + 1;
        }
        
        if(tmp > n) {
            res = generateNines(digitsCount-1);
            done = true;
        }
        if(!done) {
            
            int cur = (int)digits.size()-1;
            while(!done) {
                
                for(int i = digits[cur] ; i >= 0; i--) {
                    digits[cur] = i;
                    if(isTidy(toInt(digits)) && toInt(digits) <= n) {
                        done = true;
                        res = toInt(digits);
                        break;
                    }
                }
                if(!done) {
                    digits[cur] = 9;
                }
                cur--;
            }
        }
//        cout << toInt(digits) <<" "<< n << endl;
        cout << "Case #"<<caseNum << ": " << res << endl;
        caseNum++;
    }
    return 0;
}
