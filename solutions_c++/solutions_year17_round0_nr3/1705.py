#include<iostream>
#include<fstream>
#include<vector>
#include<bits/stdc++.h>
using namespace std;
long long int minimumm(long long int one,long long int two){
    return (one<two)?one:two;
}
long long int maximumm(long long int one,long long int two){
    return (one>two)?one:two;
}
void getForEven(long long int lower,long long int upper,long long int &minimum,long long int &maximum,long long int &k){
    long long int mid;
    mid=(lower+upper)/2;
    k=k/2;
    if(k == 1){
        minimum = minimumm(mid-lower,upper-mid);
        maximum = maximumm(mid-lower,upper-mid);
        return;
    }
    else{
        if(k%2 == 0){
            getForEven(mid+1,upper,minimum,maximum,k);
        }
        else{
            getForEven(lower,mid-1,minimum,maximum,k);
        }
    }
}
void getForOdd(long long int lb,long long int ub,long long int &minimum,long long int &maximum,long long int &k){
    long long int mid;
    mid=(lb+ub)/2;
    k=k/2;
    if(k == 1){
        minimum = minimumm(mid-lb,ub-mid);
        maximum = maximumm(mid-lb,ub-mid);
        return;
    }
    else{
        if(k%2 == 0){
            getForOdd(mid+1,ub,minimum,maximum,k);
        }
        else{
            getForOdd(lb,mid-1,minimum,maximum,k);
        }
    }
}
void getNo(long long int n,long long int k,ofstream &op){
    long long int lb=1,ub=n,minimum=0,maximum=0;
    if(n%2 == 1){
        if(k == 1){
            minimum=n/2;
            maximum=n/2;
        }
        else if(k%2 == 0){
            getForOdd(1,n/2,minimum,maximum,k);
        }
        else{
            getForOdd(((n+1)/2)+1,n,minimum,maximum,k);
        }
    }
    else{
        if(k == 1){
            minimum = n/2-1;
            maximum = n/2;
        }
        else if(k%2 == 0){
            getForEven(n/2+1,n,minimum,maximum,k);
        }
        else{
            getForEven(1,n/2-1,minimum,maximum,k);
        }
    }
    op<<maximum<<" "<<minimum<<endl;
}
int main(){
    int t,i;
    long long int n,k;
    string str;
    ifstream ip;
    ofstream op;
    ip.open("C-large.in");
    op.open("optt.txt");
    ip>>t;
    for(i=1;i<=t;i++){
        ip>>n>>k;
        op<<"Case #"<<i<<": ";
        getNo(n,k,op);
    }
    return 0;
}
