#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,m=0;
    ifstream input;
    input.open("B-large.in");
    ofstream output;
    output.open("codejam4.txt");

    input>>t;
    while (t!=0)
    { t--;
        m++;
        long long n,q,c=0,i;  int b[19]={0};
        long long w,z=0,k;
        input>>n;
        q=n;
        while (q>0)
        { c++;
            q=q/10;

        }

        q=n;
        for (i=0;i<=c-1;i++)
        {
            w=q%10;

            q=q/10; b[i]=w;
        }
        for (i=0;i<=c-2;i++)
        {
            if (b[i]<b[i+1])
            {

                for (k=0;k<=i;k++)
                {
                    b[k]=9;

                }
                b[i+1]--;
            }
        }

        output<<"Case #"<<m<<": ";
        for (i=c-1;i>=0;i--)
        {
            if (b[i]!=0||z!=0)
        {



                output<<b[i];
                z=1;
            }
        }
        output<<"\n";
    }
    return 0;
}
