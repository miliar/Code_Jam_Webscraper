//
//  main.cpp
//  A
//
//  Created by Atul Sehgal on 4/7/17.
//  Copyright © 2017 Atul Sehgal. All rights reserved.
//

#include<iostream>
#include<stdio.h>
#include<cmath>
#include<cstring>
#include<stdlib.h>
#include<algorithm>
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

int flips(bool a[], int n, int k) {
    int s[n];
    for(int i=0; i<n; i++)
        s[i] = 0;
    int sum=0, ans=0;
    for(int i=0; i<n; i++) {
        s[i] = (a[i]+sum)%2 != 1;
        sum += s[i] - (i>=k-1?s[i-k+1]:0);
        ans += s[i];
        if(i>n-k and s[i]!=0) return 1000000007;
    }
    return ans;
}

int main(int argc, const char * argv[]) {
    freopen("/Users/atulsehgal/Documents/CodeJam2017/A/input-Alarge.txt","r",stdin);
    freopen("/Users/atulsehgal/Documents/CodeJam2017/A/output-Alarge.txt","w",stdout);
    int T=1,t,n,k,ans;
    cin>>t;
    while(t--)
    {
        string str = "";
        cin>>str>>k;
        n = (int)str.size();
        bool a[n];
        for(int i=0; i<n; i++) {
            if (str[i] == '+') a[i] = 1;
            else a[i] = 0;
        }
        ans = flips(a,n,k);
        printf("Case #%d: ",T++);
        if(ans == 1000000007)
            printf("IMPOSSIBLE\n");
        else
        {
            printf("%d\n",ans);
        }
    }
    return 0;
}
