#include <bits/stdc++.h>
#include <string>
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int j=0;j<t;j++)
    {
    	string s;
        cin>>s;
        int curr=s[s.length()-1],pos=s.length();
        for(int i=s.length()-2;i>=0;i--)
        {
            if(s[i]>curr)
            {
                s[i]=((s[i]-'0')-1)%10 +'0';
                pos=i+1;
                curr=s[i];
            }
            else
            {
                curr=s[i];
            }
        }
        unsigned long long ans=0;
        for(int i=0;i<s.length();i++)
        {
            if(i<pos)
                ans=ans*10 + s[i]-'0';
            else
                ans=ans*10 + 9;
        }
        cout<<"Case #"<<(j+1)<<": "<<ans<<endl;
    }
    return 0;
}
