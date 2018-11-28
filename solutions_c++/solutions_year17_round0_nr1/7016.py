#include<iostream>
#include<cstdio>
#include<cstring>

using namespace std;

int main(){
    long long int T,K,ct;
    string S;
    cin>>T;
    for(long long int a=0;a<T;a++){
    cin>>S>>K;
    ct=0;
    for(long long int i=0;i<=S.length()-K;i++){
        if(S[i]=='-'){
            for(long long int j=i;j<(i+K);j++){
                if(S[j]=='-')
                    S[j]='+';
                else
                    S[j]='-';
            }
            ct++;
        }
    }
    bool flag=true;
    for (long long int i=0;i<S.length();i++){
        if(S[i]=='-')
            flag=false;
    }

    if(flag)
        cout<<"Case #"<<a+1<<": "<<ct<<endl;
    else
        cout<<"Case #"<<a+1<<": "<<"IMPOSSIBLE"<<endl;
    }
    return 0;
}
