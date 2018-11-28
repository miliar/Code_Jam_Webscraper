#include<bits/stdc++.h>
using namespace std;
int a[1005][3];
double b[1005];
int main()
{
     //freopen("i.in","r",stdin);
	//freopen("o.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        int d,n;
        scanf("%d %d",&d,&n);
        for(int j=0;j<n;j++)
        {
            scanf("%d %d",&a[j][0],&a[j][1]);
        }
        for(int j=0;j<n;j++)
        {
            b[j]=(double)(d-a[j][0])/a[j][1];
          //  printf("%lf\n",(double)(d-a[i][0])/a[i][1]);
         //   printf("%lf\n",b[i]);
        }
        double ans1=0;
        for(int j=0;j<n;j++)
        {
            if(ans1<b[j])
                ans1=b[j];
          //  printf("%lf\n",b[i]);
        }
      //  printf("%lf\n",ans1);
        double ans;
        ans=d/ans1;
    //    printf("%lf",b[n-1]);
        printf("Case #%d: %.7lf\n",i,ans);
    }
    return 0;
}
