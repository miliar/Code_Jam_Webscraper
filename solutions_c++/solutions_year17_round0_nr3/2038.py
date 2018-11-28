#include<iostream>
#include<fstream>
#include<vector>
#include<bits/stdc++.h>
using namespace std;
long long int Min(long long int x,long long int y){
    return (x<y)?x:y;
}
long long int Max(long long int x,long long int y){
    return (x>y)?x:y;
}
void Even(long long int l,long long int u,long long int &min,long long int &max,long long int &p){
    long long int mid;
    mid=(l+u)/2;
    p=p/2;
    if(p == 1){
        min = Min(mid-l,u-mid);
        max = Max(mid-l,u-mid);
        return;
    }
    else{
        if(p%2 == 0){
            Even(mid+1,u,min,max,p);
        }
        else{
            Even(l,mid-1,min,max,p);
        }
    }
}
void Odd(long long int l,long long int u,long long int &min,long long int &max,long long int &p){
    long long int mid;
    mid=(l+u)/2;
    p=p/2;
    if(p == 1){
        min = Min(mid-l,u-mid);
        max = Max(mid-l,u-mid);
        return;
    }
    else{
        if(p%2 == 0){
            Odd(mid+1,u,min,max,p);
        }
        else{
            Odd(l,mid-1,min,max,p);
        }
    }
}
void Numb(long long int n,long long int p,ofstream &op){
    long long int l=1,u=n,min=0,max=0;
    if(n%2 == 1){
        if(p == 1){
            min=n/2;
            max=n/2;
        }
        else if(p%2 == 0){
            Odd(1,n/2,min,max,p);
        }
        else{
            Odd(((n+1)/2)+1,n,min,max,p);
        }
    }
    else{
        if(p == 1){
            min = n/2-1;
            max = n/2;
        }
        else if(p%2 == 0){
            Even(n/2+1,n,min,max,p);
        }
        else{
            Even(1,n/2-1,min,max,p);
        }
    }
    op<<max<<" "<<min<<endl;
}
int main(){
    int temp,i;
    long long int n,p;
    string str;
    ifstream ip;
    ofstream op;
    ip.open("c-large.in");
    op.open("outLarge#3.txt");
    ip>>temp;
    for(i=1;i<=temp;i++){
        ip>>n>>p;
        op<<"Case #"<<i<<": ";
        Numb(n,p,op);
    }
    return 0;
}
