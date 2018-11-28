#include <iostream>
#include <iomanip>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <set>
#include <vector>
using namespace std;

int k[1001];
int s[1001];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("op.txt", "w", stdout);
    long long T,TT;

    cin>>T;
    for(TT = 1; TT <= T; TT++)
    {
        int d,n;
        cin>>d>>n;
        int i,j;
        for (i=0;i<n;i++)
        {
            cin>>k[i]>>s[i];
        }

        for (i=n-1;i>0;i--)
        {
            for (j=0;j<i;j++)
            {
                if (k[j]>k[j+1])
                {
                    int temp=k[j+1];
                    k[j+1]=k[j];
                    k[j]=temp;

                    temp=s[j+1];
                    s[j+1]=s[j];
                    s[j]=temp;
                }
            }
        }

        double result = d*1.0/((d-k[0])*1.0/(s[0]*1.0));
        int s0=s[0];
        for (i=0;i<n;i++)
        {
            if (i!=0 && s[i]>=s0) continue;
            s0=s[i];

            if (result>d*1.0/((d-k[i])*1.0/(s[i]*1.0)))
                result=d*1.0/((d-k[i])*1.0/(s[i]*1.0));
        }



        cout<<"Case #"<<TT<<": ";
        cout<<fixed<<setprecision(6)<<result<<endl;
    }

    return 0;
}
