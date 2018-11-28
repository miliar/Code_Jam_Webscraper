//
//  main.cpp
//  HackerRank
//
//  Created by Prerna Negi on 3/20/17.
//  Copyright (c) 2017 Rakesh Mahla. All rights reserved.
//

#include <cmath>
#include <cstdio>
#include <vector>
#include <bitset>
#include <iostream>
#include <algorithm>
#include <set>
#include <iostream>
#include <string>
#include <queue>
#include <iomanip>



using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
   
    std::setprecision(6);
    cout.precision(6);
    int T;
    double D;
    double N;
    double K;
    double S;
    double time = 0;

    
    cin>> T;
    
    for(int i =1 ; i<=T;i++){
        cin >> D;
        cin >> N;
        time = 0;

        for (int j = 1; j<=N; j++) {
            cin >> K;
            cin >> S;
            
            double tempTime = ((D-K)/S) ;
            
            if (tempTime > time) {
                time = (D-K)/S;

            }
            
            
        }
        
        double answer = D/time ;
        std::cout << std::fixed;
        cout << "Case #" << i << ": " << D/time << endl;
        
    }
    
    
    
    
    return 0;
}

