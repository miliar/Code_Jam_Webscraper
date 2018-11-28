#include <iostream>
#include <string>
#include <bits/stdc++.h>
using namespace std;

bool isTidy(unsigned long long N){
    if(N<10)
        return true;

    int prev = N%10;
    while(N!=0){
        N/=10;
        if(N%10 > prev)
            return false;
        prev = N%10;
    }
    return true;
}

int main(){
    //freopen("Input.txt", "r", stdin);
    freopen("B-small-attempt0.in", "r", stdin);
    //freopen("B-large.in", "r", stdin);
    freopen("OutputB.txt", "w", stdout);

    int T;
    cin>>T;
    unsigned long long N;
    for(int i=1;i<=T;i++){
        cin>>N;
        while(1){
            if(isTidy(N)){
                cout<<"Case #"<<i<<": "<<N<<endl;
                break;
            }
            N--;
        }
    }
    return 0;
}

