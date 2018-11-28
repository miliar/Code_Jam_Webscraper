//b题
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

void solve(string &str,int i)
{
    for(int j=i;j<str.length();j++)
    {
        str[j]='9';
    }
    str[i-1]=str[i-1]-1;
}

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
            while(true)
            {
                bool jud=true;
                int i;
                for(i=1;i<len;i++)
                {
                    if(str[i]-str[i-1]>=0)
                    {
                    }
                    else
                    {
                        jud=false;
                        break;
                    }
                }
                if(jud)
                {
                    cout<<"Case #"<<id<<": ";
                    bool bg=false;
                    for(int i=0;i<str.length();i++)
                    {
                        if(str[i]=='0')
                        {
                            if(!bg)
                            {}
                            else
                                cout<<str[i];
                        }
                        else
                        {
                            cout<<str[i];
                            bg=true;
                        }
                        
                    }
                    
                    
                    cout<<endl;
                    id++;
                    break;
                }
                else
                {
                    solve(str,i);
                }
            
        }
        
        
        
        
    }
    
    
    // fclose(stdin);
    // fclose(stdout);
}