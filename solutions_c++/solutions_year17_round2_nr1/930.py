#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
#define mp make_pair
#define fr first
#define sc second
#define ARRS int(3e5+600)
#define BARRS int(2e6+600)
#define MAX ((long long)(1e17+1))
#define MMAX ((long long)(1e9+10))
#define HS1 ((long long)(1000001329))
#define HS2 ((long long)(1000001531))
#define MOD ((long long)1000000007)
#define SQ 31622780
#define PI 3.14159265358979323846264338327950288419716939937510
#define BG 4294967232ll

ll n,q,p;
pair<ll,ll> a[ARRS];

int main(){
   #ifdef KHOKHO
   freopen("in.in","r",stdin);
   freopen("out.out","w+",stdout);
   #endif //KHOKHO
   cin>>q;
   for(int te=1; te<=q; te++){
      ll d;
      cin>>d>>n;
      for(int i=0; i<n; i++){
         cin>>a[i].fr>>a[i].sc;
      }
      long double t,l,r,m;
      ll c=500;
      l=0;
      r=2e18+100;
      while(c--){
         m=(l+r)/2.0l;
         t=((d+1.0l)/m);
         for(int i=0; i<n; i++){
            if(m>a[i].sc)
            t=min(t,1.0l*a[i].fr/(m-a[i].sc));
         }

         if(t*m<=d){
            r=m;
         } else {
            l=m;
         }
      }
      printf("Case #%d: %.8Lf\n",te,l);
   }
   return 0;
}
