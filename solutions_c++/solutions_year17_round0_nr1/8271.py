//a题
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
using namespace std;

//输入


int main(){
    
    
    // freopen("in.txt","r",stdin);
    // freopen("out","w",stdout);
    
    int T;
    cin>>T;
    int id=1;
    while(T--)
    {
        string str;
        cin>>str;
        int len=str.length();
        int K;
        cin>>K;
        int res=0;
        for(int i=0;i<=len-K;i++)
        {
            if(str[i]=='+')
            {
                
            }
            else
            {
                res++;
                int j;
                for(j=i;j<i+K;j++)
                {
                    if(str[j]=='+')
                        str[j]='-';
                    else
                        str[j]='+';
                }
                
            }
            //cout<<str<<endl;
        }
        
        bool jud=true;
        for(int i=len-1;i>=0;i--)
        {
            if(str[i]=='-')
            {
                jud=false;
                break;
            }
        }
        if(jud)
        {
            cout<<"Case #"<<id<<": "<<res<<endl;
            id++;
        }
        else
        {
            cout<<"Case #"<<id<<": IMPOSSIBLE"<<endl;
            id++;
        }
        
    }
}
