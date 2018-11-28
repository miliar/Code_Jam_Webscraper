/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   CruiseControl.cpp
 * Author: trungthanh
 *
 * Created on April 22, 2017, 11:18 PM
 */

#include <cstdlib>
#include <iostream>
#include <vector>
#include <bits/stl_vector.h>
#include <string.h>
#include <map>
#include <bits/stl_map.h>
using namespace std;


/*
 * 
 */
int main(int argc, char** argv) {
    int T;
    cin >> T;
    std::cout.precision(6);
    for (int t = 0; t< T; t++)
    {
        int D, N;
        cin >> D >> N;
        double timeMax = 0;
        for (int i = 0; i < N; i++)
        {
            int Ki; int Si;
            cin >> Ki >> Si;
            double timeI = (double)(D - Ki)/(double)Si;
            if (timeMax < timeI)
                timeMax = timeI;
        }
        std::cout.setf(std::ios::fixed, std::ios::floatfield);
        std::cout.precision(6);
        cout <<"Case #"<<t+1<<": "<<D/timeMax<<endl;;
    }
    return 0;
}

