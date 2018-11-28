#include <bits/stdc++.h>
#define ll long long int
#define si1(a) scanf("%d",&a)
#define si2(a,b) scanf("%d%d",&a,&b)
#define si3(a,b,c) scanf("%d%d%d",&a,&b,&c)
#define sil1(a) scanf("%lld",&a)
#define sil2(a,b) scanf("%lld%lld",&a,&b)
#define sil3(a,b,c) scanf("%lld%lld%lld",&a,&b,&c)
#define MOD 1000000007
#define pb push_back
#define mp make_pair
#define pi1(a) printf("%d",a)
#define pi2(a,b) printf("%d%d",a,b)
#define pi3(a,b,c) printf("%d%d%d",a,b,c)
#define pil1(a) printf("%lld",a)
#define pil2(a,b) printf("%lld%lld",a,b)
#define pil3(a,b,c) printf("%lld%lld%lld",a,b,c)
#define dd double
using namespace std;
int main()
{   freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,tt=1;
    si1(t);
    while(t--){
      string s,s1;
      cin>>s;
      int i,j,k,n,ctr=0,ctr1=0;
      si1(k);
      n=s.length();
      for(i=0;i<=n-k;i++){
        if(s[i]=='-'){
           for(j=i;j<i+k;j++){
             if(s[j]=='-'){
                s[j]='+';
             }
             else {
                s[j]='-';
             }
           }
           ctr++;
        }
      }
   for(i=0;i<n;i++){
    if(s[i]=='-'){
        ctr1++;
        break;
    }
   }
   printf("Case #%d: ",tt);
   tt++;
    if(ctr1!=0){
        printf("IMPOSSIBLE");
    }
    else {
        pi1(ctr);
    }
    printf("\n");
    }
    return 0;
}
