//
//  tiddy_small.cpp
//  xcode 
//
//  Created by BETA on 4/8/17.
//  Copyright © 2017 BETA. All rights reserved.
//

#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
#include <fstream>

#include <climits>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

long solve(long n){
    string str = to_string(n);
    string res = str;
    bool carry = false;
    int last = res.size();
    for(int i=str.size()-1; i>0; i--) {
        int a = str[i] - '0' - carry;
        int b = str[i-1] - '0';
        
        if(a < b) {
            last = i;
            carry = true;
        } else {
            res[i] = a + '0';
            carry = false;
        }
    }
    
    if(carry) res[0] = res[0] - 1;
    for(int i = last; i<res.size(); i++)
        res[i] = '9';

    return stol(res);
}


//    cout<<INT_MAX<<endl;
//    cout<<"123456789990"<<endl;
int main() {
    //cout<< LONG_MAX<<endl;
    int t;
    long n, res;
    ifstream myfile ("/Users/beta/Documents/xcodes/helloworld/helloworld/B-large.txt");
    myfile >> t;  // read t. cin knows that t is an int, so it reads it as such.
    for (int i = 1; i <= t; ++i) {
        myfile >> n ;  // read n and then m.
        res = solve(n);
        cout << "Case #" << i << ": " << res << endl;
    }
    return 0;
}
