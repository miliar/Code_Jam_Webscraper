#include<bits/stdc++.h>
using namespace std;

int main()
{

    freopen("inp.txt","r",stdin);
    freopen("output.txt","w",stdout);


    int t;
    cin>>t;

    int curr=1;
    while(t--)
    {

        string s;
        cin>>s;
        if(s.size()==1)
        {


             cout<<"Case #"<<curr<<": ";
            cout<<s[0]<<"\n";
            curr++;
        }
        else
        {

        for(int i=0;i<s.size()-1;i++)
        {

            if(s[i]>s[i+1])
            {
                int j;
                for(j=i-1;j>=0;j--)
                {

                    if(s[j]!=s[i])
                        break;
                }
               // cout<<j<<"hello\n";
                s[j+1]=(char)(s[j+1]-1);

                for(int k=j+2;k<s.size();k++)
                    s[k]='9';
                break;
            }
        }
        int i=0;
        while(s[i]=='0')
        {
            i++;
        }
        //for(int j=i;j<s.size();j++)
            cout<<"Case #"<<curr<<": ";
            for(int j=i;j<s.size();j++)
            cout<<s[j];
        cout<<"\n";
        curr++;
    }
    }
}
