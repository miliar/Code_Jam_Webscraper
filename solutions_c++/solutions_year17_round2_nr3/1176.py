#include<bits/stdc++.h>
using namespace std;
#define ll long long

int main()
{   ll t,k;
    scanf("%lld",&t);
    for(k=1;k<=t;k++)
    {   ll n,q,i,j,m;
        vector<double> p;
        scanf("%lld%lld",&n,&q);
        double z[n][3];
        for(i=0;i<n;i++)
        {   scanf("%lf%lf",&z[i][0],&z[i][1]);
            z[i][2]=0;
        }
        for(i=0;i<n;i++)
        {   for(j=0;j<n;j++)
            {   scanf("%lld",&m);
                if(m!=-1)
                    p.push_back(m);
            }
        }
        while(q--)
        {   ll a,b,r=-1;
            double s=0.0,q;
            scanf("%lld%lld",&a,&b);
            for(i=1;i<n;i++)
            {   double min=1e18;
                for(j=0;j<i;j++)
                {   z[j][0]-=p[i-1];
                    if(z[j][0]>=0)
                    {   z[j][2]+=p[i-1]/z[j][1];
                        if(z[j][2]<min)
                            min=z[j][2];
                    }
                    else
                        z[j][2]=-1;
                }
                z[i][2]=min;
            }
            double min=1e18;
            for(i=0;i<n;i++)
                if(z[i][2]<min && z[i][2]>0)
                    min=z[i][2];
            printf("Case %lld: %lf\n",k,min);
        }
    }
    return 0;
}