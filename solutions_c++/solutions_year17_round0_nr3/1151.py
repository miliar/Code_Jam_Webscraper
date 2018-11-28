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
    myfile.open ("3rdlarge.txt");
    while(t--){
        long long n1,k1;
        cin >> n1 >> k1;
        long long n=n1,k=k1,po=0,m1,m2;
        while(n>0){
            long long power=(long long)pow((long long)2,po);
            long long l=n/power;
            if(k>power){
                k=k-power;
                n=n-power;
                po++;
                continue;
            }
            long long ex=n-(l*power);
            if(ex<k){
                l=l-1;
            }
            if(l%2==0){
                m1=l/2;
                n1=l/2;
            }else{
                m1=(l+1)/2;
                n1=m1-1;
            }
                
           
            break;
        }
        myfile << "Case #";
        myfile << l;
        myfile << ": ";
        myfile << m1;
         myfile << " ";
        myfile << n1;
        myfile << endl;
        l++;
        
    }
    return 0;
}
