#include <bits/stdc++.h>

using namespace std;

int main(void){
    freopen("testin.txt","r",stdin);
    freopen("testout.txt", "w", stdout);
    int tt;
    long long n,k;
    cin >> tt;
    
    for(int t=1; t<=tt; t++){
        cin >> n;
        cin >> k;
        
        long long nn=k;
        long long m=0;
        while(nn>1){
            nn>>=1;
            m++;
        }
        //printf("%lld %lld %d\n",n,k,m);
        long long parts=1LL<<m;
        long long newn=n+1-parts;
        long long small=newn/parts;
        long long numbig=newn-small*parts;
        long long extrak=k-parts;
        long long finalgap=small;
        if(extrak<numbig) finalgap++;
        //printf("%lld %lld %lld %lld %lld\n",m,parts, newn, extrak, finalgap);
        long long ansmax=finalgap/2;
        long long ansmin=(finalgap-1)/2;
        
        printf("Case #%d: %lld %lld\n", t, ansmax, ansmin);
        
    }
    
    return 0;
}
