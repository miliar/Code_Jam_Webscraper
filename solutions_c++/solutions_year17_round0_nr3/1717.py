//
//  main.cpp
//  tmp
//
//  Created by 金航宇 on 2017/4/8.

//  Copyright © 2017年 金航宇. All rights reserved.
// 123454334
// 123449999

#include <iostream>
#include<cstring>
#define N 2000
using namespace std;

int cas=0,tt;
long long n,k,a1,a2,m;
long long work(long long n,long long k)
{
    if(k==1)return n;
    if(n%2==1)return work(n/2,k/2);
    //n/2,(n-1)/2///1000 500 499
    if(n%2==0)
    {
        if(k%2==0)return work(n/2,k/2);
        else return work(n/2-1,k/2);
    }
    return n;
}
int main()
{
freopen("1.in","r",stdin);
freopen("1.out","w",stdout);
    cin>>tt;
    while(tt--)
    {
        cin>>n>>k;
         m=work(n,k);
        cout<<"Case #"<<++cas<<": "<<m/2<<" "<<(m-1)/2<<endl;
    }
    return 0;
}
