#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <limits>
using namespace std;
 
int main()
{
    int t ;
    cin>>t ;
    int i,j ;
    string num,temp ;
    for(i=1;i<=t;i++)
    {   cin>>num ;
        temp = num ;
        sort(temp.begin(),temp.end()) ;
        cout<<"Case #"<<i<<": " ;
        if(num==temp)
        {    cout<<num<<endl ;
            continue ;
        }
        else
        {
        for(j=num.length();j>0;j--)
        {   
            if(num[j]==0&&num[j-1]==1)
            {   num[j]='9' ;
                    
            }
            else if(num[j]==0&&num[j-1]==0)
                num[j]='9' ;
            else if(num[j]<num[j-1]&&num[j-1]!=1)
            {
                num[j]='9' ;
                num[j-1]=num[j-1]-1 ;
            }    
            else if(num[j]<num[j-1]&&num[j-1]==1)
            {
                num[j-1]='9' ;
            }
        }
        if(num.find('0')!=string::npos)
           num.erase(num.begin()) ;
        }
        cout<<num<<endl ;
    }
    
   return 0 ; 
    }