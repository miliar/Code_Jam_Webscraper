#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int main(){
    int T;
    cin>>T;
    for(int i=1;i<=T;i++)
    {
        string N;
        cin>>N;
        int x= N.size();
        int j;
        for(j=1;j<x;j++)
        {
            if(N[j]<N[j-1])
            {
                if(N[j-1]=='1')
                {
                    N.empty();
                    N="999999999999999999999999";
                    N.resize(x-1);
                    break;
                }
                N[j-1]-=1;
                for(;j<x;j++)
                    N[j]='9';
            }
        }
        x=N.size();
        for(j=x-1;j>0;j--)
        {
            if(N[j-1]>N[j])
            {
                N[j-1]=N[j];
                N[j]='9';
            }
        }
        cout<<"Case #"<<i<<": "<<N<<endl;
    }
}
