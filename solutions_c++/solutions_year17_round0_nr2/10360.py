#include<iostream>
#include<stdio.h>
#include<fstream>
using namespace std;

int main()
{
int data,i,j,x,n,d,tidy,next;
ifstream infile;
infile.open("input.txt");
ofstream outfile;
   outfile.open("output.txt");
infile>>data;
if(data>0)
{
    for(i=1;i<=data;i++)
    {
        infile>>x;
        if(x>10)
        {
            for(j=10;j<=x;j++)
            {
                n=j;
                while(n)
                {
                    d=n%10;
                    next=(n/10);
                    next%=10;

                    if(d<next)
                        break;
                    n=n/10;
                    if(!n)
                    {
                        tidy=j;
                    }
                }
            }
        }
        else
        {
            tidy=x;
        }
    outfile<<"Case #"<<i<<": "<<tidy<<endl;
    }

}
}

