#include<bits/stdc++.h>
using namespace std;
long long p[20],q[20],a[20];
int main(){
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int t,i,j,k;
    long long n,z;
    p[18]=1;
    q[18]=1;
    for(i=17;i>0;--i){
        p[i]=p[i+1]*10;
        q[i]=p[i]+q[i+1];
    }
    cin>>t;
    for(k=1;k<=t;++k){
        cin>>n;
        printf("Case #%d: ",k);
        if(n==10*p[18]) --n;
        z=n;
        for(i=18;i>0;--i) a[i]=z%10,z/=10;
        z=0;
        for(i=1;i<=18;++i){
            for(j=9;j>=0;--j)
                if(z+j*q[i]<=n){
                    z+=j*p[i];
                    break;
                }
        }
        printf("%I64d\n",z);
    }
}
