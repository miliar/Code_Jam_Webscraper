#include <iostream>
#include <iomanip>
#include <cmath>
#include <stdio.h>
using namespace std;

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int N;
    cin>>N;
    for(int i=1;i<=N;i++)
    {
       long double x=0,n;
        int ctr=0;
        cin>>n;
        if((n/10)==0)
        {
            x=n;
        }
        else
        {
            int a=fmod(n,10),b;
            while(n!=0)
            {
               b=fmod(n,10);
               if(b>a)
               {
                   x=0;
                   for(int i=0;i<ctr;i++)x=x+(9*pow(10,i));
                   b--;
               }

               x=x+(b*pow(10,ctr));
               a=b;
               n=floor(n/10);
                ctr++;

            }
        }
        cout<<setprecision(19)<<"Case #"<<i<<": "<<x<<endl;
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
