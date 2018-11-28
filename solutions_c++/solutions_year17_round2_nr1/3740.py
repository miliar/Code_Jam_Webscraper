//
//  main.cpp
//  Problem
//
//  Created by Loc Ngo on 4/22/17.
//  Copyright © 2017 Loc Ngo. All rights reserved.
//

#include <iostream>
#include <algorithm>
#include <fstream>
using namespace std;
ifstream fin("/Users/locngo/Desktop/A-large.in");


void process(int t){
    long double D;
    int N;
    fin>>D>>N;
    long double K[N];
    long double S[N];
    long double R[N];
    long double totalTime = 0;
    
    for(int i=0;i<N;i++)
        fin>>K[i]>>S[i];
    for(int i=0;i<N-1;i++)
        for(int j=i+1;j<N;j++)
            if(K[j]<K[i]){
                swap(K[i],K[j]);
                swap(S[i],S[j]);
            }
    
    for(int i=0;i<N-1;i++)
        R[i] = K[i+1]-K[i];
    R[N-1] = D - K[N-1];
    
    while(N>0){
        long double minTimeInterval = 1000000000;
        int index = -1;
        for(int i=0;i<N-1;i++){
            if(S[i]-S[i+1]>0 && minTimeInterval > R[i]/(S[i]-S[i+1])){
                minTimeInterval = R[i]/(S[i]-S[i+1]);
                index = i;
            }
        }
        if(minTimeInterval > R[N-1]/S[N-1]){
            minTimeInterval = R[N-1]/S[N-1];
            index = N-1;
        }
        if(index == N-1){
            for(int i=0;i<N-1;i++)
                R[i] += (S[i+1]-S[i])*minTimeInterval;
        }
        else{
            for(int i=0;i<N-1;i++)
                R[i] += (S[i+1]-S[i])*minTimeInterval;
            R[N-1] -= S[N-1]*minTimeInterval;
            //remove index
            for(int i=index;i<N-1;i++){
                R[i] = R[i+1];
                S[i] = S[i+1];
            }
        }
        N--;
        totalTime += minTimeInterval;
    }
    printf("Case #%d: %.6Lf\n",t,D/totalTime);
}

int main(int argc, const char * argv[]) {
    // insert code here...
    int T;
    fin>>T;
    for(int i=1;i<=T;i++)
        process(i);
    
    return 0;
}
