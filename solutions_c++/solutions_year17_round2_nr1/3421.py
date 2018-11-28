#include <iostream>
using namespace std;

//Google CodeJam 1B Problem 2 by :
//*******************_ LBSREX _*******************

int main()
{
	int test;
    cin>>test;
    for(int t=1;t<=test;t++)
    {
        float maxt;
        int d,n;
        cin>>d>>n;
        for(int i=0;i<n;i++)
        {
            int p,s;
            cin>>p>>s;
            if(i==0)
            {
                maxt=(float)(d-p)/(float)(s);
            }
            else
            {
                float m=(float)(d-p)/(float)(s);
                maxt=((m>maxt)?m:maxt);
            }
        }
        printf("Case #%d: %0.6f\n",t,float(d)/maxt);
    }
	return 0;
}
