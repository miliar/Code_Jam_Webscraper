#include<bits/stdc++.h>
using namespace std;
int main()
{
 
    int t,r=1;;
    cin>>t;
    while(r<=t)
    {
        long long int n,k,a;
        double m,min1=0.0,b;
        cin>>n>>k;
        for(int i=0;i<k;i++)
        {
            cin>>a>>b;
            m=(n-a)/b;
            if(i!=0)
            {
             if(m>min1)
             {
              min1=m;
             }
            }
 
            else
            min1=m;
        }
        min1=n/min1;
        cout<<"Case #"<<r<<": ";
            printf("%.6f",min1);
            printf("\n");
            r++;
    }
}