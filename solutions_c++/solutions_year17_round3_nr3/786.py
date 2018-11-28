#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>
#define PI 3.14159265358979323846
using namespace std;
ifstream infile("file.in");
ofstream outfile("file.out");
int t;
int n,k;
double u;
double possi[100];
double mim(double a,double b)
{
    return a<=b?a:b;
}
double mean(int j)
{
    double tmp=0;
    for(int k=0;k<=j;++k)
    {
        tmp+=possi[k];
    }
    tmp+=u;
    return tmp/(j+1);
}
int main()
{
    while(infile>>t)
    {
        for(int i=0;i<t;++i)
        {
            infile>>n>>k>>u;
            for(int j=0;j<n;++j)infile>>possi[j];
            for(int j=0;j<n;++j)
            {
                for(int k=n-1;k>j;--k)
                {
                    if(possi[k]<possi[k-1])
                    {
                        double tmp=possi[k];
                        possi[k]=possi[k-1];
                        possi[k-1]=tmp;
                    }
                }
            }
            double result=1;
            int st=0;
            while(mean(st)>=possi[st])
            {
                ++st;
                if(st==n)break;
            }
            if(st==n)
            {
                double tmp=mean(n-1);
                cout<<tmp<<endl;
                for(int j=0;j<n;++j)
                {
                    if(possi[j]>=tmp)
                    {
                        result*=possi[j];
                    }
                    else
                    {
                        result*=tmp;
                    }
                }
            }
            else
            {
                double tmp=mean(st-1);
                for(int j=0;j<st;++j)
                {
                    if(possi[j]>=tmp)result*=possi[j];
                    else
                    {
                        result*=tmp;
                    }
                }
                for(int j=st;j<n;++j)result*=possi[j];
            }
            if(result==0)cout<<i<<endl;
            outfile<<fixed<<setprecision(7)<<"Case #"<<i+1<<": "<<result<<endl;
        }
    }
}
