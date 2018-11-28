#include<bits/stdc++.h>
using namespace std;
main(){
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int T,t;
    scanf("%d",&T);
    for(t=1;t<=T;t++){
        long long n,k;
        scanf("%lld %lld",&n,&k);
        k--;
        long long a=n,sa=1,b=n-1,sb=0,c=0,sc=0,d=0,sd=0,ans;
        while(1){
            //printf("k=%lld\n%lld %lld\n%lld %lld\n",k,a,sa,b,sb);
            if(a==1){
                ans=1;
                break;
            }
            else if(k<sa+sb){
                if(k<sa)ans=a;
                else ans=b;
                break;
            }
            else{
                k-=sa+sb;
                if(a%2==0){
                    c=(a-1)/2+1;
                    d=(a-1)/2;
                    sc=sa;
                    sd=sa+2*sb;
                    a=c,sa=sc,b=d,sb=sd,c=sc=d=sd=0;
                }
                else{
                    c=(a-1)/2;
                    d=(a-1)/2-1;
                    sc=sb+2*sa;
                    sd=sb;
                    a=c,sa=sc,b=d,sb=sd,c=sc=d=sd=0;
                }
            }
        }
        printf("Case #%d: %lld %lld\n",t,ans/2,(ans-1)/2);
    }
}
