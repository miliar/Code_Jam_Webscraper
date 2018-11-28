#include <bits/stdc++.h>

typedef long long int ull;
typedef std::pair<ull, ull> l2;

void solve(int ind){
    ull N, K;
    std::cin>>N>>K;
    std::map<ull, ull> S;
    S[-N]=1;
    while(!S.empty()){
        l2 cur=*S.begin();
        S.erase(S.begin());
        cur.first*=-1;
        K-=cur.second;
        ull a, b;
        if(cur.first%2==0){
            a=cur.first/2;
            b=a-1;
        }
        else a=b=(cur.first-1)/2;
        if(K<=0){
            std::cout<<"Case #"<<ind<<": "<<a<<" "<<b<<"\n";
            break;
        }
        S[-a]+=cur.second;
        S[-b]+=cur.second;
    }
}

int main(){
    int T;
    std::cin>>T;
    for(int i=0;i<T;i++)
        solve(i+1);
}
