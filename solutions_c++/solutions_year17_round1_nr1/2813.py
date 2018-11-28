#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <cstdio>
#include <iomanip>
#include <map>
#include <string.h>
#include <utility>
using namespace std;
int t;
int r;
int c;
int can[30][2][2]={0};
int used[30]={0};
char grid[30][30];
int mim(int a,int b)
{
    return a<=b?a:b;
}
int max1(int a,int b)
{
    return a>=b?a:b;
}
ifstream infile("file.in");
ofstream outfile("file.out");
bool conflict(int j,int x1,int y1 ,int x2,int y2)
{
    for(int i=0;i<30;++i)
    {
        if(i==j || !used[i])continue;
        else
        {
            int x11=can[i][0][0];
            int y11=can[i][0][1];
            int x22=can[i][1][0];
            int y22=can[i][1][1];
            if(x1<=x22 && x1>=x11 && y1<=y22 && y1>=y11)return true;
            if(x2<=x22 && x2>=x11 && y2<=y22 && y2>=y11)return true;
            if(x2<=x22 && x2>=x11 && y1<=y22 && y1>=y11)return true;
            if(x1<=x22 && x1>=x11 && y2<=y22 && y2>=y11)return true;
            
            if(x11<=x2 && x11>=x1 && y11<=y2 && y11>=y1)return true;
            if(x22<=x2 && x22>=x1 && y22<=y2 && y22>=y1)return true;
            if(x22<=x2 && x22>=x1 && y11<=y2 && y11>=y1)return true;
            if(x11<=x2 && x11>=x1 && y22<=y2 && y22>=y1)return true;
        }
    }
    return false;
}
void extend_h(int i)
{
    int x1=can[i][0][0];
    int y1=can[i][0][1];
    int x2=can[i][1][0];
    int y2=can[i][1][1];
    while(!conflict(i, x1, y1, x2, y2))
    {
        if(y1==0)break;
        else
        {
            --y1;
        }
    }
    if(conflict(i, x1, y1, x2, y2))
    {
        ++y1;
    }
    while(!conflict(i, x1, y1, x2, y2))
    {
        if(y2==c-1)break;
        else
        {
            ++y2;
        }
    }
    if(conflict(i, x1, y1, x2, y2))
    {
        --y2;
    }
    can[i][0][1]=y1;
    can[i][1][1]=y2;
}
void extend_s(int i)
{
    int x1=can[i][0][0];
    int y1=can[i][0][1];
    int x2=can[i][1][0];
    int y2=can[i][1][1];
    while(!conflict(i, x1, y1, x2, y2))
    {
        if(x1==0)break;
        else
        {
            --x1;
        }
    }
    if(conflict(i, x1, y1, x2, y2))
    {
        ++x1;
    }
    while(!conflict(i, x1, y1, x2, y2))
    {
        if(x2==r-1)break;
        else
        {
            ++x2;
        }
    }
    if(conflict(i, x1, y1, x2, y2))
    {
        --x2;
    }
    can[i][0][0]=x1;
    can[i][1][0]=x2;
}
void extend_l(int i)
{
    int x1=can[i][0][0];
    int y1=can[i][0][1];
    int x2=can[i][1][0];
    int y2=can[i][1][1];
    while(!conflict(i, x1, y1, x2, y2))
    {
        if(x1==0 || y1==0)break;
        else
        {
            --x1;
            --y1;
        }
    }
    if(conflict(i, x1, y1, x2, y2))
    {
        ++x1;
        ++y1;
    }
    while(!conflict(i, x1, y1, x2, y2))
    {
        if(x2==r-1 || y2==c-1)break;
        else
        {
            ++x2;
            ++y2;
        }
    }
    if(conflict(i, x1, y1, x2, y2))
    {
        --x2;
        --y2;
    }
    can[i][0][0]=x1;
    can[i][1][0]=x2;
    can[i][0][1]=y1;
    can[i][1][1]=y2;
 //   cout<<x1<<' '<<y1<<' '<<x2<<' '<<y2<<endl;
}
void initial()
{
    memset(used,0,sizeof(used));
    for(int i=0;i<30;++i)
    {
        can[i][0][0]=1000000;
        can[i][0][1]=1000000;
        can[i][1][0]=-1;
        can[i][1][1]=-1;
    }
}
int main()
{
    while(infile>>t)
    {
        for(int i=0;i<t;++i)
        {
            infile>>r>>c;
            initial();
            outfile<<"Case #"<<i+1<<":"<<endl;
            for(int j=0;j<r;++j)
            {
                for(int k=0;k<c;++k)
                {
                    infile>>grid[j][k];
                    if(grid[j][k]=='?')continue;
                    used[grid[j][k]-'A']=1;
                    can[grid[j][k]-'A'][0][0]=mim(j,can[grid[j][k]-'A'][0][0]);
                    can[grid[j][k]-'A'][0][1]=mim(k,can[grid[j][k]-'A'][0][1]);
                    can[grid[j][k]-'A'][1][0]=max1(j,can[grid[j][k]-'A'][1][0]);
                    can[grid[j][k]-'A'][1][1]=max1(k,can[grid[j][k]-'A'][1][1]);
                }
            }
            for(int j=0;j<30;++j)
            {
                if(used[j])
                {
                    
                    extend_l(j);
                    extend_h(j);
                    extend_s(j);
                    int x1=can[j][0][0];
                    int y1=can[j][0][1];
                    int x2=can[j][1][0];
                    int y2=can[j][1][1];
                    //cout<<char(j+'A')<<' '<<x1<<' '<<y1<<' '<<x2<<' '<<y2<<endl;
                    for(int k=x1;k<=x2;++k)
                    {
                        for(int l=y1;l<=y2;++l)grid[k][l]=j+'A';
                    }
                }
            }
            for(int j=0;j<r;++j)
            {
                for(int l=0;l<c;++l)outfile<<grid[j][l];
                outfile<<endl;
            }
        }
        
    }
}
