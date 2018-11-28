#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("outputl.txt","w",stdout);
    int q;
    string s;
    cin>>q;
    int z=1;
    while(z!=q+1)
    {
        cin>>s;
        for(int i=s.length()-2;i>=0;i--)
        {
            if(s[i]>s[i+1])
            {
                for(int j=i;j<s.length()-1;j++)
                    s[j+1]='9';
                if(int(s[i])>47)
                {
                    s[i]=s[i]-1;
                }

                else
                    s[i]='9';
            }
        }
        cout<<"Case #"<<z<<": ";
        if(s[0]=='0')
        {
            for(int i=1;i<s.length();i++)
                cout<<s[i];
            cout<<endl;
        }
        else
            cout<<s<<endl;
        z++;
    }
    return 0;
}

