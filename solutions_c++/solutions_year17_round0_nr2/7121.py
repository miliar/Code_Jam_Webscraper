#include <cmath> 
#include <cstdio>
#include <vector> 
#include <iostream>
#include <algorithm>
using namespace std;
long long int n;
long long int check(long long int c){
    long long int d=c%10,m=c; 
    c=c/10;
    long long int sum=d,i=0;
    while(c>0){
        if((c%10)<=d){
            d=c%10;
            c=c/10;
            i++;
        } 
        else{
            long long int p=pow(10,i+1);
            sum=m%p;
            n=n-sum-1;
            return 0;
        }
    } 
    return 1;
}
int main(){
    int t;
    cin>>t;
    int i=1;
    while(i<=t){
        cin>>n;
        while(n){
            if(check(n))
                break;
        }
        cout<<"Case #"<<i<<": "<<n<<"\n"; i++; 
    }
}
