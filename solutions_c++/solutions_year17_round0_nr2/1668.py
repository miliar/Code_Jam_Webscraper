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
int k;
long long s0,s,ans;
long long  x[N];
bool bong(int n)
{
    for(int i=n;i>=1;i--)if(x[i]!=x[n])
    {
        if(x[i]<x[n])return 1;
        if(x[i]>x[n])return 0;
    }
    return 0;
}

int main()
{
freopen("1.in","r",stdin);
freopen("1.out","w",stdout);
    cin>>tt;
    while(tt--)
    {
        cin>>s0;
        int n=0;
        ans=0;
        long long s=s0;
        while(s)
        {
            x[++n]=s%10;
            s/=10;
        }
        //for(int i=n;i>=1;i--)cout<<x[i];continue;
        for(int i=n;i>=1;i--)
        {
            if(bong(i))
            {
                x[i]--;
                for(int j=i-1;j>=1;j--)x[j]=9;
                break;
            }
        }
        for(int i=n;i>=1;i--)ans=ans*10+x[i];
        cout<<"Case #"<<++cas<<": "<<ans<<endl;
    }
    return 0;
}
