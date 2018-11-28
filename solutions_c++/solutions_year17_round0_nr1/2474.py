#include <bits/stdc++.h>

int T, K;

int solve(int ind){
    std::vector<bool> v;
    char ch;
    while(std::cin>>std::noskipws>>ch){
        if(ch=='\n') continue;
        if(ch=='-' || ch=='+'){
            v.push_back(ch=='+');
            continue;
        }
        std::cin>>K;
        int N=v.size();
        int cnt=0;
        for(int i=0;i<=N-K;i++){
            if(!v[i]){
                for(int j=0;j<K && i+j<N;j++)
                    v[i+j]=!v[i+j];
                cnt++;
            }
        }
        bool cool=true;
        for(int i=N-1;i>=N-K+1;i--)
            cool&=v[i];

        std::cout<<"Case #"<<ind<<": ";
        if(cool) std::cout<<cnt<<"\n";
        else std::cout<<"IMPOSSIBLE\n";

        v.clear();
        break;
    }
}

int main(){
    std::cin>>T;
    for(int i=0;i<T;i++)
        solve(i+1);
}
