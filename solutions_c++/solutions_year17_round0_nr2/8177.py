//
//  B.cpp
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
#include <sstream>

using namespace std;
typedef long long ll;

int main(){
    int n;
    ll k;
    cin >> n;
    for (int i=0; i<n; i++){
        cin >> k;
        string s = to_string(k);
        int j=0;
        vector<int> res;
        stack<int> res_stack = stack<int>();
        
        for (; j < s.length(); j++){
            int cur = s[j] - '0';
            if (j==s.length()-1) {
                res_stack.push(cur);
                break;
            }
            int next = s[j+1] - '0';
            if (cur > next) {
                for (int ii=j+1; ii<s.length();ii++){
                    res.push_back(9);
                }
                res_stack.push(cur-1);
                break;
            }else{
                res_stack.push(cur);
            }
        }
        while (!res_stack.empty()) {
            int t = res_stack.top(); res_stack.pop();
            if (!res_stack.empty() && t< res_stack.top()){
                res.push_back(9);
                t = res_stack.top()-1;
                res_stack.pop();
                res_stack.push(t);
            }else if(t != 0){
                res.push_back(t);
            }
        }
        
        if (s.length() == 1){
            cout << "Case #"<< i+1 <<": "<< s << endl;
        }else{
            std::stringstream ss;
            for(int ii = res.size()-1; ii >-1 ; --ii)
            {
                ss << res[ii];
            }
            std::string s = ss.str();
            
            cout << "Case #"<< i+1 <<": "<< s << endl;
        }
        
    }
    
    return 0;
}
