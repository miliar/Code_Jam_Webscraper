#include <bits/stdc++.h>
using namespace std;

inline void in(int &n){scanf("%d",&n);}

int T;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    in(T);
    for(int t=1;t<=T;++t){
        printf("Case #%d: ",t);
        int D,N;
        double tp=0;
        in(D);in(N);
        for(int i=0,K,S;i<N;++i){
            cin>>K>>S;
            tp=max(tp,(double)(D-K)/S);
        }
        cout<<setprecision(6)<<fixed<<(double)D/tp<<endl;
    }
}
