#include<bits/stdc++.h>
using namespace std;
#define MX 1020

typedef long long int ll;

struct info{
  ll a,b;
}arr[MX+5];

bool cmp(info a,info b)
{
    if(a.a<b.a) return true;
    else return false;
}

int main()
{
    int T,t;
    freopen("A-small-attempt2 (1).in","r",stdin);
    freopen("A-small-attempt2 (1).out","w",stdout);
    scanf("%d",&T);
    for(t = 1; t <= T; t++)
    {
        ll d,n;
        scanf("%lld %lld",&d,&n);
        for(int i = 1; i<=n;i++)
        {
            cin>>arr[i].a>>arr[i].b;
        }
        if(n==1)
        {
            double ans = d - arr[1].a;
            ans /= arr[1].b;
            ans = d / ans;
            printf("Case #%d: %0.8lf\n",t,ans);
            continue;
        }
        sort(arr+1,arr+1+n,cmp);
        if(arr[2].b>=arr[1].b)
        {
            double ans = d - arr[1].a;
            ans /= arr[1].b;
            ans = d / ans;
            printf("Case #%d: %0.8lf\n",t,ans);
        }
        else
        {
              double Time = (arr[2].a - arr[1].a) / (arr[1].b - arr[2].b);
              double v  =  (arr[2].a + arr[2].b * Time);
              //cout<<Time<<" " << v << endl;
              if(arr[2].a + Time * arr[2].b>d)
              {
                     //cout<<"d h u " << endl;
                     double ans = d - arr[1].a;
                     ans /= arr[1].b;
                     ans = d / ans;
                     printf("Case #%d: %0.8lf\n",t,ans);
              }
              else
              {

                   Time = Time + (double)(d-arr[2].a-arr[2].b*Time)/arr[2].b;
                   //cout<<Time<<endl;
                    double ans = d / Time;
                    printf("Case #%d: %0.8lf\n",t,ans);

              }
        }

    }
    return 0;
}
