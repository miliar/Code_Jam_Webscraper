#include<bits/stdc++.h>
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    freopen("C:\\Downloads\\Documents\\Downloads\\B.in","r",stdin);
    freopen("C:\\Downloads\\Documents\\Downloads\\out.txt","w",stdout);
    int t;
    cin>>t;
    int h=1;
    while(t--)
    {
        string s;
        cin>>s;
        for(int i=s.length()-1;i>0;i--)
        {
            char ch=s[i];
            char ch1=s[i-1];
            if(ch<ch1)
            {
                for(int j=i;j<s.length();j++)
                    s[j]='9';
                while(true)
                {
                    if(s[i-1]=='0')
                        s[i-1]='9';
                    else
                    {
                         s[i-1]=s[i-1]-1;
                         break;
                    }
                }
            }
        }
        cout<<"Case "<<"#"<<h++<<":"<<" ";
        int g=0;
        for(int i=0;i<s.length();i++)
        {
            if(s[i]!='0')
            {
                g=1;
            }
            if(g)
                cout<<s[i];
        }
        cout<<"\n";

    }
    return 0;
}
