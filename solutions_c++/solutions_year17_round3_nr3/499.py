#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <vector>
#include<bits/stdc++.h>
using namespace std;
double pi=acos(-1);
int T,n,k;
double have,a[1010];
int main()
{
    scanf("%d",&T);
   freopen("C.out","w",stdout);
    for(int cas=1;cas<=T;cas++){
        scanf("%d %d",&n,&k);
        scanf("%lf",&have);
        for (int i=1;i<=n;i++) scanf("%lf",&a[i]);
        sort(a+1,a+1+n);
       // for (int i=1;i<=n;i++) printf("%.5f ",a[i]);cout<<endl;
        a[n+1]=1.0;
        for (int i=1;i<=n;i++){
            if (i!=n && a[i]==a[i+1]) continue;
            if (have<(a[i+1]-a[i])*i) {
                for (int j=1;j<=i;j++) a[j]+=have/i;
                break;
            }
            else {
                have-=(a[i+1]-a[i])*i;
                for (int j=1;j<=i;j++) a[j]=a[i+1];
            }
          //  for (int l=1;l<=n;l++) printf("%.5f ",a[l]);cout<<endl;
        }
        //for (int i=1;i<=n;i++) printf("%.5f ",a[i]);cout<<endl;
        double ans=1;
        for (int i=1;i<=n;i++) ans*=a[i];
        printf("Case #%d: %f\n",cas,ans);
    }
    return 0;
}
