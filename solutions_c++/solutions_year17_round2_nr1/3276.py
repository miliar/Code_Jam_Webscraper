/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: hanv2
 *
 * Created on April 22, 2017, 11:01 PM
 */

#include <cstdlib>
#include <iostream>
#include <sstream>
#include <math.h>
#include <vector>
#include <queue>
//#include <queue>

using namespace std;

/*
 * 
 */
double solve();
double solve_bf();

int main(int argc, char** argv) {
    int t;
    cin >> t;
//    cout << "\nt: "<<t<<"\n";
    for (int i = 1;i <= t;++i){
        
        //solve
        double result = solve();
        
        //print result 
//        cout << "Case #" << i << ": " <<  result << "\n";
        printf("Case #%d: %.6f\n",i,result);
        //double check by brute force
//        int result1 = solve_bf(inp);        
//        if (result == result1){
//            cout << "Check case #" << i << ":OK\n";
//        } else {
//            cout << "Check case #" << i << ":ERRRRR\n";
//            cout << "Case #" << i << ":" <<  result1 << "(brute force)\n";
//        }
    }
    
    return 0;
}
double solve(){
    unsigned long long D;        
    int N;
    cin >> D >> N;
    priority_queue<double> times;
    for (int i = 0; i < N; ++i){            
        unsigned long long Ki;
        int Si;

        cin >> Ki >> Si;
        
        double Ti = ((double)(D-Ki))/Si;
        
//        cout << "\ndistance: "<<D-Ki<<"\n";
//        cout << "\nspeed: "<<Si<<"\n";
//        cout << "\ntime: "<<Ti<<"\n";
        times.push(Ti);
    }
    //debug input
//        cout << "\ninput: "<<inp<<"\n";

    double longest = times.top();
    return (double)D / longest;
}
double solve_bf(){
    return 1.1;
}

