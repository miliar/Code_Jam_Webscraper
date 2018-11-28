#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);
    int t,k,i,cnt,flag,j,a=1;
    string s;
    cin>>t;
    while(a<=t)
    {
        cin>>s>>k;
        cnt=0;
        flag=1;
        for(i=0;i<s.length();i++)
        {
            if(s[i]=='-')
            {
                if(i+k<=s.length())
                {
                    cnt++;
                    for(j=i;j<i+k;j++)
                    {
                        if(s[j]=='-')
                            s[j]='+';
                        else
                            s[j]='-';
                    }
                }
                else
                {
                    flag=0;
                    break;
                }
            }
        }
        if(flag)
            cout<<"Case #"<<a<<": "<<cnt<<endl;
        else
            cout<<"Case #"<<a<<": "<<"IMPOSSIBLE"<<endl;
        a++;
    }
}














