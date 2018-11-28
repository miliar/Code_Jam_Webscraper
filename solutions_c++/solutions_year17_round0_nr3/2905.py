//
//  C.cpp
//  
//
//  Created by Kesarwani, Prateek on 4/9/17.
//
//

#include <iostream>
using namespace std;

int func(long long N,long long K){
    long long L=0,R=N+1;
    long long x=K,cur;
    int fl=1;
    while(x){
        if(fl){
            cur = (L+R)/2;
            --x;
        }
        if(x){
            if(x&1){
                L = cur;
                cur = (L+R)/2;
                fl=0;
            }
            else{
                R = cur;
                fl=1;
            }
            x/=2;
        }
    }
    printf("%lld %lld\n",max(cur-L,R-cur)-1,min(cur-L,R-cur)-1);
    return 0;
}

int main(){
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;++t){
        long long N,K;
        scanf("%lld %lld",&N,&K);
        printf("Case #%d: ",t);
        func(N,K);
    }
    return 0;
}
