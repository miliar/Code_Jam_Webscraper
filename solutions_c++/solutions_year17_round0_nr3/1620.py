#include<iostream>
#include<fstream>
#include<vector>
#include<bits/stdc++.h>
using namespace std;
long long int gM(long long int a,long long int b){
    return (a<b)?a:b;
}
long long int gMax(long long int a,long long int b){
    return (a>b)?a:b;
}
void gFEven(long long int lb,long long int ub,long long int &min,long long int &max,long long int &k){
    long long int mid;
    mid=(lb+ub)/2;
    k=k/2;
    if(k == 1){
        min = gM(mid-lb,ub-mid);
        max = gMax(mid-lb,ub-mid);
        return;
    }
    else{
        if(k%2 == 0){
            gFEven(mid+1,ub,min,max,k);
        }
        else{
            gFEven(lb,mid-1,min,max,k);
        }
    }
}
void getForOdd(long long int lb,long long int ub,long long int &min,long long int &max,long long int &k){
    long long int mid;
    mid=(lb+ub)/2;
    k=k/2;
    if(k == 1){
        min = gM(mid-lb,ub-mid);
        max = gMax(mid-lb,ub-mid);
        return;
    }
    else{
        if(k%2 == 0){
            getForOdd(mid+1,ub,min,max,k);
        }
        else{
            getForOdd(lb,mid-1,min,max,k);
        }
    }
}
void getNo(long long int n,long long int k,ofstream &op){
    long long int lb=1,ub=n,min=0,max=0;
    if(n%2 == 1){
        if(k == 1){
            min=n/2;
            max=n/2;
        }
        else if(k%2 == 0){
            getForOdd(1,n/2,min,max,k);
        }
        else{
            getForOdd(((n+1)/2)+1,n,min,max,k);
        }
    }
    else{
        if(k == 1){
            min = n/2-1;
            max = n/2;
        }
        else if(k%2 == 0){
            gFEven(n/2+1,n,min,max,k);
        }
        else{
            gFEven(1,n/2-1,min,max,k);
        }
    }
    op<<max<<" "<<min<<endl;
}
int main(){
    int t,i;
    long long int n,k;
    string str;
    ifstream ip;
    ofstream op;
    ip.open("C-large.in");
    op.open("output3.txt");
    ip>>t;
    for(i=1;i<=t;i++){
        ip>>n>>k;
        op<<"Case #"<<i<<": ";
        getNo(n,k,op);
    }
    return 0;
}

