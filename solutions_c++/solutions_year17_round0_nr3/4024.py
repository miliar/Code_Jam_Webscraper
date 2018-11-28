#include<cstdio>
#include<iostream>
using namespace std;
#define ll long long
ll f[100];
ll n,k;
int main()
{
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    int l,T,kase=0;
    scanf("%d",&T);
    f[1]=1;
    for(int i=2;f[i-1]*2<1e18;i++)
        f[i]=f[i-1]*2;
    while(T--){
        cin>>n>>k;
        printf("Case #%d: ",++kase);
        for(l=1;f[l+1]-1<k;l++);
        int mi,mx;
        k-=(f[l]-1);
        if(l>1){
            l--;
            if(n&1)mi=2,mx=0;
            else mi=1,mx=1;
            n=(n-1)/2;
            while(l>1){
                if(n&1){
                    if(mx)mi=mi*2+mx;
                    else mi=mi*2;
                }
                else{
                    if(mx)mx=mx*2+mi;
                    else mx=mi;
                }
                n=(n-1)/2;
                l--;
            }
            if(mx&&k<=mx)cout<<(n+1)/2<<' '<<(n)/2<<endl;
            else cout<<n/2<<' '<<(n-1)/2<<endl;
        }
        else cout<<n/2<<' '<<(n-1)/2<<endl;
    }
    return 0;
}
