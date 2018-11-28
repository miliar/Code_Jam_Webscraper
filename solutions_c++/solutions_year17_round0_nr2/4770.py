#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

#define mod 1000000007
#define ll long long

int main()
{
    string num;
    int t,i,flag;
    
   freopen("input2.in","r",stdin);
   freopen("output2.txt","w",stdout);
    
    cin>>t;
    
    for(int j=0;j<t;j++)
    {
        
        cin>>num;
        int k=20;
        while(k--)
        {
            flag=0;
            for(i=1;num[i];i++)
            {
                if(num[i]<num[i-1])
                {
                    num[i-1]=num[i-1]-1;
                    while(num[i])
                    {num[i++]='9';}
                    flag=1;
                    break;
                }
            }
            if(flag==0)
            break;
        }
        i=0;
        while(num[i]=='0')
        {i++;}
        cout<<"Case #"<<j+1<<": ";
        for( ;num[i];i++)
        cout<<num[i];
        cout<<endl;
    }
}
