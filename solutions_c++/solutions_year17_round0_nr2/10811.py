//
//  main.cpp
//  TidyNumbers
//
//  Created by YOUQingfei on 4/8/17.
//  Copyright © 2017 YOUQingfei. All rights reserved.
//

#include <iostream>
#include <cmath>
#include <fstream>
#include <vector>
#include <map>

using namespace std;

int main(int argc, const char * argv[]) {
    int T, N, count = 1;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        cin >> N;
        string s = to_string(N), t;
        bool is_tidy = true;
        int len = s.size();
        cout << "Case #" << to_string(count++) << ": ";
        if (len == 1) {
            cout << N;
        } else {
            int i;
            for (i = 0; i < len-1; ++i) {
                if (s[i+1] < s[i]) {
                    is_tidy = false;
                    break;
                }
            }
            
            if (is_tidy) {
                cout << N;
            } else {
                t = s;
                for (int j = i+2; j < len; ++j) {
                    t[j] = '9';
                }
                for (int j = i; i >= 0 && t[i+1] < t[i]; --i) {
                    t[i+1] = '9';
                    t[i]--;
                }
                cout << stol(t);
                
            }
        }
        cout << endl;
    }
    return 0;
}
