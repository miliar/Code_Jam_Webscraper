#include<bits/stdc++.h>
using namespace std;
int main(void){
    //freopen("123.in","r",stdin);
    //freopen("out.out","w",stdout);
    long long n,k,t,ca=1,T,L,R,cnt;
    cin>>T;
    while(T--){
        cin>>n>>k;
        t=1;L=0;R=n;cnt=1;
        while(t<k){
            k-=t;
            n-=t;
            t*=2;
            R=n/t;
			L=n%t;
        }
        if(k<=L) R++;
        if(R&1) printf("Case #%I64d: %I64d %I64d\n",ca++,R/2,R/2);
        else printf("Case #%I64d: %I64d %I64d\n",ca++,R/2,R/2-1);
    }
}
