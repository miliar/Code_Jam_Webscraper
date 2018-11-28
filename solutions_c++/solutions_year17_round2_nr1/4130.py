#include<bits/stdc++.h>
using namespace std;
int main()
{
   long long int t,z,n,i,j;
    long double ans,b,coun;
    long long int d,k[1001][2],x,y,m,h;

    scanf("%lld",&t);
    for(z=1;z<=t;z++)
    {
        coun=0;
        ans=0;
        scanf("%lld%lld",&d,&n);
        for(i=0;i<n;i++)
        {
            scanf("%lld%lld",&k[i][0],&k[i][1]);
        }

        for(i=0;i<n;i++)
        {
            for(j=i+1;j<n;j++)
            {
                if(k[i][0]>k[j][0])
                {
                    x=k[i][0];
                    y=k[i][1];
                    k[i][0]=k[j][0];
                    k[i][1]=k[j][1];
                    k[j][0]=x;
                    k[j][1]=y;
                }
            }
        }
        m=k[0][0];



        for(i=0;i<n-1;i++)
        {
            y=k[i+1][1]-k[i][1];
            if(y<0)
            {
                x=k[i+1][0]-k[i][0];
                y*=-1;
                b=x/y;

                h=k[i+1][0]+b*k[i+1][1];
                if(h<=d)
                {
                    coun+=b;
                    m=h;
                }
                else
                    break;
            }

            else
            {
                break;
            }
        }

        x=d-m;
        b=(long double)x/k[i][1];

        coun+=b;
       // printf("%lf\n",coun);
        ans=d/coun;

//cout<<"Case "<<z<<": "<<ans<<endl;
       printf("Case #%lld: %llf\n",z,ans);
    }
    return 0;
}
