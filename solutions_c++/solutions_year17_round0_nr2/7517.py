#include<iostream>
#include<fstream>
using namespace std;
ifstream in("tidy.in");
ofstream out("tidy.out");

unsigned long long int pow(int baza,int exp)
{
    unsigned long long int x=1;
    int i;
    if(exp==0)
        return 1;
    else
    {
        for(i=1;i<=exp;i++)
            x=baza*x;
        return x;
    }
}

unsigned long long int solve(unsigned long long int n)
{
    int nr[25], i=0, k=1, l;
    while(n)
    {
        i++;
        nr[i]=n%10;
        n/=10;
    }
    for(k=1;k<i;k++)
    {
        if(nr[k]<nr[k+1])
        {
            nr[k+1]--;
            while(k>0)
            {
                nr[k]=9;
                k--;
            }

            k=0;
        }
    }
    n=0;
    for(l=1;l<=i;l++)
        n+=nr[l]*pow(10,l-1);
    return n;
}

int main()
{
    unsigned long long int n;
    int i, cases;
    in>>cases;
    for(i=1;i<=cases;i++)
    {
        in>>n;
        out<<"Case #"<<i<<": "<<solve(n)<<endl;
    }

}
