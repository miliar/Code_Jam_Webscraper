#include <bits/stdc++.h>

void solve(int ind){
    std::vector<char> N;
    char ch;
    do{
        if(!(std::cin>>std::noskipws>>ch))break;
        if(ch=='\n') break;
        N.push_back(ch);
    }while(ch>='0' && ch<='9');
    char min=N[0];
    for(int i=1;i<N.size();i++){
        if(N[i]<min){
            N[i-1]--;
            for(int j=i;j<N.size();j++)
                N[j]='9';
            for(int j=i-1;j>0;j--){
                if(N[j]<N[j-1]){
                    N[j]='9';
                    N[j-1]--;
                }
                else break;
            }
            break;
        }
        else min=N[i];
    }

    std::cout<<"Case #"<<ind<<": ";
    for(int i=(N[0]=='0'?1:0);i<N.size();i++)
        std::cout<<N[i];
    std::cout<<"\n";
}

int main(){
    int T;
    char ch;
    std::cin>>T;
    std::cin>>std::noskipws>>ch;
    for(int i=0;i<T;i++)
        solve(i+1);
}
