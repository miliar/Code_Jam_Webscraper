#include<stdlib.h>
#include<iostream>
#include<stdio.h>

using namespace std;

int main()
{
    long t,i,j;
    double ans;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        int d,n;
        cin>>d>>n;

        double hor[n][2];
        double time[n];

        for(j=0;j<n;j++)
        {
            cin>>hor[j][0]>>hor[j][1];
        }

        if(n==2 && hor[0][0]<hor[1][0])
        {
            //cout<<"error"<<endl;
            double tmp=hor[0][0];
            hor[0][0]=hor[1][0];
            hor[1][0]=tmp;
            tmp=hor[0][1];
            hor[0][1]=hor[1][1];
            hor[1][1]=tmp;
        }

        for(j=0;j<n;j++)
        {
            double a,b,p,q;
            double x;
            if(j==0)
            {
                q=d;
                b=0;
                p=hor[j][0];
                a=hor[j][1];
                x=0;
            }
            else
            {
                q=hor[j-1][0];
                b=hor[j-1][1];
                p=hor[j][0];
                a=hor[j][1];
                x=0;
            }

            x=(q-p)/(a-b);

            if(j!=0 && (x>time[j-1] || x<0))
            {
                q=d;
                b=0;
                p=hor[j][0];
                a=hor[j][1];

                x=(q-p)/(a-b);
            }
            else if(j!=0)
            {
                x=time[j-1];
            }

            time[j]=x;
        }

        ans=d/time[n-1];
        printf("Case #%d: %.12lf\n",i,ans);
    }
}
