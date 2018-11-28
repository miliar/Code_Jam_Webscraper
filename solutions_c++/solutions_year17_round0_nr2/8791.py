//
//  main.cpp
//  TidyNumbers
//
//  Created by Ari Jordan on 08.04.17.
//  Copyright © 2017 Ari Jordan. All rights reserved.
//


#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <string>
#include <queue>
#include <cmath>
#include <iomanip>
#include <set>
#include <map>
#include <queue>
#include <stack>
//#include <bits/stdc++.h>
using namespace std;
long long zero,inputamount,number;
pair<long long,long long>emptypair;
vector<long long>emptyvec,numbers;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    //ifstream file_;
    //file_.open("B-small-attempt1.txt");///file reads in inputs from document
    //if(file_.is_open())
    cout<<setprecision(10);
    cin>>inputamount;
    /*if (file_.is_open()) {
        cout<<"open\n";
    }*/
    for (int i=0; i<inputamount; i++) {
        cin>>number;
        int digits= log10(number);
        for (int i=1; i<digits+1; i++) {
            long long p = pow(10,i);
            long long a = (number % p)/(pow(10,(i-1)));
            long long p2= pow(10,i+1);
            long long b = (number%p2)/(pow(10,i));
            if (b>a){
                number -= ((number%(p))+1);
            }
        }
        numbers.push_back(number);
    }
    //file_.close();
    //ofstream file2_("outputB.txt");
    //if(file2_.is_open())
    
        for (int i=0; i<numbers.size(); i++)
            cout <<"case #"<<i+1<<": "<<numbers.at(i)<<"\n";
    
    
    //file2_.close();
    return 0;
}


