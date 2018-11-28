//
//  main.cpp
//  oversizedpanflip
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
long long zero,cases,flipper,broken,counter;
pair<long long,long long>emptypair;
vector<long long>emptyvec,solutions;
string pans;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout<<setprecision(10);
    cin>>cases;
    for (int i=0; i<cases; i++) {
        counter=0;
        cin>> pans>>flipper;
        for (int j=0; j<pans.size()-flipper+1; j++) {
            if (pans.at(j)==45) {
                counter++;
                for (int k=0; k<flipper; k++) {
                    pans.at(j+k)=88-pans.at(j+k);
                }
            }
        }
        broken=0;
        for (int j=pans.size()-flipper; j<pans.size(); j++) {
            if (pans.at(j)==45) {
                solutions.push_back(-1);
                broken=1;
                break;
            }
        }
        if (broken==0) {
            solutions.push_back(counter);
        }
    }
    for (int h=0; h<solutions.size(); h++) {
        if (solutions.at(h)==-1) {
            cout<<"case #"<<h+1<<": IMPOSSIBLE\n";
        }
        else{
            cout<<"case #"<<h+1<<": "<<solutions.at(h)<<"\n";
        }
    }
    
    return 0;
}

