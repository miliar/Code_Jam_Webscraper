#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,n,m,i,cse=1;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d",&n,&m);
        double k;
        scanf("%lf",&k);
        double a[n];
        for(i=0;i<n;i++)
            scanf("%lf",&a[i]);
        double sum=0;
        for(i=0;i<n;i++)
        {
            sum+=1-a[i];
        }
        int j;
        if(sum<=k)
        {
            printf("Case #%d: 1.000000\n",cse);
        }
        else
        {
            sort(a,a+n);
            int c=1;
            for(i=1;i<n;i++)
            {
                if(k<c*(a[i]-a[i-1]))
                {
                    for(j=0;j<=i-1&&a[j]<=1.0000;j++)
                    {
                        a[j]+=k/((double)(i));
                    }
                    k=-1;
                    break;
                }
                k-=c*(a[i]-a[i-1]);
                for(j=0;j<=i-1;j++)
                    {
                        a[j]=a[i];
                    }
                    c++;
            }
            if(k>0)
            {
                for(i=0;i<n;i++)
                {

                    double y=k/((double)n);
                    if(a[i]+y<=1.00)
                        a[i]+=y;
                    else
                        break;
                }
            }
            double ans=1;
            for(i=0;i<n;i++)
                ans=ans*a[i];
            printf("Case #%d: %lf\n",cse,ans);
        }
        cse++;
    }
    return 0;
}
