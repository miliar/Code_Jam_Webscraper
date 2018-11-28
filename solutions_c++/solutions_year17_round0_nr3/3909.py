//
//  main.cpp
//  C
//
//  Created by Atul Sehgal on 4/8/17.
//  Copyright © 2017 Atul Sehgal. All rights reserved.
//

#include<iostream>
#include<stdio.h>
#include<cmath>
#include<cstring>
#include<stdlib.h>
#include<algorithm>
#include<vector>
#include<limits.h>
#include <queue>
using namespace std;

/*printing definitions*/
#define pi(x) printf("%d\n",(x))
#define pii(x,y) printf("%d %d\n",(x),(y))
#define pl(x) printf("%lld\n",(x))
#define pll(x,y) printf("%lld %lld\n",(x),(y))
#define pil(x,y) printf("%d %lld\n",(x),(y))
#define pli(x,y) printf("%lld %d\n",(x),(y))
#define plf(x) printf("%lf\n",(x))
#define plflf(x,y) printf("%lf %lf\n",(x),(y))

/*scanning definitions*/
#define si(x) scanf("%d",&x)
#define sii(x,y) scanf("%d %d",&x,&y)
#define sl(x) scanf("%lld",&x)
#define sll(x,y) scanf("%lld %lld",&x,&y)
#define sil(x,y) scanf("%d %lld",&x,&y)
#define sli(x,y) scanf("%lld %d",&x,&y)
#define slf(x) scanf("%lf",&x)
#define slflf(x,y) scanf("%lf %lf",&x,&y)

pair<long long int, long long int> solve(long long int b, long long int e, long long int k) {
    pair<long long int, long long int> pr,p;
    if (k==1){
        //p =make_pair(b,e);
        //cout<<p.first<<" "<<p.second<<endl;
        return make_pair(b,e);
    }
    pr = solve(b,e,k/2);
    long long int mid = pr.first + (pr.second - pr.first)/2;
    if (k&1){
        //p =make_pair(mid+1,pr.second);
        //cout<<p.first<<" "<<p.second<<endl;
        return make_pair(mid,pr.second);
    }
    //p =make_pair(pr.first,mid-1);
    //cout<<p.first<<" "<<p.second<<endl;
    return make_pair(pr.first,mid);
}




int main(int argc, const char * argv[]) {
    freopen("/Users/atulsehgal/Documents/CodeJam2017/C/input-Csmall2.txt","r",stdin);
    freopen("/Users/atulsehgal/Documents/CodeJam2017/C/output-Csmall2.txt","w",stdout);
    int T = 1, t;
    long long int n,k,y,z;
    cin>>t;
    while(t--)
    {
        cin>>n>>k;
        pair<long long int, long long int> p;
        //p = solve(0,n+1,k);
        priority_queue< long long int > Q;
        
        Q.push(n);
        while (k-- && Q.empty() == false)
        {
            long long int tp = Q.top();
            if (tp&1){
                y = z = tp/2;
            }
            else{
                y = tp/2;
                z = (tp-1)/2;
            }
            Q.pop();
            Q.push(y);
            Q.push(z);
        }
        /*
        long long int diff = (p.second-1) - (p.first+1);
        z = diff/2;
        y = diff - z;*/
        printf("Case #%d: %lld %lld\n",T++,y,z);
    }

    return 0;
}
