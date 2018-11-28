//
//  2008prob2.cpp
//  
//
//  Created by srikar on 01/04/17.
//
//

#include <stdio.h>
//
//  main.cpp
//  dfd
//
//  Created by srikar on 28/03/17.
//  Copyright © 2017 srikar. All rights reserved.
//

#include <iostream>
#include <string>
#include <queue>
#include <unordered_set>
#include<limits.h>
#include <fstream>
#include <math.h>
#include <iomanip>
using namespace std;

bool isTidy(string &s){
    for(int i=1;i<s.length();i++){
        if(s[i]<s[i-1])
            return false;
    }
    return true;
}

int main() {
    int t;
    cin >> t;
    int l=1;
    ofstream myfile;
    myfile.open ("2ndlarge.txt");
    while(t--){
        int k;
        string s;
        cin >> s;
        for(int i=s.length()-1;i>=1;i--){
            if(s[i]<s[i-1]){
                s[i-1]--;
                for(int j=i;j<s.length();j++)
                    s[j]='9';
                
            }
        }
        string ans="";
        int z=0;
        for(int i=0;i<s.length();i++){
            if(s[i]=='0' && z==0)
                continue;
            z=1;
            ans+=s[i];
        }
        myfile << "Case #";
        myfile << l;
        myfile << ": ";
        myfile << ans;
        myfile << endl;
        l++;
        
    }
    return 0;
}
