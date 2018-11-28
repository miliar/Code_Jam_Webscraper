#include <iostream>
#include <iomanip>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <set>
#include <vector>
using namespace std;

long long r[1001],h[1001],a[1001],b[1001];
long long n,k;

long long get(long long st)
{
    long long result=0;

    long long nn=n-st;
    long long i,j;
    for (i=0;i<nn;i++)
    {
        b[i]=a[i+st];
    }

    for (i=nn-1;i>1;i--)
    {
        for (j=1;j<i;j++)
        {
            if (b[j]<b[j+1])
            {
                long long temp = b[j];
                b[j]=b[j+1];
                b[j+1]=temp;
            }
        }
    }

    for (i=0;i<k;i++)
    {
        result += 2*b[i];
    }

    result += r[st]*r[st];
    return result;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("op.txt", "w", stdout);
    long long TTT,TT;

    cin>>TTT;
    for(TT = 1; TT <= TTT; TT++)
    {
        long long i,j;
        cin>>n>>k;
        for (i=0;i<n;i++)
        {
            cin>>r[i]>>h[i];
            a[i]=r[i]*h[i];
        }

        for (i=n-1;i>0;i--)
        {
            for (j=0;j<i;j++)
            {
                if (r[j]<r[j+1]||(r[j]==r[j+1] && h[j]<h[j+1]))
                {
                    long long temp=r[j];
                    r[j]=r[j+1];
                    r[j+1]=temp;
                    temp=h[j];
                    h[j]=h[j+1];
                    h[j+1]=temp;
                    temp=a[j];
                    a[j]=a[j+1];
                    a[j+1]=temp;
                }
            }
        }


        /*for (i=0;i<n-1;i++)
        {
            if (r[i]==r[i+1] && h[i]<h[i+1])
                cout<<"error";
        }*/


        long long result = get(0);
        for (i=0;i<=n-k;i++)
        {
            long long temp = get(i);
            if (temp>result) result=temp;
        }


        cout<<"Case #"<<TT<<": ";
        cout<<fixed<<setprecision(9)<<result*1.0*3.14159265358979323846264<<endl;
    }

    return 0;
}
