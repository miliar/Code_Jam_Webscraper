//
//  main.cpp
//  Bathroom Stalls
//
//  Created by 王越 on 17/4/8.
//  Copyright © 2017年 王越. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <map>

using namespace std;

int main(int argc, const char * argv[]) {
    ofstream cout("/Users/xidui/Documents/xidui/practices/gcj/Bathroom Stalls/Bathroom Stalls/output3.txt");
    ifstream cin("/Users/xidui/Documents/xidui/practices/gcj/Bathroom Stalls/Bathroom Stalls/C-large.in");
    
    int T, t = 0;
    cin >> T;
    while (t++ != T){
        long long N, K;
        cin >> N >> K;
        long long cur = 0;
        map<long long, long long> mll;
        mll[-N] += 1;
        while (mll.size() && mll.begin()->second + cur < K) {
            long long count =  mll.begin()->second;
            cur += count;
            long long gap = mll.begin()->first * -1;
            mll.erase(mll.begin());
            if (gap <= 3) continue;
            if (gap % 2 == 1) {
                mll[gap / -2] += count * 2;
            } else {
                mll[gap / -2] += count;
                mll[gap / -2 + 1] += count;
            }
        }
        long long gap = 0;
        if (mll.size() != 0) gap = mll.begin()->first * -1;
        cout << "Case #" << t << ": " << gap / 2 << " " << (gap - 1) / 2 << endl;
    }
    return 0;
}