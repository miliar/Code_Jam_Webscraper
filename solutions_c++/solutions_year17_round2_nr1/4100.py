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
#define pi1(a) printf("%d\n",a)
#define pi2(a,b) printf("%d%d",a,b)
#define pi3(a,b,c) printf("%d%d%d",a,b,c)
#define pil1(a) printf("%lld\n",a)
#define pil2(a,b) printf("%lld%lld",a,b)
#define pil3(a,b,c) printf("%lld%lld%lld",a,b,c)
#define dd double
using namespace std;
int main()
{
   freopen("A-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,tt=1;
    si1(t);
    while(t--)
    {
  double d,n,i,j,k,a,b;
  double di,lo,hi,mid;
  cin>>d>>n;
  vector<pair<double,double> >v;
  for(i=0;i<n;i++){
    cin>>a>>b;
    v.pb(mp(a,b));
  }
 sort(v.begin(),v.end());
 double ma;
for(i=0;i<n;i++){

    double speed=v[i].second;
    double dist=v[i].first;
    double speed1=v[i+1].second;
    double dist1=v[i+1].first;

    if(i==n-1){
       double ti=(d-dist)/speed;
            ma=d/ti;
            break;
    }

    if(speed>speed1){
        double ti=(dist1-dist)/(speed-speed1);
        if(speed1*ti>=d-dist1){
            ti=(d-dist)/speed;
            ma=d/ti;
            break;
        }
        else {
           k=speed*ti;
           ti=k/speed;
           k=d-(dist+speed*ti);
           ti+=(k/speed1);
           ma=d/ti;
           break;
        }
    }
     else {

       double ti=(d-dist)/speed;
            ma=d/ti;
            break;

     }


}
printf("Case #%d: ",tt);
tt++;
cout<< fixed <<setprecision(6)<<ma<<endl;
}






    return 0;
}
