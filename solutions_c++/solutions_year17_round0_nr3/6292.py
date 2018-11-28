/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   bathroom.cpp
 * Author: davidtompul
 *
 * Created on April 9, 2017, 4:06 AM
 */

#include <cstdlib>
#include <cstdio>
#include <queue>

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    
    long long t, n, k;
    scanf("%lld",&t);
    for(long long x=1;x<=t;x++){
        scanf("%lld %lld",&n,&k);
        priority_queue<long long> q;
        q.push(n);
        for(long long i=1;i<k;i++){
            long long cur = q.top();
            q.pop();
            if(cur%2==0){
                cur = cur/2;
                q.push(cur);
                cur-=1;
                q.push(cur);
            }else{
                cur = cur/2;
                q.push(cur);
                q.push(cur);
            }
        }

        n = q.top();
        if(n%2==0){
            n = n/2;
            printf("Case #%lld: %lld %lld\n",x,n,n-1);
        }else{
            n=n/2;
            printf("Case #%lld: %lld %lld\n",x,n,n);
        }
    }
    return 0;
}

