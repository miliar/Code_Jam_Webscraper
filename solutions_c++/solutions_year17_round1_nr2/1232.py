//文件流的输入输出
//注意用Xcode时：文件栏->右键products下的exe文件->show in finder->在这里面添加输入文件、查找输出文件
#include <iostream>
#include <algorithm>
#include <string>
#include <sstream>
#include <set>
#include <vector>
#include <stack>
#include <map>
#include <queue>
#include <deque>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <ctime>
#include <functional>
#include <utility>
#include <iomanip>
#include <unordered_map>
#include <unordered_set>
using namespace std;
const double pi=acos(-1.0);
const double eps=0.000001;
const int MAX_N=100010;
const int INF=2147483647;
typedef long long  ll;

//输入
int T;
int N;  //材料种类
int P;  //每种材料的重量有多少种
int R[60]; //制作一道菜需要的材料重量
int Q[60][60];  //第i种材料的第j个重量
double RD[60];  //R*0.9;
double RU[60];  //R*1.1
double PD[60][60]; //serve最少的人
double PU[60][60];  //serve最多的人
bool used[60][60];
int res;
int pre[60][60];

//3 3
//70 80 90
//1260 1500 700
//800 1440 1600
//1700 1620 900
//11 10    20 17    23 20
//11 10    20 17    22 19
//11 10    20 17    20 18



void huisu(int i,int j)
{
    if(i==1)
        return;
    used[i][j]=false;
    huisu(i-1,pre[i][j]);
}

void dfs(int index,double left,double right,int col)
{
    if(index==N+1 )
    {
        res++;
        return;
    }
    bool jud=false;
    for(int i=1;i<=P;i++)
    {
        if(!used[index][i] && PU[index][i]!=0 &&PD[index][i]!=0&& PU[index][i]>=PD[index][i] && PU[index][i]>=left && PD[index][i]<=right)
        {
            used[index][i]=true;
            jud=true;
            dfs(index+1,max(left,PD[index][i]),min(right,PU[index][i]),i);
            pre[index][i]=col;
        }
    }
    if(!jud)
    {
        huisu(index-1,col);
    }
}




int main(){
    freopen("B-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    
    cin>>T;
    int times=1;
    while(T--)
    {
        cin>>N>>P;
        memset(used,0,sizeof(used));
        for(int i=1;i<=N;i++)
        {
            cin>>R[i];
            RD[i]=R[i]*0.9;
            RU[i]=R[i]*1.1;
        }
        
        for(int i=1;i<=N;i++)
        {
            for(int j=1;j<=P;j++)
                cin>>Q[i][j];
            sort(Q[i]+1,Q[i]+1+P);
        }
        for(int i=1;
            i<=N;i++)
        {
            for(int j=1;j<=P;j++)
            {
                //有错误
                //计算PD
                double tmp1=ceil(Q[i][j]/RU[i]);
                if(tmp1*RD[i]>Q[i][j])
                    PD[i][j]=0;
                else
                    PD[i][j]=tmp1;
                
                double tmp2=floor(Q[i][j]/RD[i]);
                if(tmp2*RU[i]<Q[i][j])
                    PU[i][j]=0;
                else
                    PU[i][j]=floor(Q[i][j]/RD[i]);
            }
        }
        
//         //test
//         for(int i=1;i<=N;i++)
//         {
//             for(int j=1;j<=P;j++)
//             {
//                 cout<<PU[i][j]<<" "<<PD[i][j]<<"    ";
//             }
//             cout<<endl;
//         }
        
        //开始计算
        res=0;
        if(N==1)
        {
            for(int i=1;i<=P;i++)
            {
                if(PU[1][i]!=0 && PD[1][i]!=0)
                    res++;
            }
        }
        else
        {
        for(int i=1;i<=P;i++)
        {
            double left=PD[1][i];
            double right=PU[1][i];
            dfs(2,left,right,i);
        }
        }
        cout<<"Case #"<<times<<": "<<res<<endl;
        times++;
        
    }
    
    
    
    
    
    fclose(stdin);
    fclose(stdout);
}




