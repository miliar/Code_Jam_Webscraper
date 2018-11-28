//
//  main.cpp
//  ProblemA
//
//  Created by Loc Ngo on 4/7/17.
//  Copyright © 2017 Loc Ngo. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;
ifstream fin("/Users/locngo/Desktop/A-large.in");

void process(int t){
    string s;
    fin>>s;
    int k;
    fin>>k;
    int i=0,n=(int)s.length(),nFlips=0;
    bool found = true;
    while(i<n){
        if(s[i]=='-'){
            if(i+k>n){
                found = false;
                break;
            }
            else{
                for(int j=i;j<i+k;j++)
                    s[j] = (s[j]== '-') ? '+' : '-';
                nFlips++;
            }
        }
        i++;
    }
    if(!found)
        cout<<"Case #"<<t<<": IMPOSSIBLE\n";
    else
        cout<<"Case #"<<t<<": "<<nFlips<<endl;
}

int main(int argc, const char * argv[]) {
    // insert code here...
    int T;
    fin>>T;
    for(int i=1;i<=T;i++)
        process(i);
    return 0;
}
