#include<bits/stdc++.h>
using namespace std;

int main()
{
    int test=0,testcase,i,j,k,n,m;
    int h[1111][4];
    double hh[1111];
    cin>>testcase;


    while(test++ < testcase)
    {
        cin>>m>>n;
        for(i=1;i<=n;i++)cin>>h[i][0]>>h[i][1];

        for(i=1;i<=n;i++)
        {
            hh[i]=m-h[i][0];
            hh[i]/=h[i][1];
        }
        for(i=n;i>1;i--)
        {
            if(hh[i]>hh[i-1])hh[i-1]=hh[i];
        }
        double result = hh[1];

        result = m / result;

        printf("Case #%d: %.8lf\n",test,result);
        //cout<<result<<endl;
    }

    return 0;
}
