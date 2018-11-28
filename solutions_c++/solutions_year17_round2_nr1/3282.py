#include <bits/stdc++.h>

typedef unsigned long long int ull;
std::pair<int, int> ii;

void solve(int ind){
    ull N, D;
    std::cin>>D>>N;
    ull K[N], S[N];
    for(int i=0;i<N;i++)
        std::cin>>K[i]>>S[i];
    long double T[N];
    long double maxT=0;
    for(int i=0;i<N;i++){
        T[i]=(long double)(D-K[i])/S[i];
        maxT=std::max(maxT, T[i]);
    }
    long double maxS=D/maxT;
    std::cout<<"Case #"<<ind<<": "<<std::fixed<<std::setprecision(6)<<maxS<<"\n";
    return;
}

int main(){
    int T;
    std::cin>>T;
    for(int i=0;i<T;i++)
        solve(i+1);
}
