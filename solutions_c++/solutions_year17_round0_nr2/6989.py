
#include<bits/stdc++.h>
using namespace std;
string s,ss;

int main()
{

    int n,t,i,j,rr,r=1;
    cin>>t;
    while(t--)
    {
        ss.clear();
        s.clear();
        cin>>s;
        n=s.size();
        if(n==1)
        {
                ss=s;

        }
        else{
        for(i=n-2;i>=0;i--)
        {
            if(s[i]!='0'&&s[i+1]<s[i])
            {
                s[i]--;
                for(j=i+1;j<n;j++)
                    s[j]='9';
            }

        }
        for(i=0;i<n;i++)
        {
            if(s[i]!='0')
                    break;
        }
        ss=s.substr(i);
        }
        cout<<"Case #"<<r<<": "<<ss<<"\n";
        r++;
    }
}
