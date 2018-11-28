//
//  main.cpp
//  test1
//
//  Created by Lingsong Zeng on 3/2/17.
//  Copyright © 2017 Lingsong Zeng. All rights reserved.
//




#include<set>
#include<map>
#include<cmath>
#include<queue>
#include<stack>
#include<cstdio>
#include<string>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;
int main(){
    int t,cas=0;
    cin>>t;
    while(t--){
        printf("Case #%d: ",++cas);
        long long n,k;
        cin>>n>>k;
        long long cnt=1,now=0;
        while(now+cnt<k){
            now+=cnt;
            n-=cnt;
            cnt*=2;
        }
        k-=now;
        long long tmp=n/cnt;
        long long num=n%cnt;
        if(k<=num)
            tmp++;
        tmp--;
        cout<<tmp/2+tmp%2<<" "<<tmp/2<<endl;
    }
}