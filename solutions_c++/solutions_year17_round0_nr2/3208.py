#include <stdio.h>
#include <bits/stdc++.h>

#include <string.h>
#include <math.h>
#include <stdlib.h>

using namespace std;


long long int Tidy(long long int num){
    if(num<10){return num;}
    vector<unsigned long long int> arr;
    while(num>0){
        arr.push_back(num%10);
        num=num/10;
    }
    reverse(arr.begin(), arr.end());
    
    while(true){
        int n0=0;
        int max=arr[0];
        for(unsigned long long int i=1;i<=arr.size()-1;i++){
            
            if(n0)arr[i]=9;
            else if(arr[i]==0 ){
                arr[i]=9;
                n0=1;   
                arr[i-1]-=1;
            }
            else{
                if(arr[i]>=max)max=arr[i];
                else{
                    arr[i]=9;
                    arr[i-1]-=1;
                    n0=1;
                    
                }
            }
        }
        if(!n0) break;
    }
    long long int sum=0;
    for(unsigned long long int i=0;i<arr.size();i++){
        sum=10*sum + arr[i];
    }
    return sum;
}
int main() {
    int t;cin>>t;
    int testcase=1;
    
    while(t--){
        unsigned long long int n;
        cin>>n;
        unsigned long long int num=n;
        unsigned long long int ans=0;
        
        cout<<"Case #"<<testcase++<<": "<<Tidy(n)<<endl;
        
    }
    return 0;
}
