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
int n;
int k;
double pancake[1005][2];
void swap(int &a,int &b)
{
    int tmp=a;
    a=b;
    b=tmp;
}
int main()
{
    while(infile>>t)
    {
        for(int i=0;i<t;++i)
        {
            infile>>n>>k;
            int used[1005]={0};
            int result2[1005]={0};
            int paixu1[1005]={0};
            int num=0;
            for(int j=0;j<n;++j)infile>>pancake[j][0]>>pancake[j][1];
            while(num<n)
            {
                double result=-1;
                int index=0;
                for(int j=0;j<n;++j)
                {
                    if(!used[j])
                    {
                        if(pancake[j][0]>result)
                        {
                            result=pancake[j][0];
                            index=j;
                        }
                    }
                }
                paixu1[num++]=index;
                used[index]=1;
            }
            double result=0;
            for(int j=0;j<=n-k;++j)
            {
                double tmp=0;
                tmp+=pancake[paixu1[j]][0]*pancake[paixu1[j]][0];
                tmp+=2*pancake[paixu1[j]][0]*pancake[paixu1[j]][1];
                int candidate[1005]={0};
                for(int l=j+1;l<n;++l)candidate[l-j-1]=paixu1[l];
                for(int l=0;l<k-1;++l)
                {
                for(int k=n-1-j-1;k>l;--k)
                {
                    int index1=candidate[k];
                    int index2=candidate[k-1];
                    if(pancake[index1][0]*pancake[index1][1]>pancake[index2][0]*pancake[index2][1])
                    {
                        swap(candidate[k],candidate[k-1]);
                    }
                }
                }
                for(int l=0;l<k-1;++l)tmp+=2*pancake[candidate[l]][0]*pancake[candidate[l]][1];
                if(tmp>result)result=tmp;
            }
            outfile<<fixed<<setprecision(7)<<"Case #"<<i+1<<": "<<result*PI<<endl;
        }
    }
}
