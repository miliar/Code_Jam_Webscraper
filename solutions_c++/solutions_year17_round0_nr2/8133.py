#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


bool check_tidy(string&);
string find_tidy(string&);
int main()
{
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        string num;
        cin>>num;
        cout<<"Case #"<<i<<": ";
        if(check_tidy(num)){
            cout<<num<<endl;
            continue;
        }
        num=find_tidy(num);
        for(int i=0;i<num.size();i++)
        {
            if(i==0 && num[i]=='0')
                while(num[i]=='0')
            {
                i++;
            }
            cout<<num[i];
        }
        cout<<endl;
    }
    return 0;
}

string find_tidy(string &num)
{
    for(int i=num.size()-1;i>=1;i--)
    {
        num[i]='9';
        if(num[i-1]<='1')
            num[i-1]='0';
        else
            num[i-1]=num[i-1]-1;
        if(check_tidy(num))
            return num;
    }
    return num;
}

bool check_tidy(string &num)
{
    for(int i=num.size()-1;i>=1;i--)
    {
        if(num[i]<num[i-1])
            return 0;
    }
    return 1;
}
