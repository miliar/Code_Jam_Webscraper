#include <iostream>
#include <iomanip>
#include <stdio.h>
using namespace std;

int main()
{
    int t;
    cin>>t;

    for(int i=0;i<t;i++)
    {
        double d;
        int n;
        cin>>d>>n;
        double a[n][2];

        for(int j=0;j<n;j++)
        {
            cin>>a[j][0]>>a[j][1];
        }

        double b[n];

        for(int j=0;j<n;j++)
        {
            b[j]=(d-a[j][0])/a[j][1];
        }

        double max1=b[0];

        for(int j=1;j<n;j++)
        {
            if(b[j]>max1)
            {
                max1=b[j];
            }
        }


        d=d/max1;
        printf("Case #%d: %0.6f\n",i+1,d);


    }
    return 0;
}
