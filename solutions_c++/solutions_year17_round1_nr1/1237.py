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
char board[30][30];
bool kong[30];
int R,C;

int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>T;
    int times=1;
    while(T--)
    {
        
        cin>>R>>C;
        for(int i=1;i<=R;i++)
        {
            for(int j=1;j<=C;j++)
            {
                cin>>board[i][j];
            }
        }
        
        memset(kong ,0,sizeof(kong));
        
        for(int i=1;i<=R;i++)
        {
            
            bool jud=true;
            for(int j=1;j<=C;j++)
            {
                if(board[i][j]!='?')
                {
                    jud=false;
                    break;
                }
            }
            if(jud)
            {
                kong[i]=true;
            }
        }
        
        
        //对不空的每一行进行处理
        for(int i=1;i<=R;i++)
        {
            if(kong[i])
                continue;
            else
            {
                int index=0;    //最后一个不是?的字符的位置
                for(int j=1;j<=C;j++)
                {
                    if(board[i][j]=='?')
                        continue;
                    else
                    {
                        for(int k=index+1;k<j;k++)
                        {
                            board[i][k]=board[i][j];
                        }
                        index=j;
                    }
                }
                for(int k=index+1;k<=C;k++)
                    board[i][k]=board[i][index];
            }
        }
        
        
        //对全局进行处理
        int index=0;
        for(int i=1;i<=R;i++)
        {
            if(kong[i])
                continue;
            else
            {
                for(int k=index+1;k<i;k++)
                {
                    for(int l=1;l<=C;l++)
                    {
                        board[k][l]=board[i][l];
                    }
                }
                index=i;
            }
            
            
        }
        
        
        
       
        
        for(int k=index+1;k<=R;k++)
        {
            for(int l=1;l<=C;l++)
                board[k][l]=board[index][l];
        }
        
        //输出
        cout<<"Case #"<<times<<":"<<endl;
        times++;
        for(int i=1;i<=R;i++)
        {
            for(int j=1;j<=C;j++)
                cout<<board[i][j];
            cout<<endl;
        }
       
        
    }
    
    
    fclose(stdin);
    fclose(stdout);
}
