//
//  main.cpp
//  GoogleCodeJam
//
//  Created by yujian liu on 4/6/17.
//  Copyright © 2017 yujian liu. All rights reserved.
//
#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text

int testtidy(int n)
{
    int temp=0,max=n%10;
    while(n>0)
    {
        temp=n%10;
        if(max<temp)
            return 0;
        max=temp;
        n=n/10;
    }
    return 1;
}

void TidyNums()
{
    int t;
    cin >> t;
    for(int i=0;i<t;i++)
    {
        int n;
        cin >> n;
        cout<<"Case #"<<i+1<<": ";
        if(n<10)
        {
            cout<<n<<endl;
        }
        else
        {
            for(int i=n;i>0;i--)
            {
                if(testtidy(i)==1)
                {cout<< i <<endl;
                    break;}
            }
        }
        
    }
}

void TidyNums_large()
{
    int t;
    cin >> t;
    for(int i=0;i<t;i++)
    {
        string s;
        cin >> s;
        cout << "Case #"<<i+1<<": ";
        int len = s.size();
        if(len==1)
            {
                cout<<s<<endl;
            }
        else
        {
            
            for(int j=len-2;j>=0;j--)
            {
                if(s[j]>s[j+1])
                {
                    s[j]-=1;
                    for(int k=j+1;k<len;k++)
                    {s[k]='9';}
                }
            }
            while(s[0]=='0')
            {
                s.erase(s.begin());
            }
            cout << s<<endl;
        }
    }
}
void Bathroom_Stalls()
{
    int t;
    cin >> t;
    for(int i = 0;i < t;i++)
    {
        int m, n;
        cin >> m >> n;
        
    }
}
int main() {
    TidyNums_large();
        return 0;
}
