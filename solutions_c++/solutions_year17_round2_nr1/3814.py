#include <iostream>
#include <string.h>
#include <iomanip>
using namespace std;

int main()
{
    int t;
    long d,n;
    double k[1000],s[1000],max,f;
    freopen("A-large.in","r",stdin);
    cin>>t;
    for(int j = 1 ; j <= t; j++)
    {
        cin>>d>>n;
        
        for(int i = 0 ; i < n ; i++)
        {
            cin>>k[i];
            cin>>s[i];
            k[i]=(d-k[i])/s[i];
        }
        
     /*   for(int i=0;i<n;i++)
        {
            k[i]=(d-k[i])/s[i];
        }*/
        
        max=k[0];
        for(int i=0;i<n;i++)
        {
            if(k[i]>max)
                max=k[i];
        }
        f = d/max;
        //cout<<setprecision(9)<<f<<'\n';
        printf("Case #%d: %.6f\n", j ,f);
    }
    freopen("small.out","w",stdout);
}
