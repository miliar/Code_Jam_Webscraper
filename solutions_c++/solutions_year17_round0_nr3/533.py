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


long long solve(long long n, long long k) {
 //   cout << n << " " << k << endl;
    if(k==1) {
        return n;
    }
    
    if(k%2 == 0) {
        if(n%2 == 0) {
            return solve(n/2, k/2);
        } else {
            return solve((n-1)/2,k/2);
        }
        
    } else {
        if(n%2 == 0) {
            return solve(n/2-1,(k-1)/2);
        } else {
            return solve((n-1)/2,(k-1)/2);
        }
    }
}

vector<long long> sol(long long n, long long k) {
    long long x,y;
    long long divCount = k;//n / (k+1);
    long long spacesRemaining = n - k;
    
    //        if(spacesRemaining <= divCount) {
    if(k*2 > n) {
        x = 0;
        y = 0;
    } else {
        long long spacePerDiv = spacesRemaining / divCount;
        //  if(spacesRemaining%divCount != 0) spacePerDiv++;
        x = spacePerDiv/2;
        y = spacePerDiv/2;
        if(2*(spacePerDiv/2) != spacePerDiv) x++;
    }
    vector<long long> res;
    res.push_back(x);
    res.push_back(y);
    return res;
}

vector<long long> bruteForce(long long n, long long k) {
    long long x,y;
    
    bool stalls[1002] = {0};
    stalls[0] = stalls[n+1] = true;
    
    
    for(int i = 0; i < k; i++) {//for each human
        int pos = -1;
        int curLeft = 0, curRight = 0;
        for(int j = 1; j <= n; j++) { //for each stall
            if(stalls[j]) continue;
            int left = 0,right = 0;
            for(int k = j-1; k >= 1; k--) { //search left/right
                if(!stalls[k]) {
                    left++;
                } else {
                    break;
                }
            }
            
            for(int k = j+1; k <= n; k++) {
                if(!stalls[k]) {
                    right++;
                } else {
                    break;
                }
            }
            
            if(min(left,right) > min(curLeft, curRight)) {
                pos = j;
                curLeft = left;
                curRight = right;
            } else if(min(left,right) == min(curLeft, curRight) &&
                      max(left,right) > max(curLeft, curRight)) {
                pos = j;
                curLeft = left;
                curRight = right;
            } else {
                
            }
        }
        if(i == k-1) {
            x = curLeft;
            y = curRight;
        }
        //        if(i == k-1) {
        //            for(int j = 1; j <= n; j++) {
        //                cout << stalls[j];
        //            }
        //
        //            cout << endl;
        //            stalls[pos] = true;
        //
        //            for(int j = 0; j <= n+1; j++) {
        //                cout << stalls[j];
        //            }
        //            cout << endl;
        //        }
        stalls[pos] = true;
        
    }
    
    vector<long long> res;
    res.push_back(max(x,y));
    res.push_back(min(x,y));
    return res;
}
//500 253
int main(int argc, const char * argv[]) {
    
    ifstream cin ("input.txt");
    ofstream cout ("output.txt");
    
    int t, caseNum = 1;
    long long n, k, x,y;
    
    cin >> t;
    
    
    while(t--) {
        
        cin >> n >> k;
        
//        vector<long long> res = bruteForce(n, k);
//        cout << res[0] << " " << res[1] << endl << endl;
        //x = res[0];
        //y = res[1];
        long long f = solve(n,k);
        if(f%2 == 1) {
            x = (f-1)/2;
            y = x;
        } else {
            x = f/2;
            y = f/2-1;
        }
   //     cout <<f << " ... ";
        
        cout << "Case #"<<caseNum << ": " << x << " " << y << endl;
        caseNum++;
    }
    return 0;
}
