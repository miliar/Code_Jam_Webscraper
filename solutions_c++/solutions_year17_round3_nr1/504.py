#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <vector>
#include<bits/stdc++.h>
using namespace std;
double pi=acos(-1);
int T,n,k,x,y;
pair<int,int> a[10100];
int cmp1(pair<int,int> a,pair<int,int> b){
    return 1ll*a.first*a.second<1ll*b.first*b.second;
}
int main()
{
    scanf("%d",&T);
   freopen("A.out","w",stdout);
    for(int cas=1;cas<=T;cas++){
        scanf("%d %d",&n,&k);
        for (int i=1;i<=n;i++) {
            scanf("%d %d",&x,&y);
            a[i]=make_pair(x,y);
        }
       // sort(a+1,a+1+n,cmp);
        double ans=0;
        for (int i=n;i>=k;i--){
            sort(a+1,a+1+n);
            double sum=pi*a[i].first*a[i].first;
            sum+=2.0*pi*a[i].first*a[i].second;
            sort(a+1,a+i,cmp1);
            for (int j=i-1;j>=i-k+1;j--)
                sum+=2.0*pi*a[j].first*a[j].second;
            ans=max(ans,sum);
        }
        printf("Case #%d: %.10f\n",cas,ans);
    }
   // cout<<pi<<endl;
    return 0;
}
