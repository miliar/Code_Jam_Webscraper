#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>
using namespace std;
ifstream infile("file.in");
ofstream outfile("file.out");
int t;
int n;
int q;
int goal[105][2]={0};
double tim[105]={0};
long long horse[101][2]={0};
long long graph[100][100]={0};
long long dist[100]={0};
double dp(int n)
{
    if(n==0)return 0;
    else
    {
        if(tim[n]!=0)return tim[n];
        else
        {
            double mim=100000000000;
            for(int j=0;j<n;++j)
            {
                if(horse[j][0]>=dist[n]-dist[j])
                {
                    double tmp=dp(j)+double(dist[n])/double(horse[j][1])-double(dist[j])/double(horse[j][1]);
                    mim=mim<=tmp?mim:tmp;
                }
            }
            tim[n]=mim;
            return tim[n];
        }
    }
}
double result(int i)
{
    double tmp=0;
    return tmp;
}
int main()
{
    while(infile>>t)
    {
        for(int i=0;i<t;++i)
        {
            infile>>n>>q;
            memset(tim,0,sizeof(tim));
            memset(dist,0,sizeof(dist));
            outfile<<"Case #"<<i+1<<": ";
            for(int j=0;j<n;++j)infile>>horse[j][0]>>horse[j][1];
            for(int j=0;j<n;++j)for(int k=0;k<n;++k)infile>>graph[j][k];
            for(int j=0;j<q;++j)infile>>goal[j][0]>>goal[j][1];
            for(int j=1;j<n;++j)dist[j]=dist[j-1]+graph[j-1][j];
            outfile<<fixed<<setprecision(8)<<dp(n-1)<<endl;
        }
    }
}
