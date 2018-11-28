//
//  main.cpp
//  TidyNumbers
//
//  Created by Tab on 07/04/2017.
//  Copyright © 2017 Tab. All rights reserved.
//

#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
bool isTidy(string & num){
    bool ret = true;
    for (int i=1; i<num.length(); ++i) {
        if (num[i-1]>num[i]) {
            ret = false;
        }
    }
    return ret;
}
const string getLastTidyNum(string& lastNum) {
    if (lastNum.length()==1) {
        return lastNum;
    }
    string digits = lastNum;
    
    while (!isTidy(digits)) {
        for (int i=1; i<lastNum.length(); ++i) {
            char prev = lastNum[i-1];
            char current = lastNum[i];
            if (prev>current) {
                digits[i-1] = prev-1;
            }
        }
        bool flag = false;
        for (int i=0; i<lastNum.length(); ++i) {
            if (flag) {
                digits[i] = '9';
            }else if (digits[i]<lastNum[i]){
                flag = true;
            }
        }
        lastNum = digits;
    }
    return digits;
}
int main() {
    int t;
    string n;
    cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
    for (int i = 1; i <= t; ++i) {
        cin >> n;  // read n and then m.
        long long lastTidyNum = stoll(getLastTidyNum(n));
        cout << "Case #" << i << ": " <<lastTidyNum<< endl;
        // cout knows that n + m and n * m are ints, and prints them accordingly.
        // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
    }
}

