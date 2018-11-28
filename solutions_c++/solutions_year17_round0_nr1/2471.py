/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   PancakeFlipper.cpp
 * Author: trungthanh
 *
 * Created on April 9, 2017, 2:03 AM
 */

#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>

using namespace std;
/*
 * 
 */
int main(int argc, char** argv) {
    int T;
    cin >> T;
    
    for (int t = 0; t< T; t++)
    {
        std::string S;
        int K;
        cin >> S >> K;
        int N = S.length();
        int count = 0;
        int i = 0;
        for (i = 0; i <= N-K; i++)
        {
            if (S[i] == '+')
                continue;
            for (int j = i; j< i+K ; j++)
                if (S[j] == '+')
                    S[j] = '-';
                else
                    S[j] = '+';
            count ++;
        }
        bool ok = true;
        for (;i<N;i++)
            if (S[i] != '+')
            {
                ok = false;
                break;
            }
        if (ok)
            cout<<"Case #"<<t+1<<": "<<count<<endl;
        else
            cout<<"Case #"<<t+1<<": IMPOSSIBLE"<<endl;
        
    }
    return 0;
}

