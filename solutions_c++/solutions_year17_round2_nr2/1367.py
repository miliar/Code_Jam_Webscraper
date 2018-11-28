#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
ifstream infile("file.in");
ofstream outfile("file.out");
int t;
int n;
//R, O, Y, G, B, and V.;
int color[6];
char colorname[7]="ROYGBV";
int main()
{
    while (infile>>t) {
        for(int i=0;i<t;++i)
        {
            infile>>n;
            outfile<<"Case #"<<i+1<<": ";
            int flag=0;
            for(int i=0;i<6;++i)infile>>color[i];
            int index1[6]={0};
            for(int i=0;i<6;++i)index1[i]=i;
            for(int i=1;i<=6;++i)
            {
                for(int j=5;j>i-1;--j)
                {
                    if(color[index1[j]]>color[index1[j-1]])
                    {
                        int tmp=index1[j];
                        index1[j]=index1[j-1];
                        index1[j-1]=tmp;
                    }
                }
            }
            if(color[index1[2]]>=color[index1[0]]-color[index1[1]])
            {
                flag=1;
            }
            if(!flag)
            {
                outfile<<"IMPOSSIBLE"<<endl;
                continue;
            }
            else
            {
                int remain=color[index1[2]]-(color[index1[0]]-color[index1[1]]);
               // int remain3==color[index1[2]]-remain;
                int remain2=color[index1[1]];
                for(int j=0;j<color[index1[0]];++j)
                {
                    outfile<<colorname[index1[0]];
                    if(remain2)
                    {
                        outfile<<colorname[index1[1]];
                        if(remain)
                        {
                            outfile<<colorname[index1[2]];
                            --remain;
                        }
                        --remain2;
                    }
                    else
                    {
                        outfile<<colorname[index1[2]];
                    }
                }
                outfile<<endl;
            }
        }
    }
}
