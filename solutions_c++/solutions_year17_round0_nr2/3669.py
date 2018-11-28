#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    int t,i,j,a=1;
    string s;
    cin>>t;
    while(a<=t)
    {
        cin>>s;
        for(i=s.length()-2;i>=0;i--)
        {
            if(s[i]>s[i+1])
            {
                s[i]--;
                for(j=i+1;j<s.length();j++)
                    s[j]='9';
            }
        }
        while(s[0]=='0')
            s.erase(s.begin());
        cout<<"Case #"<<a<<": "<<s<<endl;
        a++;
    }
}














