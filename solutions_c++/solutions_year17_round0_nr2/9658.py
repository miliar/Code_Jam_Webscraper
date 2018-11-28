#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("a.txt","w",stdout);
    int t;
    cin>>t;
    int c=1;
    while(t--)
    {
        string s;
        cin>>s;
        int k=0,l=0;
        for(int i=0;i<s.size()-1;i++)
        {
           if(s[i]>s[i+1])
           {
               k=i;

               l=i;
               break;
           }
        }
        for(int i=k;i>0;i--)
        {
            if(s[i]==s[i-1])
                k=i-1;
        }
        if(k!=0 )
        {
            if(s[k]!=48||s[k]!=49)
            {s[k]=s[k]-1;
            for(int i=k+1;i<s.size();i++)
                s[i]='9';
            }
        }
        if(k==0&&l!=0)
        {
            if (s[k]!='1')
               {s[k]=s[k]-1;
            for(int i=k+1;i<s.size();i++)
                s[i]='9';
            }
            if(s[k]=='1')
            {
                s.erase(k,1);
                for(int i=0;i<s.size();i++)
                s[i]='9';

            }
        }
        if(k==0&&l==0&&(s.size()>1)&&(s[0]>s[1]))
        {
            if(s[0]=='1')
            {
                s.erase(k,1);
                for(int i=0;i<s.size();i++)
                s[i]='9';
            }
            else
                {s[k]=s[k]-1;
            for(int i=k+1;i<s.size();i++)
                s[i]='9';
            }

        }
        cout<<"Case #"<<c<<": "<<s<<endl;

c++;
    }
    return 0;
}
