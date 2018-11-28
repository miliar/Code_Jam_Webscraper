#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("B-large.in");
ofstream fout("output.out");

int main()
{
    int t,k;
    fin>>t;

    for(k=1; k<=t; k++)
    {
        unsigned long long n,rez=0;
        fin>>n;

        int cifri[19];
        int i,l=0,j;
        for(i=0; i<19; i++)
            cifri[i]=0;

        unsigned long long tmp=n;
        while(tmp>0)
        {
            cifri[l]=tmp%10;
            tmp/=10;
            l++;
        }

        for(i=l-1; i>0; i--)
        {
            if(cifri[i]>cifri[i-1])
            {
                cifri[i]--;
                for(j=i-1; j>=0; j--)
                    cifri[j]=9;

                for(j=i; j<l-1; j++)
                {
                    if(cifri[j]<cifri[j+1])
                    {
                        cifri[j]=9;
                        cifri[j+1]--;
                    }
                }
            }
        }

        rez=cifri[0];
        for(i=1; i<l; i++)
        {
            tmp=10;
            for(j=1; j<i; j++)
                tmp*=10;
            tmp*=cifri[i];
            rez+=tmp;
        }

        fout<<"Case #"<<k<<": "<<rez<<endl;
    }
    return 0;
}
