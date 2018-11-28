#include<iostream>
#include<fstream>
using namespace std;
int tidy(int x);
int main()
{
    ifstream fin;
    fin.open("B-small-attempt0.in");
    ofstream fout;
    fout.open("B-small-attempt0.out");
    int i,t,n[100],c;
    fin>>t;
    for(i=0;i<t;i++)
    {
        fin>>n[i];
    }
    for(i=0;i<t;i++)
    {
        c=tidy(n[i]);
        fout<<"Case #"<<i+1<<":"<<" "<<c<<endl;
    }
    return(0);
}
int tidy(int x)
{
    int i,j,a,b,d,tn;
    for(i=1;i<=x;i++)
    {
        a=i;
        d=-1;
        while(a>0)
        {
            b=a%10;
            a=a/10;
            if(d==-1)
            {
                d=b;
                continue;
            }
            if(d>=b)
            {
                d=b;
            }
            else
            {

                if(a==0)
                    a=-1;
                break;
            }
        }
        if(a==0)
        {
            tn=i;
        }
    }
    return(tn);
}






