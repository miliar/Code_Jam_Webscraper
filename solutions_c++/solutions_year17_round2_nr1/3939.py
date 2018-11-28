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
#include <unordered_map>
#include<limits.h>
#include <fstream>
#include <iomanip>
using namespace std;
struct horse{
    double k;
    double s;

};
bool comp(horse a,horse b){
    return a.k<=b.k;
}
int main() {
    int t;
    cin >> t;
    int l=1;
    ofstream myfile;
    myfile.open ("1stsmall.txt");
    vector <horse> vec(1000);
    while(t--){
        double d;
        int n;
        cin >> d >> n;
        int i=0;
        while(i<n){
            cin >> vec[i].k >> vec[i].s;
            i++;
        }
        sort(vec.begin(),vec.begin()+n,comp);
        int curd=vec[n-1].k,cursp=vec[n-1].s;
        for(int i=n-2;i>=0;i--){
            if(cursp>=vec[i].s)
            {
                cursp=vec[i].s;
                curd=vec[i].k;
                continue;
            }else{
                double r=(d-curd)/cursp;
                double g=(d-vec[i].k)/vec[i].s;
                if(r<g){
                    cursp=vec[i].s;
                    curd=vec[i].k;
                }
            
            }
        
        }
        double tim=(d-curd)/cursp;
        double speed=d/tim;
        
        myfile << std::fixed;
        myfile<< std::setprecision(6);
        myfile << "Case #";
        myfile << l;
        myfile << ": ";
        myfile << speed<< endl;
        l++;
        
    }
    return 0;
}
