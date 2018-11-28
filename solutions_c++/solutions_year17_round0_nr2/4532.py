#include<bits/stdc++.h>
using namespace std;
FILE *fin = freopen("in.txt","r",stdin);
FILE *fout = freopen("out.txt","w",stdout);
int main()
{
    int t;
    cin>>t;
    string s;
    for(int k=1;k<=t;k++)
    {
        cin>>s;
        for(int i=0;i<s.length()-1;i++)
        {
            if(s[i]>s[i+1])
            {
                char temp=s[i];
                int p=i;
                while(s[i]==temp)i--;
                i++;
                s[i]--;
                for(int j=i+1;j<=s.length();j++)
                    s[j]='9';

                break;
            }
        }
        if(s[0]!='0')
        cout<<"Case #"<<k<<": "<<s<<endl;
        else {cout<<"Case #"<<k<<": ";
            for(int i=1;i<s.length();i++)
                cout<<s[i];
                cout<<endl;
        }

    }
}

