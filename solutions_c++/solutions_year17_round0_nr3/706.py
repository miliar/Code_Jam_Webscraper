#include<bits/stdc++.h>
#define f first
#define s second
using namespace std;
char s[10005];
int main(){
    int t,T=0;;
    scanf("%d",&t);
    while(t--){T++;
        long long int n,k;
        scanf("%lld%lld",&n,&k);
        long long a=n,an=1,b=n-1,bn=0,ans=-1;
        while(true){
            if(k<=an){
                ans=a;
                break;
                }
            else k-=an;
            if(k<=bn){
                ans=b;
                break;
                }
            else k-=bn;
            long long c=a/2,cn=0,d=c-1,dn=0;
            (c==((a-1)/2)?cn:dn)+=an;
            (c==(a-1-(a-1)/2)?cn:dn)+=an;
            (c==((b-1)/2)?cn:dn)+=bn;
            (c==(b-1-(b-1)/2)?cn:dn)+=bn;
            a=c;b=d;
            an=cn;bn=dn;
            }
        ans--;
        printf("Case #%d: %lld %lld\n",T,max(ans/2,ans-ans/2),min(ans/2,ans-ans/2));
        }
    return 0;
    }
