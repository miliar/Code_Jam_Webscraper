#include <cmath> 
#include <cstdio>
#include <vector> 
#include <iostream>
#include <algorithm>
using namespace std;
long long int num;
long long int check(long long int c){
    long long int d=c%10,m=c; 
    c=c/10;
    long long int s=d,i=0;
    while(c>0){
        if((c%10)<=d){
            d=c%10;
            c=c/10;
            i++;
        } 
        else{
            long long int p=pow(10,i+1);
            s=m%p;
            num=num-s-1;
            return 0;
        }
    } 
    return 1;
}
int main(){
    int t;
    cin>>t;
    int i=1,f=0;
    while(i<=t){
        cin>>num;
        f=0;
        while(num){
            if(check(num))
                f=1;
            if(f==1)
                break;
        }
        cout<<"Case #"<<i<<": "<<num<<"\n"; i++; 
    }
}