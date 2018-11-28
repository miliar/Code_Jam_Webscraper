#include<bits/stdc++.h>
typedef long long int lli;
using namespace std;

int main()
{
    lli t,k=0;
    cin>>t;
    while(t--)
    {   k++;
        lli d,n,l=0;
        cin>>d>>n;
        lli *d1=new lli[n];
        lli *s1=new lli[n];
        double *t1=new double[n];
        for(lli i=0;i<n;i++)
        {
            cin>>d1[i]>>s1[i];
            t1[i]=(double)(d-d1[i])/(double)s1[i];
        }
        double m,s;
        m=t1[0];
        for(lli i=0;i<n;i++)
        {
            if(m<t1[i])
            {
                m=t1[i];
                l=i;
            }
        }
        s=(double)d/m;
		 printf("Case #%d",k);printf(": ");
		 printf("%6f",s);
		 printf("\n");
    }
    return 0;
}
