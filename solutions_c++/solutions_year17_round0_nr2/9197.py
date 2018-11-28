#include<iostream>
#include<fstream>
#include<math.h>
using namespace std;
long long int power(int p,int l)
{
    if(l<0)
        return 0;
    long long int sum=1;
    while(l>=1)
    {
        sum*=p;
        l--;
    }
    return sum;
}

int main()
{
    ifstream fin("B-large.in");
    ofstream fout("outputfile.txt");
    int t,a,b;
    long long int p,l,m,g;
    fin>>t;
    for(int i=0;i<t;i++)
    {
        fin>>p;
        label:l=p;
        a=0,b=0;
        int c=0;
        while(l>0)
        {
            c++;
            l=l/10;
        }
        c=c-1;
        l=p;
        m=power(10,c);
        c=c+1;
        while(a<=b && c>=1)
        {
            a=b;
            b=l/m;
            l=l%m;
            if(m>=10)
            {
                m=m/10;
            }
            c--;
        }
        cout<<a<<" "<<b<<" "<<c<<" "<<l<<p<<" \n";
        if((a<=b)&& (c==0))
        {
            l=0;
        }
        else
        {
            l=b*power(10,c)+l+1;
        }
        p=p-l;
        g=p;
        a=19,b=19,c=0;
        while(g>0)
        {
            a=b;
            b=g%10;
            g=g/10;
            if(a<b)
            {
                goto label;
            }
        }
        fout<<"case #"<<i+1<<": "<<p<<"\n";
    }

return 0;
}
