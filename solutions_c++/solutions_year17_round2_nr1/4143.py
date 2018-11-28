#include <bits/stdc++.h>
using namespace std;
int main() 
{
    int t;
    scanf("%d",&t);
    for(int j=1;j<=t;j++)
    {
        long long int i,pos;
        double d,n;
        scanf("%lf %lf",&d,&n);
        double a[1009],b[1009];
        double ans,tim,max=0.0;
        for(i=0;i<n;i++)
        {
            scanf("%lf %lf",&a[i],&b[i]);
             tim=(d-a[i])/b[i];
            if(max<tim)
            {
                max=tim;
                pos=i;
            }
        }
       // cout<<min<<" "<<pos<<" "
        ans=d/max;
        printf("Case #%d: %.6lf\n",j,ans);
        //cout<<setprecision(6)<<ans<<endl;
    }
	// your code goes here
	return 0;
}