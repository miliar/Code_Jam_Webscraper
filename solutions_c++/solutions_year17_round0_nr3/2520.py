/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   BathroomStalls.cpp
 * Author: trungthanh
 *
 * Created on April 8, 2017, 9:12 PM
 */

#include <cstdlib>
#include <iostream>
#include <vector>

#define TMin(X,Y) ((X)>(Y)?Y:X)
using namespace std;

struct TResult{
    long int L;
    long int R;
    
    bool operator == (const TResult& other)
    {
        return L==other.L && R== other.R;
    }
    
    bool operator < (const TResult& other)
    {
        return (L < other.L || (L == other.L && R<other.R) );
    }
};

void calculate(long int N, long int K, TResult& res ){
    if (K == 1)
    {
        res.L = N/2 ;
        res.R = N-1 - res.L;
        return;
    }       
    
    if (K%2 == 1)
    {
        if (N%2 == 0)            
            return calculate( N/2 - 1, K/2  , res);
        else
            return calculate( N/2 , K/2  , res);
    } else {
        if (N%2 == 0)
            return calculate(N/2, K/2, res);
        else
            return calculate(N/2, K/2, res);
                    
    }
    
}

/*
 * 
 */
int main(int argc, char** argv) {
    int T;
    cin >> T;
    
    for (int i = 0; i< T; i++)
    {
        long int N, K;
        cin >> N >> K;
        TResult res;
        calculate(N, K, res);
        cout<<"Case #"<<i+1<<": "<<res.L<<" "<<res.R<<endl;
    }
    
    return 0;
}

