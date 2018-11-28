//
//  main.cpp
//  q3
//
//  Created by Ken-Hao Liu on 09/04/2017.
//  Copyright © 2017 Ken-Hao Liu. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;

typedef long long ll;
class Solution{
public:
    vector<ll> solve(ll N, ll K){
        vector<ll>result(2);
        bool isOdd=N%2;
        ll c=isOdd,d=!isOdd,e=1,cur=K,width=N;
        while(cur){
//            printf("cur c d e width %lld %lld %lld %lld %lld\n",cur,c,d,e,width);
            if(cur<=e){
//                printf("w %lld\n",width);
                if(width%2){
                    if(cur<=c)result[0]=result[1]=width/2;
                    else result[0]=width/2,result[1]=width/2-1;
                }
                else{
                   if(cur<=d)result[0]=width/2,result[1]=width/2-1;
                   else result[0]=result[1]=width/2-1;
                }
                break;
            }
            else{
                cur-=e,e*=2;
                ll w1=width-1,w2=width,on,en,c1=d,d1=d;
                if(w1%2)on=w1,en=w2;
                else on=w2,en=w1;
                if((on/2)%2)c1+=2*c;
                else if(on>1)d1+=2*c;
                if((en/2)==1)d1-=d;
                c=c1,d=d1;
                width/=2;
            }
            
        }
        return result;
    }
};
int main(int argc, const char * argv[]) {
    int t;
    ll N,K;
    cin>>t;
    for(int i=0;i<t;i++){
        cin>>N>>K;
        Solution sol;
        vector<ll>result=sol.solve(N,K);
        printf("Case #%d: %lld %lld\n",i+1,result[0],result[1]);
    }
    return 0;
}
