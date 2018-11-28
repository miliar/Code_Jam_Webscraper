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
int ac;
int aj;
int man1[105][2]={0};
int man2[105][2]={0};
int max1(int a,int b)
{
    return a>=b?a:b;
}
int mim(int a,int b)
{
    return a<=b?a:b;
}
int main()
{
    while(infile>>t)
    {
        for(int i=0;i<t;++i)
        {
            outfile<<"Case #"<<i+1<<": ";
            infile>>ac>>aj;
            for(int j=0;j<ac;++j)
            {
                infile>>man1[j][0]>>man1[j][1];
            }
            for(int j=0;j<aj;++j)infile>>man2[j][0]>>man2[j][1];
            if(ac+aj==1)
            {
                outfile<<2<<endl;
            }
            else
            {
                if(ac==1 && aj==1)
                {
                    outfile<<2<<endl;
                }
                else
                {
                    if(ac==2)
                    {
                        int right=max1(man1[0][1],man1[1][1]);
                        int left=mim(man1[0][0],man1[1][0]);
                        if(right-left<=720)outfile<<2<<endl;
                        else
                        {
                            int left2=max1(man1[0][0],man1[1][0]);
                            int right2=mim(man1[0][1],man1[1][1]);
                            if(left2-right2>=720)outfile<<2<<endl;
                            else
                            {
                               outfile<<4<<endl;
                            }
                        }
                    }
                    else
                    {
                        int right=max1(man2[0][1],man2[1][1]);
                        int left=mim(man2[0][0],man2[1][0]);
                        if(right-left<=720)outfile<<2<<endl;
                        else
                        {
                            int left2=max1(man2[0][0],man2[1][0]);
                            int right2=mim(man2[0][1],man2[1][1]);
                            if(left2-right2>=720)outfile<<2<<endl;
                            else
                            {
                                outfile<<4<<endl;
                            }
                        }
                    }
                }
            }
        }
    }
}
