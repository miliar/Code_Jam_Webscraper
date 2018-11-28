/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: bernardo
 *
 * Created on April 15, 2017, 2:38 AM
 */

#include <cstdlib>
#include <unordered_set>
#include <set>
#include <unordered_map>
#include <map>
#include <list>
#include <vector>
#include <cmath>
#include <string>
#include <iostream>
#include <string>
#include <cstdlib>
#include <algorithm>

using namespace std;

/*
 * 
 */

bool AreDoubleSame(double dFirstVal, double dSecondVal)
{
    return std::fabs(dFirstVal - dSecondVal) < 1E-6;
}

int main(int argc, char** argv) {
    int T;
    cin>>T;
    cout.precision(20);
    for (int t = 0; t < T; t++) {
        int N;
        cin>>N;
        int K;
        cin>>K;
        double U;
        cin>>U;
        vector<double> P(N);
        for(int i=0;i<N;i++) {
            cin>>P[i];
        }
        double missingToOne = 0;
        for(int i=0;i<N;i++) {
            missingToOne+= 1 - P[i];
        }
        if(missingToOne <= U || AreDoubleSame(missingToOne,U)) {
            cout << "Case #" << t + 1 << ": 1.000000" << endl;
            continue;
        }
        sort(P.begin(), P.end());
        P.push_back(1);
        while(!AreDoubleSame(0,U)) {
            
            for(int i=1;i<N+1;i++) {
                if(!AreDoubleSame(P[i],P[i-1])) {
                    //i is different, distrubute from 0 to i-1, subtract and continue
                    double toBecomeI = (P[i]-P[i-1])*i;
                    if(toBecomeI<= U || AreDoubleSame(0,U)) {
                        for(int j=0;j<i;j++) {
                            P[j]=P[i];
                        }
                        U-=toBecomeI;
                    } else {
                        for(int j=0;j<i;j++) {
                            P[j]+=U/i;
                        }
                        U=0;
                    }
                    
                    break;
                }
            }
        }
        double result = 1;
        for(int i=0;i<N;i++) {
            result*=P[i];
        }
        
        cout << "Case #" << t + 1 << ": " <<result<< endl;
    }
    return 0;
}

