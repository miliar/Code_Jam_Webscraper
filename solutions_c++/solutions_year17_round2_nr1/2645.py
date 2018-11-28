#include<iostream>
#include<cstdio>
#include<vector>
#include<map>
#include<string>
#include<algorithm>
#include<queue>
#include <deque>
#include <bits/stdc++.h>
typedef unsigned long long int ulli;
typedef unsigned long int uli;
typedef long long int lli;
typedef long int li;
using namespace std;


int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        ulli d;
        int n;
        scanf("%llu",&d);
        scanf("%d",&n);
        long double max_speed=0;
        for(int j=0;j<n;j++){
			ulli k;
			scanf("%llu",&k);
			int s;scanf("%d",&s);
			long double temp=(long double)((long double)(d-k)/(long double)(s));
			if(temp>max_speed)max_speed=temp;
		}
		
		long double ans=(long double)d/(long double)max_speed;
        printf("Case #%d: %Lf\n",i,ans);
        

    }
return 0;
}
