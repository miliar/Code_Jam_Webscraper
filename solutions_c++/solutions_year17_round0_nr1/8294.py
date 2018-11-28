#include<iostream>
#include<string>
#include<cmath>
#include<math.h>
#include<map>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin>>t;
    for(int ii=1;ii<=t;ii++)
    {
        int i,j,l,k,a=0;
        string s;
        cin>>s>>k;
        l=s.length();
        for(i=0;i<l-k+1;i++)
        {
            if(s[i]=='+') continue;
            a++;
            for(j=i;j<i+k;j++)
            {
                if(s[j]=='-') s[j]='+';
                else s[j]='-';
            }
        }
        for(i=0;i<l;i++)
            if(s[i]!='+')
               a=-1;
        if(a==-1) cout<<"Case #"<<ii<<": "<<"IMPOSSIBLE"<<endl;
        else
            cout<<"Case #"<<ii<<": "<<a<<endl;
    }
    return 0;
}