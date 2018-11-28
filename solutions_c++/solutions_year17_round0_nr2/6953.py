#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int ii=1;ii<=t;ii++)
    {

        string s;
        int f=1,i,j;
        cin>>s;
        cout<<"Case #"<<ii<<": ";
        for(i=0;i<s.length()-1;i++)
        {
            if(s[i]>s[i+1])
            {
                f=0;
                break;
            }
        }
        if(f)
        {
            cout<<s;
        }
        else
        {
                s[i]--;
                for(j=i-1;j>=0;j--)
                {
                    if(s[j]>s[j+1])
                    {
                        s[j]=s[j+1];
                        s[j+1]='9';
                    }

                }
                for(j=i+1;j<s.length();j++)
                    s[j]='9';
                int lz=0;
                for(i=0;i<s.length();i++)
                {
                    if(s[i]!='0') break;
                    lz++;
                }
                if(!lz)
                cout<<s;
                else
                {
                    lz--;
                    while(lz--) cout<<"9";
                    for(j=i;j<s.length();j++) cout<<s[j];
                }
        }
        cout<<endl;

    }
    return 0;
}
