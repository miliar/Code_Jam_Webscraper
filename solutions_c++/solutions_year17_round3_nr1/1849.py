#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <iostream>
using namespace std;
const long double pi=acos(-1);

int n,k;

struct cake{
    int id;
    long r;
    long h;
}c[1005];


bool cmp1(cake a,cake b){
    if(a.h*a.r==b.r*b.h){
        return a.r>b.r;
    }else return a.h*a.r>b.r*b.h;
}

bool cmp2(cake a,cake b){
    return a.r*a.r+2*a.r*a.h>b.r*b.r+2*b.r*b.h;
}

int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T;cin>>T;
    int time=0;
    while(T--){
        long long res=0;
        scanf("%d%d",&n,&k);
        for(int i=0;i<n;i++){
            scanf("%lld%lld",&c[i].r,&c[i].h);
            c[i].id=i;
        }
        sort(c,c+n,cmp2);
        int maxx=c[0].id;
        sort(c,c+n,cmp1);
        bool flag=true;
        for(int i=0;i<n;i++){
            int cnt=0;
            long long sum=(long long)(c[i].r*c[i].r+2*c[i].r*c[i].h);
            for(int j=0;j<n;j++){
                if(cnt==k-1) break;
                if(j==i) continue;
                if(c[j].r>c[i].r) continue;
                cnt++;
                sum+=(long long)(c[j].r*c[j].h*2);
            }
            res=max(res,sum);
        }
        long double ans = (long double)res*pi;
        printf("Case #%d: %.6Lf\n",++time,ans);
    }
    return 0;
}
