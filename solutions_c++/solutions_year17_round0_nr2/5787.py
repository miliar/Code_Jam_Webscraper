//
//  main.cpp
//  ProblemB
//
//  Created by Loc Ngo on 4/7/17.
//  Copyright © 2017 Loc Ngo. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;
ifstream fin("/Users/locngo/Desktop/B-large.in");

void process(int t){
    string s;
    fin>>s;
    int k = 0;
    for(int i=1;i<s.length();i++)
        if(s[i]<s[i-1]){
            k = i-1;
            s[i-1]--;
            for(int j=i;j<s.length();j++)
                s[j] = '9';
            break;
        }
    for(int i=k-1;i>=0;i--)
        if(s[i] > s[i+1]){
            s[i+1] = '9';
            s[i]--;
        }
    if(s[0]=='0')
        s = s.substr(1);
    cout<<"Case #"<<t<<": "<<s<<endl;
}

int main(int argc, const char * argv[]) {
    // insert code here...
    int T;
    fin>>T;
    for(int i=1;i<=T;i++)
        process(i);
    return 0;
}
