//
//  main.cpp
//  B
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

long long int num(vector<int> a){
    long long int result = 0, ten = 10;
    int n = (int)a.size();
    
    for(int i=0; i<n; i++){
        result = (result * ten) + a[i];
    }
    return result;
}

long long int tidy(vector<int> a){
    int n = (int)a.size();
    for (int i=1; i<n; i++){
        if (a[i] < a[i-1]){
            if(a[i] == 0 && a[i-1] == 1) {
                a[0] = 0;
                for (int j=1;j<n;j++) a[j] = 9;
                break;
            }
            a[i-1] -= 1;
            for (int j=i;j<n;j++){
                a[j] = 9;
            }
            i=0;
        }
    }
    return num(a);
}

bool isTidy(long long int x){
    int prev = x%10;
    int cur = prev;
    while (x) {
        if (cur > prev) return false;
        x/=10;
        prev = cur;
        cur = x%10;
    }
    return true;
}

int main(int argc, const char * argv[]) {
    freopen("/Users/atulsehgal/Documents/CodeJam2017/B/input-Blarge.txt","r",stdin);
    freopen("/Users/atulsehgal/Documents/CodeJam2017/B/output-Blarge.txt","w",stdout);
    int T=1,t;
    long long int n;
    cin>>t;
    while(t--)
    {
        cin>>n;
//        for (long long int i=n;i>=1;i--){
//            if (isTidy(i)){
//                printf("Case #%d: %lld\n",T++,i);
//                break;
//            }
//        }
        vector<int> a;
        while(n){
            a.push_back(n%10);
            n/=10;
        }
        reverse(a.begin(), a.end());
        printf("Case #%d: %lld\n",T++,tidy(a));
    }

    return 0;
}
