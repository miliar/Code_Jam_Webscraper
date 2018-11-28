#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <stack>
using namespace std;


int main() {
    int n,a,f=0,flag=1,r=0;
    string t;
    cin>>n;
    while(n--)
    {
        r++;
        cin>>t>>a;
        for(int i=0;i<t.size()-a+1;i++)
        {
            if(t[i]=='+')
                continue;
            else
            {
            f=f+1;
            for(int j=i;j<i+a;j++)
            {
                if(t[j]=='+')
                    t[j]='-';
                else
                    t[j]='+';


            }
           /* cout<<t<<endl;
            cout<<f<<endl;*/
            }

        }
        for(int i=t.size()-a;i<t.size();i++)
        {
            if(t[i]=='-')
            {
                flag=0;
                break;
            }

        }
        if(flag==0)
            cout<<"Case #"<<r<<":"<<" "<<"IMPOSSIBLE"<<endl;
        else
            cout<<"Case #"<<r<<":"<<" "<<f<<endl;
        f=0;
        flag=1;

    }

    return 0;
    }

