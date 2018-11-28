//
//  2008prob2.cpp
//  
//
//  Created by srikar on 01/04/17.
//
//

#include <stdio.h>
#include <iostream>
#include <string>
#include <queue>
#include <unordered_set>
#include<limits.h>
#include <fstream>

#include <iomanip>


using namespace std;
//
//  main.cpp
//  dfd
//
//  Created by srikar on 28/03/17.
//  Copyright © 2017 srikar. All rights reserved.
//

//Lawnmover 2003 prob b
struct horse{
     double r;
     double h;
    
};

int u=1;
void merge(vector<horse> &aVector, int size, int low, int middle, int high){
    horse temp[size];
    for(int i = low; i <= high; i++){
        temp[i] = aVector[i];
    }
    int i = low;
    int j = middle+1;
    int k = low;
    
    while (i <= middle && j <= high){
        if(temp[i].r < temp[j].r|| (temp[i].r == temp[j].r && temp[i].h <= temp[j].h)){
            aVector[k] = temp[i];
            ++i;
        }
        else {
            aVector[k] = temp[j];
            ++j;
        }
        ++k;
    }
    while (i <= middle){
        aVector[k] = temp[i];
        ++k;
        ++i;
    }
}

void mergeSort(vector<horse> &aVector, int size, int low, int high){
    if (low < high){
        int middle = (low + high) / 2;
        mergeSort(aVector, size, low, middle);
        mergeSort(aVector, size, middle+1, high);
        merge(aVector, size, low, middle, high);
    }
}



int main() {
    int t;
    cin >> t;
    int l=1;
    ofstream myfile;
    myfile.open ("1small.txt");
    vector <horse> vec(1003);
    vector <vector <double> > dp;
    for(int i=0;i<=1001;i++){
        vector <double> v(1003);
        dp.push_back(v);
    }
    const double M_P  =3.141592653589793238463;
    while(t--){
        int n,k;
        cin >> n >> k;
        for(int i=0;i<n;i++){
            cin >> vec[i].r;
            cin >> vec[i].h;
        }
         mergeSort(vec,n,0,n-1);
         for(int i=0;i<n;i++){
             dp[i][0]=0;
         }
        for(int i=0;i<n;i++){
            int j;
            
            for(j=1;j<=k;j++){
                if(j>i+1)
                {   dp[i][j]=-100;
                    continue;
                }
                
                if(i+1==j || i==0)
                {
                    
                    if(i!=0)
                        dp[i][j]=dp[i-1][j-1]+2*M_P* vec[i].r*vec[i].h;
                    else
                        dp[i][j]=2*M_P* vec[i].r*vec[i].h;
                    if(j==k)
                        dp[i][j]+=M_P*vec[i].r*vec[i].r;
                    
                    continue;
                }
                else if(j==1){
                    if(k==1)
                        dp[i][j]=max(M_P*vec[i].r*vec[i].r+2*M_P* vec[i].r*vec[i].h,dp[i-1][j]);
                    else
                      dp[i][j]=max(2*M_P* vec[i].r*vec[i].h,dp[i-1][j]);
                
                }
                else if(j==k)
                  dp[i][j]=max(M_P*vec[i].r*vec[i].r+dp[i-1][j-1]+2*M_P* vec[i].r*vec[i].h,dp[i-1][j]);
                else
                  dp[i][j]=max(dp[i-1][j-1]+2*M_P* vec[i].r*vec[i].h,dp[i-1][j]);
            }
        
        }
        myfile << fixed;
        myfile << setprecision(9);
        myfile << "Case #";
        myfile << l;
        myfile << ": ";
        myfile << dp[n-1][k]<<endl;
       
        l++;
        
    }
    return 0;
}
